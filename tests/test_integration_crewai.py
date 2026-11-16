from __future__ import annotations

import pytest

pytest.importorskip("crewai")

from krova.integrations.crewai import krova_tools  # noqa: E402


def by_name(tools):
    return {tool.name: tool for tool in tools}


def test_names_and_descriptions(fake_shell):
    tools = krova_tools(fake_shell)
    assert [t.name for t in tools] == ["krova_run", "krova_read_file", "krova_write_file"]
    for tool in tools:
        assert "Krova Cube" in tool.description and "CPU-only" in tool.description


def test_schemas(fake_shell):
    tools = by_name(krova_tools(fake_shell))
    assert set(tools["krova_run"].args_schema.model_fields) == {"command", "cwd", "timeout"}
    assert tools["krova_run"].args_schema.model_json_schema()["required"] == ["command"]
    assert set(tools["krova_read_file"].args_schema.model_fields) == {"path"}
    assert set(tools["krova_write_file"].args_schema.model_fields) == {"path", "content"}


def test_run_returns_exit_code_stdout_stderr(fake_shell):
    out = by_name(krova_tools(fake_shell))["krova_run"].run(command="ls", cwd="/srv", timeout=4)
    assert out == "exit_code: 3\nstdout:\nhello\n\nstderr:\nwarn\n"
    assert fake_shell.calls == [("ls", "/srv", 4)]


def test_write_then_read(fake_shell):
    tools = by_name(krova_tools(fake_shell))
    assert tools["krova_write_file"].run(path="/a", content="hi") == "Wrote 2 bytes to /a"
    assert tools["krova_read_file"].run(path="/a") == "hi"


def test_truncation_is_configurable(fake_shell):
    fake_shell.result = type(fake_shell.result)(stdout="x" * 50, stderr="", exit_code=0)
    out = by_name(krova_tools(fake_shell, max_output_bytes=10))["krova_run"].run(command="c")
    assert "[truncated: 40 more bytes not shown]" in out
