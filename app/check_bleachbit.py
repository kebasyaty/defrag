"""Check if BleachBit is installed on the user's computer."""

from __future__ import annotations

import shlex
from typing import Any

from gi.repository import Gio, Gtk


def check_installed_bleachbit(constants) -> None:
    """Check if BleachBit is installed on the user's computer."""
    # Flags for proper I/O handling
    flags = Gio.SubprocessFlags.STDOUT_PIPE | Gio.SubprocessFlags.STDERR_PIPE
    # Create commands
    command_string = "rpm -q bleachbit"
    command_args = shlex.split(command_string)
    # Create the subprocess
    process = Gio.Subprocess.new(command_args, flags)
    # Asynchronously watch for the process termination
    # When it exits, the callback function will be triggered
    process.wait_async(None, check_installed_bleachbit_exit, constants)


def check_installed_bleachbit_exit(process: Gio.Subprocess, res: Any, constants) -> None:  # noqa: ARG001
    """Get result of main subprocess or error."""
    # Read the output streams in the callback
    stdout_stream, stderr_stream = process.get_stdout_pipe(), process.get_stderr_pipe()
    # Reading from streams and converting to string result
    exit_code = process.get_exit_status()
    if exit_code == 0:
        if stdout_stream is not None:
            stdout_bytes = stdout_stream.read_bytes(1024, None)
            tmp_ = stdout_bytes.get_data()
            if tmp_ is not None:
                constants.IS_INSTALLED_BLEACHBIT = "bleachbit-" in tmp_.decode("utf-8")
    else:
        if stderr_stream is not None:
            stderr_bytes = stderr_stream.read_bytes(1024, None)
            tmp_ = stderr_bytes.get_data()
            if tmp_ is not None:
                stderr_str = tmp_.decode("utf-8")
                dialog = Gtk.AlertDialog(
                    modal=True,
                    message="ERROR",
                    detail=stderr_str,
                    buttons=["Cancel"],
                )
                dialog.show()
