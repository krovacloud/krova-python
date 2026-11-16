"""Run commands and move files on a Cube over its own SSH.

Krova has no exec or files API. Commands and files go straight from your process to the Cube's
SSH server, with a private key you supply. The Cube's host keys come from the API
(``cubes.ssh``) and are checked on every connection; there is no way to skip that check.
"""

from __future__ import annotations

import base64
import io
import os
import re
import shlex
import threading
import time
from collections.abc import Mapping, Sequence
from dataclasses import dataclass
from types import TracebackType
from typing import Any, Protocol

import paramiko
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import ec, ed25519, rsa

from .errors import HostKeyMismatchError, PrivateKeyError, RunTimeoutError

_ENV_NAME = re.compile(r"^[A-Za-z_][A-Za-z0-9_]*$")
_READ_CHUNK = 32768

# Preferred first: paramiko offers the first pinned key's type to the server first.
_TYPE_ORDER = {"ssh-ed25519": 0}


class HostKeyLike(Protocol):
    type: str
    key: str


@dataclass(frozen=True)
class RunResult:
    """What a command printed and how it ended.

    ``exit_code`` is -1 when the server reported no exit status, for example when the command was
    killed by a signal.
    """

    stdout: str
    stderr: str
    exit_code: int


def build_command(
    command: str | Sequence[str],
    cwd: str | None = None,
    env: Mapping[str, str] | None = None,
) -> str:
    """Return the string sent to the remote shell.

    A ``str`` command is run as written. A list is joined with each argument quoted, so no
    argument can start a second command. ``cwd`` and ``env`` values are quoted here. Without
    ``cwd`` or ``env`` the command is sent as it is.
    """
    if isinstance(command, str):
        text = command
        is_list = False
    else:
        args = list(command)
        if not args or not all(isinstance(a, str) for a in args):
            raise ValueError("command must be a string or a non-empty list of strings")
        text = " ".join(shlex.quote(a) for a in args)
        is_list = True
    if not text.strip():
        raise ValueError("command is empty")
    if "\x00" in text:
        raise ValueError("command contains a NUL byte")

    steps: list[str] = []
    if cwd is not None:
        if not isinstance(cwd, str) or not cwd or "\x00" in cwd:
            raise ValueError("cwd must be a non-empty string")
        steps.append(f"cd -- {shlex.quote(cwd)}")
    if env:
        assignments: list[str] = []
        for name, value in env.items():
            if not isinstance(name, str) or not _ENV_NAME.match(name):
                raise ValueError(f"invalid environment variable name: {name!r}")
            if not isinstance(value, str) or "\x00" in value:
                raise ValueError(f"the value of {name} must be a string without NUL bytes")
            assignments.append(f"{name}={shlex.quote(value)}")
        steps.append("export " + " ".join(assignments))
    if not steps:
        return text
    # eval keeps a string command's own `;`, `||` and `&&` from binding to the prefix.
    steps.append(text if is_list else f"eval {shlex.quote(text)}")
    return " && ".join(steps)


def load_private_key(private_key: str | bytes | paramiko.PKey, passphrase: str | None = None):
    """Return a paramiko key from an OpenSSH or PEM private key string, or pass a key through.

    Ed25519, ECDSA and RSA are supported. Errors never include key material.
    """
    if isinstance(private_key, paramiko.PKey):
        return private_key
    if isinstance(private_key, str):
        data = private_key.encode()
    elif isinstance(private_key, bytes | bytearray):
        data = bytes(private_key)
    else:
        raise TypeError("private_key must be a string, bytes or a paramiko.PKey")
    password = passphrase.encode() if passphrase else None
    try:
        try:
            loaded = serialization.load_ssh_private_key(data, password=password)
        except ValueError:
            loaded = serialization.load_pem_private_key(data, password=password)
    except TypeError:
        raise PrivateKeyError("The private key is encrypted: pass its passphrase") from None
    except Exception:
        raise PrivateKeyError(
            "Could not read the private key: wrong passphrase or not an OpenSSH or PEM key"
        ) from None
    if isinstance(loaded, rsa.RSAPrivateKey):
        key_class: Any = paramiko.RSAKey
    elif isinstance(loaded, ed25519.Ed25519PrivateKey):
        key_class = paramiko.Ed25519Key
    elif isinstance(loaded, ec.EllipticCurvePrivateKey):
        key_class = paramiko.ECDSAKey
    else:
        raise PrivateKeyError("Unsupported private key type: use Ed25519, ECDSA or RSA") from None
    try:
        return key_class.from_private_key(io.StringIO(data.decode()), password=passphrase)
    except Exception:
        raise PrivateKeyError("Could not read the private key") from None


