"""Framework-neutral tool logic shared by the LangChain, CrewAI and OpenAI Agents adapters.

``CubeToolbox`` wraps one open ``CubeShell`` and turns its ``run`` and ``files`` calls into three
plain functions that take strings and return strings, which is what an LLM tool call needs. A
failed call comes back as text starting with ``Error:`` so the model can read it and try again;
nothing here raises for a bad command, a missing file or a timeout.
"""

from __future__ import annotations

from typing import Any

from ..errors import RunTimeoutError

DEFAULT_MAX_OUTPUT_BYTES = 32 * 1024

RUN_DESCRIPTION = (
    "Run a shell command in a Krova Cube, a CPU-only Linux VM, over SSH. Returns the exit code, "
    "stdout and stderr. Each stream is cut at a size limit, and the result says when it was. "
    "Set cwd to choose the working directory and timeout (seconds) to stop a long command."
)
READ_FILE_DESCRIPTION = (
    "Read a text file from a Krova Cube, a CPU-only Linux VM. The path is used as written: "
    "no ~ expansion, and a relative path starts in the login user's home directory. "
    "A long file is cut at a size limit, and the result says when it was."
)
WRITE_FILE_DESCRIPTION = (
    "Create or replace a text file in a Krova Cube, a CPU-only Linux VM. The path is used as "
    "written: no ~ expansion, and a relative path starts in the login user's home directory. "
    "The parent directory must already exist."
)


def truncate(text: str, limit: int) -> str:
    """Cut ``text`` to ``limit`` UTF-8 bytes and append a note saying how much was dropped."""
    raw = text.encode("utf-8")
    if len(raw) <= limit:
        return text
    kept = raw[:limit].decode("utf-8", errors="ignore")
    return f"{kept}\n[truncated: {len(raw) - limit} more bytes not shown]"


class CubeToolbox:
    """Three tools bound to one ``CubeShell``: run a command, read a file, write a file.

    ``shell`` is anything with ``run(command, cwd=, timeout=)`` and ``files.read/write``, which
    is what ``CubeShell`` offers. ``max_output_bytes`` caps stdout, stderr and a file read, each
    on its own.
    """

    def __init__(self, shell: Any, *, max_output_bytes: int = DEFAULT_MAX_OUTPUT_BYTES) -> None:
        if max_output_bytes < 1:
            raise ValueError("max_output_bytes must be at least 1")
        self.shell = shell
        self.max_output_bytes = max_output_bytes

    def _format(self, exit_code: int | str, stdout: str, stderr: str) -> str:
        limit = self.max_output_bytes
        return (
            f"exit_code: {exit_code}\n"
            f"stdout:\n{truncate(stdout, limit)}\n"
            f"stderr:\n{truncate(stderr, limit)}"
        )

    def run(self, command: str, cwd: str | None = None, timeout: float | None = None) -> str:
        try:
            result = self.shell.run(command, cwd=cwd, timeout=timeout)
        except RunTimeoutError as exc:
            return "Error: the command timed out and was stopped.\n" + self._format(
                "none", exc.stdout, exc.stderr
            )
        except Exception as exc:
            return f"Error: could not run the command: {exc}"
        return self._format(result.exit_code, result.stdout, result.stderr)

    def read_file(self, path: str) -> str:
        try:
            data = self.shell.files.read(path)
        except Exception as exc:
            return f"Error: could not read {path}: {exc}"
        return truncate(data.decode("utf-8", errors="replace"), self.max_output_bytes)

    def write_file(self, path: str, content: str) -> str:
        try:
            self.shell.files.write(path, content)
        except Exception as exc:
            return f"Error: could not write {path}: {exc}"
        return f"Wrote {len(content.encode('utf-8'))} bytes to {path}"


def missing_extra(package: str, extra: str) -> ImportError:
    """The error a framework module raises when its framework is not installed."""
    return ImportError(
        f"This adapter needs the {package} package. Install the {extra} extra from a release tag: "
        f'pip install "krova[{extra}] @ git+https://github.com/krovacloud/krova-python@vX.Y.Z"'
    )
