from __future__ import annotations

import io
import socket
import threading
from types import SimpleNamespace

import httpx
import paramiko
import pytest
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import ec, ed25519, rsa

import krova.shell as shell_module
from krova import (
    CubeShell,
    HostKey,
    HostKeyMismatchError,
    Krova,
    KrovaError,
    PrivateKeyError,
    RunTimeoutError,
)
from krova.shell import build_command, load_host_keys, load_private_key, server_name

# ---------------------------------------------------------------- keys made at test time


def private_pem(key, password: bytes | None = None, openssh: bool = True) -> str:
    encryption = (
        serialization.BestAvailableEncryption(password)
        if password
        else serialization.NoEncryption()
    )
    return key.private_bytes(
        serialization.Encoding.PEM,
        serialization.PrivateFormat.OpenSSH
        if openssh
        else serialization.PrivateFormat.TraditionalOpenSSL,
        encryption,
    ).decode()


def ed25519_pair() -> tuple[str, paramiko.PKey]:
    text = private_pem(ed25519.Ed25519PrivateKey.generate())
    return text, paramiko.Ed25519Key.from_private_key(io.StringIO(text))


def ecdsa_pair() -> tuple[str, paramiko.PKey]:
    text = private_pem(ec.generate_private_key(ec.SECP256R1()))
    return text, paramiko.ECDSAKey.from_private_key(io.StringIO(text))


def host_key_of(key: paramiko.PKey) -> HostKey:
    return HostKey(type=key.get_name(), key=key.get_base64())


# ---------------------------------------------------------------- quoting and env


def test_string_command_is_sent_as_written():
    assert build_command("echo $HOME | wc -c") == "echo $HOME | wc -c"


def test_list_command_quotes_every_argument():
    out = build_command(["echo", "a b", "x; rm -rf /", "$(id)", "it's"])
    assert out == "echo 'a b' 'x; rm -rf /' '$(id)' 'it'\"'\"'s'"


def test_cwd_and_env_are_quoted():
    out = build_command(["ls"], cwd="/tmp/my dir; id", env={"A": "x y", "B_1": "$(id)"})
    assert out == "cd -- '/tmp/my dir; id' && export A='x y' B_1='$(id)' && ls"


def test_string_command_with_prefix_cannot_escape_the_prefix():
    out = build_command("false || echo no", cwd="/srv")
    assert out == "cd -- /srv && eval 'false || echo no'"


@pytest.mark.parametrize("name", ["", "1A", "A-B", "A B", "A=1", "A;id", "É"])
def test_env_names_are_validated(name):
    with pytest.raises(ValueError):
        build_command("true", env={name: "x"})


@pytest.mark.parametrize("bad", ["", "  ", [], [""] * 0, ["ok", 3], "a\x00b"])
def test_bad_commands_are_refused(bad):
    with pytest.raises(ValueError):
        build_command(bad)


def test_env_value_must_be_a_string_without_nul():
    with pytest.raises(ValueError):
        build_command("true", env={"A": "a\x00b"})
    with pytest.raises(ValueError):
        build_command("true", env={"A": 1})  # type: ignore[dict-item]


# ---------------------------------------------------------------- private keys


@pytest.mark.parametrize(
    ("key", "klass"),
    [
        (ed25519.Ed25519PrivateKey.generate(), paramiko.Ed25519Key),
        (ec.generate_private_key(ec.SECP256R1()), paramiko.ECDSAKey),
        (rsa.generate_private_key(65537, 2048), paramiko.RSAKey),
    ],
)
def test_private_key_strings_load_for_each_type(key, klass):
    assert isinstance(load_private_key(private_pem(key)), klass)


def test_rsa_pem_format_loads():
    key = rsa.generate_private_key(65537, 2048)
    assert isinstance(load_private_key(private_pem(key, openssh=False)), paramiko.RSAKey)


def test_passphrase_protected_key():
    key = ed25519.Ed25519PrivateKey.generate()
    text = private_pem(key, b"correct horse")
    assert isinstance(load_private_key(text, "correct horse"), paramiko.Ed25519Key)
    with pytest.raises(PrivateKeyError, match="passphrase"):
        load_private_key(text)
    with pytest.raises(PrivateKeyError):
        load_private_key(text, "wrong")


def test_pkey_passes_through():
    _, pkey = ed25519_pair()
    assert load_private_key(pkey) is pkey


