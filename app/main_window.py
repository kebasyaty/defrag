"""Main Window."""

from __future__ import annotations

__all__ = ("MainWindow",)

import os
import shlex
from typing import Any

from gi.repository import Adw, Gio, Gtk  # pyright: ignore[reportMissingModuleSource]

from app.main_content import MainContent
from app.sidebar import Sidebar


class MainWindow(Adw.ApplicationWindow, Sidebar, MainContent):
    """Main Window."""

    def __init__(self, **kwargs) -> None:  # type: ignore[no-untyped-def]  # noqa: D107
        Adw.ApplicationWindow.__init__(self, **kwargs)

        # Is installed BleachBit
        self.IS_INSTALLED_BLEACHBIT: bool = False
        self.check_installed_bleachbit()

        # Create the main box
        self.main_vbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=12)
        self.main_vbox.set_hexpand(True)
        self.set_content(self.main_vbox)  # Set the box as the main child of the window

        # Create the header box
        self.header_hbox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=6)
        self.header_hbox.set_hexpand(True)
        self.header = Adw.HeaderBar()
        self.header.set_hexpand(True)
        self.header_hbox.append(self.header)
        self.main_vbox.append(self.header_hbox)

        # Create the content box
        self.content_hbox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=6)
        self.content_hbox.set_margin_top(12)
        self.content_hbox.set_margin_start(12)
        self.content_hbox.set_margin_end(12)
        self.content_hbox.set_margin_bottom(12)
        self.content_hbox.set_hexpand(True)
        self.main_vbox.append(self.content_hbox)

        # Create command for run gui applications as administrator
        self.gui_as_root_command = ["pkexec", "env"] + [
            f"{key}={value}"
            for key, value in os.environ.copy().items()
            if key in ["WAYLAND_DISPLAY", "XDG_RUNTIME_DIR", "DISPLAY", "XAUTHORITY"]
        ]

        # Init mixins
        Sidebar.__init__(self)
        MainContent.__init__(self)

        # Render content for the Cleaning button
        self.on_btn_cleaning(None)

    def simple_alert(self, message: str, detail: str, buttons: list[str]) -> None:
        """Simple Alert."""
        dialog = Gtk.AlertDialog(
            modal=True,
            message=message,
            detail=detail,
            buttons=buttons,
        )
        dialog.show(parent=self)

    def check_installed_bleachbit(self) -> None:
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
        process.wait_async(None, self.check_installed_bleachbit_exit)

    def check_installed_bleachbit_exit(self, process: Gio.Subprocess, res: Any) -> None:
        """Get result of main subprocess or error."""
        # Read the output streams in the callback
        stdout_stream, stderr_stream = process.get_stdout_pipe(), process.get_stderr_pipe()
        # Reading from streams and converting to string result
        exit_code = process.get_exit_status()
        if exit_code == 0:
            if stdout_stream is not None:
                stdout_bytes = stdout_stream.read_bytes(1024, None)
                result_bytes = stdout_bytes.get_data()
                if result_bytes is not None:
                    result_str = result_bytes.decode("utf-8")
                    self.IS_INSTALLED_BLEACHBIT = "bleachbit-" in result_str
        else:
            if stderr_stream is not None:
                stderr_bytes = stderr_stream.read_bytes(1024, None)
                error_bytes = stderr_bytes.get_data()
                if error_bytes is not None:
                    error_str = error_bytes.decode("utf-8")
                    dialog = Gtk.AlertDialog(
                        modal=True,
                        message="ERROR",
                        detail=error_str,
                        buttons=["Cancel"],
                    )
                    dialog.show()
