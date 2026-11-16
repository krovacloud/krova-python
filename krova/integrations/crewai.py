"""CrewAI tools for a Cube: ``krova_tools(shell)`` returns three ``BaseTool`` instances.

Needs the ``crewai`` extra (see the README). Written against crewai 1.15.39.
"""

from __future__ import annotations

from typing import Any

from ._core import (
    DEFAULT_MAX_OUTPUT_BYTES,
    READ_FILE_DESCRIPTION,
    RUN_DESCRIPTION,
    WRITE_FILE_DESCRIPTION,
    CubeToolbox,
    missing_extra,
)

try:
    from crewai.tools import BaseTool
    from pydantic import BaseModel, Field
except ImportError as exc:  # pragma: no cover - exercised only without the extra
    raise missing_extra("crewai", "crewai") from exc

__all__ = ["KrovaReadFileTool", "KrovaRunTool", "KrovaWriteFileTool", "krova_tools"]


class RunInput(BaseModel):
    command: str = Field(description="The shell command to run.")
    cwd: str | None = Field(default=None, description="Working directory for the command.")
    timeout: float | None = Field(
        default=None, description="Seconds to wait before the command is stopped."
    )


class ReadFileInput(BaseModel):
    path: str = Field(description="Path of the file to read.")


class WriteFileInput(BaseModel):
    path: str = Field(description="Path of the file to create or replace.")
    content: str = Field(description="Text to write to the file.")


class KrovaRunTool(BaseTool):
    name: str = "krova_run"
    description: str = RUN_DESCRIPTION
    args_schema: type[BaseModel] = RunInput
    toolbox: Any

    def _run(self, command: str, cwd: str | None = None, timeout: float | None = None) -> str:
        return self.toolbox.run(command, cwd=cwd, timeout=timeout)


class KrovaReadFileTool(BaseTool):
    name: str = "krova_read_file"
    description: str = READ_FILE_DESCRIPTION
    args_schema: type[BaseModel] = ReadFileInput
    toolbox: Any

    def _run(self, path: str) -> str:
        return self.toolbox.read_file(path)


class KrovaWriteFileTool(BaseTool):
    name: str = "krova_write_file"
    description: str = WRITE_FILE_DESCRIPTION
    args_schema: type[BaseModel] = WriteFileInput
    toolbox: Any

    def _run(self, path: str, content: str) -> str:
        return self.toolbox.write_file(path, content)


def krova_tools(shell: Any, *, max_output_bytes: int = DEFAULT_MAX_OUTPUT_BYTES) -> list[BaseTool]:
    """Return ``krova_run``, ``krova_read_file`` and ``krova_write_file`` bound to ``shell``.

    ``shell`` is an open ``CubeShell`` from ``client.cubes.connect(...)``. Close it yourself when
    the agent is done.
    """
    toolbox = CubeToolbox(shell, max_output_bytes=max_output_bytes)
    return [
        KrovaRunTool(toolbox=toolbox),
        KrovaReadFileTool(toolbox=toolbox),
        KrovaWriteFileTool(toolbox=toolbox),
    ]