def test_key_errors_never_contain_key_material():
    text, _ = ed25519_pair()
    body = text.splitlines()[1]
    broken = text.replace(body, body[:-6] + "AAAAAA")
    with pytest.raises(PrivateKeyError) as caught:
        load_private_key(broken)
    assert body[:20] not in str(caught.value) and body[:20] not in repr(caught.value)
    assert caught.value.__cause__ is None and caught.value.__suppress_context__
    with pytest.raises(PrivateKeyError):
        load_private_key("not a key")


# ---------------------------------------------------------------- host key loading


def test_host_keys_are_stored_under_the_port_aware_name():
    _, pkey = ed25519_pair()
    client = paramiko.SSHClient()
    assert load_host_keys(client, "cube.example", 2201, [host_key_of(pkey)]) == 1
    assert client.get_host_keys().check("[cube.example]:2201", pkey)
    assert not client.get_host_keys().check("cube.example", pkey)

    other = paramiko.SSHClient()
    load_host_keys(other, "cube.example", 22, [f"{pkey.get_name()} {pkey.get_base64()}"])
    assert other.get_host_keys().check("cube.example", pkey)
    assert server_name("h", 22) == "h" and server_name("h", 2222) == "[h]:2222"


def test_every_host_key_type_is_loaded():
    _, ed = ed25519_pair()
    _, ecd = ecdsa_pair()
    client = paramiko.SSHClient()
    assert load_host_keys(client, "h", 2200, [host_key_of(ecd), host_key_of(ed)]) == 2
    stored = client.get_host_keys().lookup("[h]:2200")
    assert set(stored.keys()) == {ed.get_name(), ecd.get_name()}
    assert stored.keys()[0] == "ssh-ed25519"


@pytest.mark.parametrize("keys", [[], [HostKey(type="ssh-ed25519", key="!!not base64")], ["x"]])
def test_no_usable_host_keys_is_refused(keys):
    with pytest.raises(HostKeyMismatchError):
        load_host_keys(paramiko.SSHClient(), "h", 22, keys)


def test_open_shell_refuses_empty_host_keys_before_touching_the_network(monkeypatch):
    def boom(*a, **k):
        raise AssertionError("must not connect")

    monkeypatch.setattr(paramiko.SSHClient, "connect", boom)
    text, _ = ed25519_pair()
    with pytest.raises(HostKeyMismatchError):
        shell_module.open_shell(host="h", port=22, user="root", host_keys=[], private_key=text)


def test_open_shell_sets_reject_policy_and_disables_agent(monkeypatch):
    seen: dict = {}

    def fake_connect(self, hostname, **kwargs):
        seen["policy"] = self._policy
        seen["kwargs"] = kwargs

    monkeypatch.setattr(paramiko.SSHClient, "connect", fake_connect)
    text, _ = ed25519_pair()
    _, host = ed25519_pair()
    opened = shell_module.open_shell(
        host="h", port=2200, user="root", host_keys=[host_key_of(host)], private_key=text, timeout=5
    )
    assert isinstance(seen["policy"], paramiko.RejectPolicy)
    assert not isinstance(seen["policy"], paramiko.AutoAddPolicy)
    assert seen["kwargs"]["allow_agent"] is False and seen["kwargs"]["look_for_keys"] is False
    assert seen["kwargs"]["timeout"] == 5 and seen["kwargs"]["port"] == 2200
    assert text not in repr(opened) and "BEGIN" not in repr(opened)


# ---------------------------------------------------------------- a real SSH server on loopback


class _Server(paramiko.ServerInterface):
    def __init__(self, client_key: paramiko.PKey) -> None:
        self.client_key = client_key
        self.commands: list[str] = []

    def get_allowed_auths(self, username):
        return "publickey"

    def check_auth_publickey(self, username, key):
        ok = key.asbytes() == self.client_key.asbytes()
        return paramiko.AUTH_SUCCESSFUL if ok else paramiko.AUTH_FAILED

    def check_channel_request(self, kind, chanid):
        if kind == "session":
            return paramiko.OPEN_SUCCEEDED
        return paramiko.OPEN_FAILED_ADMINISTRATIVELY_PROHIBITED

    def check_channel_exec_request(self, channel, command):
        text = command.decode()
        self.commands.append(text)

        def respond():
            if text == "hang":
                threading.Event().wait(30)
                return
            channel.sendall(b"out:" + command)
            channel.sendall_stderr(b"err:warn")
            channel.send_exit_status(7)
            channel.shutdown_write()

        threading.Thread(target=respond, daemon=True).start()
        return True


