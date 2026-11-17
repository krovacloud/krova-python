"""OpenAI Agents SDK tools for a Cube: ``krova_tools(shell)`` returns three ``FunctionTool``s.

Needs the ``openai-agents`` extra (see the README). Written against openai-agents 0.24.0.
The SDK runs tools on its event loop, so each call hands the blocking SSH work to a thread.
"""

from __future__ import annotations

import asyncio
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
    from agents import FunctionTool, function_tool
except ImportError as exc:  # pragma: no cover - exercised only without the extra
    raise missing_extra("openai-agents", "openai-agents") from exc

__all__ = ["krova_tools"]


def krova_tools(
    shell: Any, *, max_output_bytes: int = DEFAULT_MAX_OUTPUT_BYTES
) -> list[FunctionTool]:
    """Return ``krova_run``, ``krova_read_file`` and ``krova_write_file`` bound to ``shell``.

    ``shell`` is an open ``CubeShell`` from ``client.cubes.connect(...)``. Close it yourself when
    the agent is done. Pass the list as ``Agent(tools=...)``.
    """
    toolbox = CubeToolbox(shell, max_output_bytes=max_output_bytes)

    @function_tool(name_override="krova_run", description_override=RUN_DESCRIPTION)
    async def krova_run(command: str, cwd: str | None = None, timeout: float | None = None) -> str:
        """Run a shell command in a Cube.

        Args:
            command: The shell command to run.
            cwd: Working directory for the command.
            timeout: Seconds to wait before the command is stopped.
        """
        return await asyncio.to_thread(toolbox.run, command, cwd, timeout)

    @function_tool(name_override="krova_read_file", description_override=READ_FILE_DESCRIPTION)
    async def krova_read_file(path: str) -> str:
        """Read a text file from a Cube.

        Args:
            path: Path of the file to read.
        """
        return await asyncio.to_thread(toolbox.read_file, path)

    @function_tool(name_override="krova_write_file", description_override=WRITE_FILE_DESCRIPTION)
    async def krova_write_file(path: str, content: str) -> str:
        """Write a text file in a Cube.

        Args:
            path: Path of the file to create or replace.
            content: Text to write to the file.
        """
        return await asyncio.to_thread(toolbox.write_file, path, content)

    return [krova_run, krova_read_file, krova_write_file]
