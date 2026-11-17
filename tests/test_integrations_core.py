from __future__ import annotations

import pytest

from krova.integrations._core import CubeToolbox, truncate


def test_run_reports_exit_code_stdout_and_stderr(fake_shell):
    out = CubeToolbox(fake_shell).run("echo hello", cwd="/srv", timeout=5)
    assert out == "exit_code: 3\nstdout:\nhello\n\nstderr:\nwarn\n"
    assert fake_shell.calls == [("echo hello", "/srv", 5)]


def test_run_truncates_each_stream_and_says_so(fake_shell):
    fake_shell.result = type(fake_shell.result)(stdout="a" * 100, stderr="b" * 10, exit_code=0)
    out = CubeToolbox(fake_shell, max_output_bytes=40).run("x")
    assert "a" * 40 + "\n[truncated: 60 more bytes not shown]" in out
    assert "b" * 10 in out
    assert out.count("[truncated") == 1


def test_default_limit_is_32_kb(fake_shell):
    fake_shell.result = type(fake_shell.result)(
        stdout="a" * (32 * 1024 + 5), stderr="", exit_code=0
    )
    assert "[truncated: 5 more bytes not shown]" in CubeToolbox(fake_shell).run("x")


def test_truncate_never_splits_a_character():
    text = "é" * 10  # 2 bytes each
    cut = truncate(text, 5)
    assert cut.startswith("éé\n[truncated: 15 more bytes not shown]")


def test_run_timeout_returns_partial_output(fake_shell, timeout_error):
    fake_shell.raises = timeout_error
    out = CubeToolbox(fake_shell).run("sleep 9", timeout=2)
    assert out.startswith("Error: the command timed out")
    assert "partial out" in out and "partial err" in out


def test_run_connection_error_comes_back_as_text(fake_shell):
    fake_shell.raises = ConnectionError("The SSH connection is closed")
    out = CubeToolbox(fake_shell).run("ls")
    assert out == "Error: could not run the command: The SSH connection is closed"


def test_write_then_read_round_trip(fake_shell):
    box = CubeToolbox(fake_shell)
    assert box.write_file("/tmp/a.txt", "héllo") == "Wrote 6 bytes to /tmp/a.txt"
    assert box.read_file("/tmp/a.txt") == "héllo"


def test_read_truncates_and_reports_missing_file(fake_shell):
    box = CubeToolbox(fake_shell, max_output_bytes=4)
    fake_shell.files.store["/f"] = b"abcdefgh"
    assert box.read_file("/f") == "abcd\n[truncated: 4 more bytes not shown]"
    assert box.read_file("/missing").startswith("Error: could not read /missing:")


def test_write_failure_comes_back_as_text(fake_shell):
    assert (
        CubeToolbox(fake_shell)
        .write_file("/nope/x", "y")
        .startswith("Error: could not write /nope/x:")
    )


def test_limit_must_be_positive(fake_shell):
    with pytest.raises(ValueError):
        CubeToolbox(fake_shell, max_output_bytes=0)