class LoopbackServer:
    def __init__(self, host_key: paramiko.PKey, client_key: paramiko.PKey) -> None:
        self.sock = socket.socket()
        self.sock.bind(("127.0.0.1", 0))
        self.sock.listen(4)
        self.port = self.sock.getsockname()[1]
        self.server = _Server(client_key)
        self.host_key = host_key
        self.transports: list[paramiko.Transport] = []
        threading.Thread(target=self._serve, daemon=True).start()

    def _serve(self):
        while True:
            try:
                conn, _ = self.sock.accept()
            except OSError:
                return
            transport = paramiko.Transport(conn)
            transport.add_server_key(self.host_key)
            self.transports.append(transport)
            try:
                transport.start_server(server=self.server)
            except Exception:
                continue
            threading.Thread(target=self._accept_channels, args=(transport,), daemon=True).start()

    @staticmethod
    def _accept_channels(transport):
        kept = []  # a Channel closes itself when garbage collected
        while transport.is_active():
            channel = transport.accept(1)
            if channel is not None:
                kept.append(channel)

    def close(self):
        self.sock.close()
        for transport in self.transports:
            transport.close()


@pytest.fixture
def loopback():
    client_text, client_key = ed25519_pair()
    _, host_key = ed25519_pair()
    server = LoopbackServer(host_key, client_key)
    yield SimpleNamespace(server=server, client_text=client_text, host_key=host_key)
    server.close()


def connect(loopback, host_keys, **kwargs) -> CubeShell:
    return shell_module.open_shell(
        host="127.0.0.1",
        port=loopback.server.port,
        user="root",
        host_keys=host_keys,
        private_key=loopback.client_text,
        timeout=10,
        **kwargs,
    )


def test_connects_runs_and_closes_when_the_host_key_matches(loopback):
    with connect(loopback, [host_key_of(loopback.host_key)]) as sh:
        result = sh.run(["echo", "hi there"], cwd="/tmp", env={"A": "1"})
        assert result.exit_code == 7
        assert result.stdout == "out:cd -- /tmp && export A=1 && echo 'hi there'"
        assert result.stderr == "err:warn"
    assert loopback.server.server.commands == ["cd -- /tmp && export A=1 && echo 'hi there'"]


def test_run_timeout_raises_and_keeps_the_connection_usable(loopback):
    with connect(loopback, [host_key_of(loopback.host_key)]) as sh:
        with pytest.raises(RunTimeoutError) as caught:
            sh.run("hang", timeout=0.5)
        assert caught.value.timeout == 0.5
        assert sh.run("after").exit_code == 7


def test_a_different_host_key_is_refused(loopback):
    _, impostor = ed25519_pair()
    with pytest.raises(HostKeyMismatchError):
        connect(loopback, [host_key_of(impostor)])
    assert loopback.server.server.commands == []


def test_a_server_key_of_an_unpinned_type_is_refused(loopback):
    _, ecdsa = ecdsa_pair()
    with pytest.raises(HostKeyMismatchError):
        connect(loopback, [host_key_of(ecdsa)])


def test_a_key_the_server_does_not_accept_fails_to_authenticate(loopback):
    other_text, _ = ed25519_pair()
    loopback.client_text = other_text
    with pytest.raises(paramiko.AuthenticationException):
        connect(loopback, [host_key_of(loopback.host_key)])


def test_cubes_connect_reads_host_keys_from_the_api(loopback):
    ssh_body = {
        "host": "127.0.0.1",
        "port": loopback.server.port,
        "user": "root",
        "hostKeys": [
            {"type": loopback.host_key.get_name(), "key": loopback.host_key.get_base64()}
        ],
    }
    client = Krova(
        api_key="kro_test",
        space_id="spc_1",
        transport=httpx.MockTransport(lambda request: httpx.Response(200, json=ssh_body)),
    )
    with client.cubes.connect("cub_1", private_key=loopback.client_text, timeout=10) as sh:
        assert sh.run("x").stdout == "out:x"

    ssh_body["hostKeys"] = []
    with pytest.raises(HostKeyMismatchError):
        client.cubes.connect("cub_1", private_key=loopback.client_text, timeout=10)

    # An override replaces the API's keys, and a wrong one is still refused.
    _, impostor = ed25519_pair()
    with pytest.raises(HostKeyMismatchError):
        client.cubes.connect(
            "cub_1",
            private_key=loopback.client_text,
            timeout=10,
            host_keys=[host_key_of(impostor)],
        )


def test_connect_without_a_host_raises(loopback):
    body = {"host": None, "port": 22, "user": "root", "hostKeys": []}
    client = Krova(
        api_key="kro_test",
        space_id="spc_1",
        transport=httpx.MockTransport(lambda request: httpx.Response(200, json=body)),
    )
    with pytest.raises(KrovaError, match="no SSH address"):
        client.cubes.connect("cub_1", private_key=loopback.client_text)