def _parse_host_key(entry: HostKeyLike | str) -> tuple[str, paramiko.PKey]:
    if isinstance(entry, str):
        parts = entry.split()
        if len(parts) < 2:
            raise ValueError("host key line must be 'type base64'")
        key_type, blob = parts[0], parts[1]
    else:
        key_type, blob = entry.type, entry.key
    raw = base64.b64decode(blob, validate=True)
    return key_type, paramiko.PKey.from_type_string(key_type, raw)


def server_name(host: str, port: int) -> str:
    """The name paramiko looks host keys up under: ``host``, or ``[host]:port`` off port 22."""
    return host if port == 22 else f"[{host}]:{port}"


def load_host_keys(
    client: paramiko.SSHClient, host: str, port: int, host_keys: Sequence[HostKeyLike | str]
) -> int:
    """Pin the given host keys for ``host:port`` on ``client``; return how many were usable.

    Entries that do not parse are skipped. Raises ``HostKeyMismatchError`` when none are usable,
    so a client never connects with nothing to check against.
    """
    parsed: list[tuple[str, paramiko.PKey]] = []
    for entry in host_keys:
        try:
            parsed.append(_parse_host_key(entry))
        except Exception:
            continue
    if not parsed:
        raise HostKeyMismatchError(
            "No usable SSH host keys for this Cube, so the connection was not attempted. "
            "The API has none yet (the Cube may still be booting): retry shortly, "
            "or pass host_keys= yourself"
        )
    parsed.sort(key=lambda item: _TYPE_ORDER.get(item[0], 1))
    store = client.get_host_keys()
    name = server_name(host, port)
    for key_type, key in parsed:
        store.add(name, key_type, key)
    return len(parsed)


class _RejectUnknownHostKey(paramiko.RejectPolicy):
    """``RejectPolicy`` that reports the refusal as a ``HostKeyMismatchError``."""

    def missing_host_key(self, client: Any, hostname: str, key: paramiko.PKey) -> None:
        raise HostKeyMismatchError(
            f"The server at {hostname} presented a {key.get_name()} host key that is not one of "
            "this Cube's host keys. Refusing to connect"
        )


class CubeFiles:
    """``shell.files``: read and write files on the Cube over SFTP.

    Paths are sent to the SFTP server as written: no shell, no ``~`` expansion, and relative paths
    start in the login user's home directory.
    """

    def __init__(self, shell: CubeShell) -> None:
        self._shell = shell

    def write(self, path: str, data: str | bytes) -> None:
        """Create or replace a remote file. A ``str`` is written as UTF-8."""
        payload = data.encode() if isinstance(data, str) else bytes(data)
        self._shell._sftp().putfo(io.BytesIO(payload), path)

    def read(self, path: str) -> bytes:
        """Return the contents of a remote file."""
        buffer = io.BytesIO()
        self._shell._sftp().getfo(path, buffer)
        return buffer.getvalue()

    def upload(self, local_path: str | os.PathLike[str], remote_path: str) -> None:
        """Copy a local file to the Cube."""
        self._shell._sftp().put(os.fspath(local_path), remote_path)

    def download(self, remote_path: str, local_path: str | os.PathLike[str]) -> None:
        """Copy a file from the Cube to a local path."""
        self._shell._sftp().get(remote_path, os.fspath(local_path))


