from __future__ import annotations

import asyncio
import json

import pytest

pytest.importorskip("agents")

from agents.tool_context import ToolContext  # noqa: E402

from krova.integrations.openai_agents import krova_tools  # noqa: E402


def by_name(tools):
    return {tool.name: tool for tool in tools}


def call(tool, **arguments):
    raw = json.dumps(arguments)
    ctx = ToolContext(None, tool_name=tool.name, tool_call_id="call_1", tool_arguments=raw)
    return asyncio.run(tool.on_invoke_tool(ctx, raw))


def test_names_and_descriptions(fake_shell):
    tools = krova_tools(fake_shell)
    assert [t.name for t in tools] == ["krova_run", "krova_read_file", "krova_write_file"]
    for tool in tools:
        assert "Krova Cube" in tool.description and "CPU-only" in tool.description


def test_schemas(fake_shell):
    tools = by_name(krova_tools(fake_shell))
    assert set(tools["krova_run"].params_json_schema["properties"]) == {"command", "cwd", "timeout"}
    assert "command" in tools["krova_run"].params_json_schema["required"]
    assert set(tools["krova_read_file"].params_json_schema["properties"]) == {"path"}
    assert set(tools["krova_write_file"].params_json_schema["properties"]) == {"path", "content"}


def test_run_returns_exit_code_stdout_stderr(fake_shell):
    out = call(by_name(krova_tools(fake_shell))["krova_run"], command="ls", cwd="/srv", timeout=4)
    assert out == "exit_code: 3\nstdout:\nhello\n\nstderr:\nwarn\n"
    assert fake_shell.calls == [("ls", "/srv", 4)]


def test_optional_arguments_may_be_null(fake_shell):
    out = call(by_name(krova_tools(fake_shell))["krova_run"], command="ls", cwd=None, timeout=None)
    assert out.startswith("exit_code: 3")
    assert fake_shell.calls == [("ls", None, None)]


def test_write_then_read(fake_shell):
    tools = by_name(krova_tools(fake_shell))
    assert call(tools["krova_write_file"], path="/a", content="hi") == "Wrote 2 bytes to /a"
    assert call(tools["krova_read_file"], path="/a") == "hi"


def test_truncation_is_configurable(fake_shell):
    fake_shell.result = type(fake_shell.result)(stdout="x" * 50, stderr="", exit_code=0)
    tool = by_name(krova_tools(fake_shell, max_output_bytes=10))["krova_run"]
    assert "[truncated: 40 more bytes not shown]" in call(tool, command="c")