# ---------------------------------------------------------------- run() with a mocked channel


class FakeChannel:
    def __init__(self, out=(b"",), err=(b"",), status=0, set_status=True, block=False):
        self._out, self._err = list(out), list(err)
        self.status = status
        self.status_event = threading.Event()
        self._block = threading.Event()
        self.closed = False
        self.command = None
        self.write_shut = False
        if set_status:
            self.status_event.set()
        self.block = block

    def exec_command(self, command):
        self.command = command

    def shutdown_write(self):
        self.write_shut = True

    def _next(self, queue):
        if self.block:
            self._block.wait(30)
            return b""
        return queue.pop(0) if queue else b""

    def recv(self, n):
        return self._next(self._out)

    def recv_stderr(self, n):
        return self._next(self._err)

    def recv_exit_status(self):
        return self.status

    def close(self):
        self.closed = True
        self._block.set()


def fake_shell(channel: FakeChannel) -> CubeShell:
    transport = SimpleNamespace(is_active=lambda: True, open_session=lambda timeout=None: channel)
    ssh = SimpleNamespace(get_transport=lambda: transport, close=lambda: None)
    return CubeShell(ssh, host="h", port=22, user="root")  # type: ignore[arg-type]


def test_run_returns_output_and_exit_code():
    channel = FakeChannel(out=[b"he", b"llo \xff", b""], err=[b"oops", b""], status=3)
    result = fake_shell(channel).run("do it")
    assert (result.stdout, result.stderr, result.exit_code) == ("hello �", "oops", 3)
    assert channel.command == "do it" and channel.write_shut and channel.closed


def test_run_does_not_raise_on_a_non_zero_exit():
    assert fake_shell(FakeChannel(status=127)).run("nope").exit_code == 127


def test_run_times_out_and_closes_the_channel():
    channel = FakeChannel(block=True, set_status=False)
    with pytest.raises(RunTimeoutError, match="0.2s") as caught:
        fake_shell(channel).run("sleepy", timeout=0.2)
    assert caught.value.timeout == 0.2
    assert channel.closed


def test_run_times_out_when_the_exit_status_never_arrives():
    channel = FakeChannel(set_status=False)
    with pytest.raises(RunTimeoutError):
        fake_shell(channel).run("x", timeout=0.2)
    assert channel.closed


def test_run_on_a_closed_connection_raises():
    ssh = SimpleNamespace(get_transport=lambda: None, close=lambda: None)
    with pytest.raises(ConnectionError):
        CubeShell(ssh, host="h", port=22, user="root").run("x")  # type: ignore[arg-type]


# ---------------------------------------------------------------- files over SFTP


class FakeSftp:
    def __init__(self):
        self.calls: list[tuple] = []
        self.store: dict[str, bytes] = {}
        self.closed = False

    def putfo(self, fl, path):
        self.store[path] = fl.read()
        self.calls.append(("putfo", path))

    def getfo(self, path, fl):
        fl.write(self.store[path])

    def put(self, local, remote):
        self.calls.append(("put", local, remote))

    def get(self, remote, local):
        self.calls.append(("get", remote, local))

    def close(self):
        self.closed = True


def sftp_shell() -> tuple[CubeShell, FakeSftp, list]:
    sftp = FakeSftp()
    opened: list = []

    def open_sftp():
        opened.append(1)
        return sftp

    ssh = SimpleNamespace(open_sftp=open_sftp, close=lambda: None)
    return CubeShell(ssh, host="h", port=22, user="root"), sftp, opened  # type: ignore[arg-type]


def test_files_write_read_round_trip_and_utf8(tmp_path):
    sh, sftp, opened = sftp_shell()
    sh.files.write("/a.txt", "héllo")
    sh.files.write("/b.bin", b"\x00\x01")
    assert sh.files.read("/a.txt") == "héllo".encode()
    assert sh.files.read("/b.bin") == b"\x00\x01"
    assert len(opened) == 1


def test_files_upload_and_download_pass_paths_through(tmp_path):
    sh, sftp, _ = sftp_shell()
    sh.files.upload(tmp_path / "up.txt", "remote.txt")
    sh.files.download("remote.txt", tmp_path / "down.txt")
    assert sftp.calls == [
        ("put", str(tmp_path / "up.txt"), "remote.txt"),
        ("get", "remote.txt", str(tmp_path / "down.txt")),
    ]


def test_close_closes_sftp_and_is_idempotent():
    sh, sftp, _ = sftp_shell()
    sh.files.write("/a", "x")
    sh.close()
    sh.close()
    assert sftp.closed