class CubeShell:
    """An open SSH connection to one Cube: ``run`` commands and use ``files``.

    Get one from ``client.cubes.connect(...)`` or ``cube.connect(...)``. Use it as a context
    manager, or call ``close()``. It holds no copy of your private key.
    """

    def __init__(self, ssh: paramiko.SSHClient, *, host: str, port: int, user: str) -> None:
        self._ssh = ssh
        self.host = host
        self.port = port
        self.user = user
        self.files = CubeFiles(self)
        self._sftp_client: paramiko.SFTPClient | None = None
        self._sftp_lock = threading.Lock()

    def __repr__(self) -> str:
        return f"CubeShell(user={self.user!r}, host={self.host!r}, port={self.port})"

    def _sftp(self) -> paramiko.SFTPClient:
        with self._sftp_lock:
            if self._sftp_client is None:
                self._sftp_client = self._ssh.open_sftp()
            return self._sftp_client

    def run(
        self,
        command: str | Sequence[str],
        cwd: str | None = None,
        env: Mapping[str, str] | None = None,
        timeout: float | None = None,
    ) -> RunResult:
        """Run a command on the Cube and wait for it to finish.

        A ``str`` is run by the remote shell as written. A list is one command: each item is
        quoted as one argument. ``cwd`` and ``env`` are quoted for you; env names must match
        ``[A-Za-z_][A-Za-z0-9_]*``. A non-zero exit code is returned, not raised. After
        ``timeout`` seconds the command is cut off and ``RunTimeoutError`` is raised.
        """
        remote = build_command(command, cwd=cwd, env=env)
        transport = self._ssh.get_transport()
        if transport is None or not transport.is_active():
            raise ConnectionError("The SSH connection is closed")
        deadline = None if timeout is None else time.monotonic() + timeout
        chan = transport.open_session(timeout=timeout)
        chan.exec_command(remote)
        try:
            # Commands that read stdin see end-of-file instead of waiting for input.
            chan.shutdown_write()
        except (paramiko.SSHException, OSError):
            pass  # a fast command can finish, and close the channel, before this runs

        out: list[bytes] = []
        err: list[bytes] = []
        readers = [
            threading.Thread(target=_drain, args=(chan.recv, out), daemon=True),
            threading.Thread(target=_drain, args=(chan.recv_stderr, err), daemon=True),
        ]
        for reader in readers:
            reader.start()

        def remaining() -> float | None:
            return None if deadline is None else max(deadline - time.monotonic(), 0.0)

        finished = True
        for reader in readers:
            reader.join(remaining())
            if reader.is_alive():
                finished = False
                break
        if finished:
            finished = chan.status_event.wait(remaining())
        if not finished:
            chan.close()
            raise RunTimeoutError(
                f"The command did not finish within {timeout:g}s",
                timeout=float(timeout or 0),
                stdout=_decode(out),
                stderr=_decode(err),
            )
        exit_code = chan.recv_exit_status()
        chan.close()
        return RunResult(stdout=_decode(out), stderr=_decode(err), exit_code=exit_code)

    def close(self) -> None:
        """Close the SFTP session and the SSH connection. Safe to call twice."""
        with self._sftp_lock:
            if self._sftp_client is not None:
                try:
                    self._sftp_client.close()
                finally:
                    self._sftp_client = None
        self._ssh.close()

    def __enter__(self) -> CubeShell:
        return self

    def __exit__(
        self,
        exc_type: type[BaseException] | None,
        exc: BaseException | None,
        tb: TracebackType | None,
    ) -> None:
        self.close()


def _drain(read: Any, sink: list[bytes]) -> None:
    while True:
        try:
            data = read(_READ_CHUNK)
        except Exception:
            return
        if not data:
            return
        sink.append(data)


def _decode(chunks: list[bytes]) -> str:
    return b"".join(chunks).decode("utf-8", errors="replace")


def open_shell(
    *,
    host: str,
    port: int,
    user: str,
    host_keys: Sequence[HostKeyLike | str],
    private_key: str | bytes | paramiko.PKey,
    passphrase: str | None = None,
    timeout: float = 30.0,
) -> CubeShell:
    """Connect to ``host:port`` as ``user``, checking the server against ``host_keys``.

    Order matters: the keys are loaded and the private key is read before any socket opens, so
    a bad key or an empty host key list fails without touching the network.
    """
    client = paramiko.SSHClient()
    try:
        load_host_keys(client, host, port, host_keys)
        pkey = load_private_key(private_key, passphrase)
        client.set_missing_host_key_policy(_RejectUnknownHostKey())
        try:
            client.connect(
                host,
                port=port,
                username=user,
                pkey=pkey,
                allow_agent=False,
                look_for_keys=False,
                timeout=timeout,
                banner_timeout=timeout,
                auth_timeout=timeout,
            )
        except paramiko.BadHostKeyException:
            raise HostKeyMismatchError(
                f"The host key of {server_name(host, port)} does not match any of this Cube's "
                "host keys. Refusing to connect"
            ) from None
    except BaseException:
        client.close()
        raise
    return CubeShell(client, host=host, port=port, user=user)
