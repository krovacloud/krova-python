from __future__ import annotations

import pytest

from krova import RunResult, RunTimeoutError


class FakeFiles:
    def __init__(self) -> None:
        self.store: dict[str, bytes] = {}

    def write(self, path: str, data: str | bytes) -> None:
        if path.startswith("/nope/"):
            raise FileNotFoundError(2, "No such file")
        self.store[path] = data.encode() if isinstance(data, str) else bytes(data)

    def read(self, path: str) -> bytes:
        if path not in self.store:
            raise FileNotFoundError(2, "No such file")
        return self.store[path]


class FakeShell:
    """Stands in for ``CubeShell``: no network, canned results, records every call."""

    def __init__(self) -> None:
        self.files = FakeFiles()
        self.calls: list[tuple[str, str | None, float | None]] = []
        self.result = RunResult(stdout="hello\n", stderr="warn\n", exit_code=3)
        self.raises: Exception | None = None

    def run(self, command, cwd=None, env=None, timeout=None) -> RunResult:
        self.calls.append((command, cwd, timeout))
        if self.raises is not None:
            raise self.raises
        return self.result


@pytest.fixture
def fake_shell() -> FakeShell:
    return FakeShell()


@pytest.fixture
def timeout_error() -> RunTimeoutError:
    return RunTimeoutError(
        "did not finish", timeout=2.0, stdout="partial out", stderr="partial err"
    )
