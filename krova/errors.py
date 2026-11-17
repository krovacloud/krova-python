"""Exceptions raised by the Krova SDK."""

from __future__ import annotations

from typing import Any

import httpx


class KrovaError(Exception):
    """An API call failed, or the SDK gave up waiting.

    ``status`` is the HTTP status code, or ``None`` for errors raised by the SDK itself
    (a wait that timed out). ``code`` is a machine-readable error code when the API sends one,
    for example ``termination_protected``. ``request_id`` is the ``X-Request-Id`` response
    header; quote it when you contact support.
    """

    def __init__(
        self,
        message: str,
        *,
        status: int | None = None,
        code: str | None = None,
        request_id: str | None = None,
        body: Any = None,
    ) -> None:
        super().__init__(message)
        self.message = message
        self.status = status
        self.code = code
        self.request_id = request_id
        self.body = body

    def __str__(self) -> str:
        parts = [self.message]
        if self.status is not None:
            parts.append(f"status={self.status}")
        if self.code:
            parts.append(f"code={self.code}")
        if self.request_id:
            parts.append(f"request_id={self.request_id}")
        return " ".join(parts) if len(parts) == 1 else f"{parts[0]} ({', '.join(parts[1:])})"


class CubeFailedError(KrovaError):
    """A Cube reached a state it cannot leave on its own while you were waiting for it to run."""

    def __init__(self, message: str, *, cube_id: str, state: str) -> None:
        super().__init__(message)
        self.cube_id = cube_id
        self.state = state


class WaitTimeoutError(KrovaError):
    """``wait_until_running`` ran out of time before the Cube reached ``running``."""

    def __init__(self, message: str, *, cube_id: str, state: str) -> None:
        super().__init__(message)
        self.cube_id = cube_id
        self.state = state


class HostKeyMismatchError(KrovaError):
    """The SSH host key check failed, so the SDK did not connect or dropped the connection.

    Raised when the API has no host keys for the Cube yet, when none of the keys given are usable,
    and when the server presents a key that is not one of them. Connecting is never allowed
    without this check.
    """


class PrivateKeyError(KrovaError):
    """The private key could not be read: wrong or missing passphrase, or an unsupported format.

    The message never contains any part of the key.
    """


class RunTimeoutError(KrovaError):
    """A command passed to ``shell.run`` did not finish within its ``timeout``.

    The command's channel is closed. ``stdout`` and ``stderr`` hold what it printed before then.
    """

    def __init__(self, message: str, *, timeout: float, stdout: str = "", stderr: str = "") -> None:
        super().__init__(message)
        self.timeout = timeout
        self.stdout = stdout
        self.stderr = stderr


def error_from_response(response: httpx.Response) -> KrovaError:
    """Build a ``KrovaError`` from a non-2xx response.

    The API sends ``{"error": "text"}``; a few endpoints send ``{"error": {"code", "message"}}``.
    Anything else (an empty or non-JSON body) falls back to the HTTP reason phrase.
    """
    body: Any
    try:
        body = response.json()
    except ValueError:
        body = None

    message: str | None = None
    code: str | None = None
    if isinstance(body, dict):
        error = body.get("error")
        if isinstance(error, str):
            message = error
        elif isinstance(error, dict):
            raw_message = error.get("message")
            raw_code = error.get("code")
            message = raw_message if isinstance(raw_message, str) else None
            code = raw_code if isinstance(raw_code, str) else None

    code = response.headers.get("x-error-code") or code
    return KrovaError(
        message or response.reason_phrase or f"Request failed with status {response.status_code}",
        status=response.status_code,
        code=code,
        request_id=response.headers.get("x-request-id"),
        body=body,
    )
