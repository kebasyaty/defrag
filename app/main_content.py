"""Right side of the application."""

from __future__ import annotations

__all__ = ("MainContent",)

from typing import Any

from gi.repository import Gio, Gtk

from app.translator import gettext


class MainContent:
    """Main content area."""

    def __init__(self) -> None:  # noqa: D107
        # Create a page for dynamic content
        self.dynamic_page_vbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=6)
        self.dynamic_page_vbox.set_margin_start(30)
        self.dynamic_page_vbox.set_hexpand(True)
        self.content_hbox.append(self.dynamic_page_vbox)

    def clean_dynamic_page(self) -> None:
        """Remove all child elements in `dynamic_page_vbox`."""
        # Observe the children of `dynamic_page_vbox`
        children_model = self.dynamic_page_vbox.observe_children()
        # Iterate through the children of `dynamic_page_vbox`
        child_list: list[Gtk.Widget] = []
        for idx in range(children_model.get_n_items()):
            child = children_model.get_item(idx)
            if isinstance(child, Gtk.Widget):
                child_list.append(child)
        for child in child_list:
            self.dynamic_page_vbox.remove(child)
        # Additionally remove the following keys
        if len(child_list) > 0:
            del self.__dict__["display_result_info_vbox"]
            del self.__dict__["result_info_textview"]

    def on_subprocess_exit(self, process: Gio.Subprocess, res: Any) -> None:
        """Get result of subprocess or error."""
        # Read the output streams in the callback
        stdout_stream, stderr_stream = process.get_stdout_pipe(), process.get_stderr_pipe()
        # Reading from streams and converting to string result
        exit_code = process.get_exit_status()
        result_str = gettext("The operation was completed successfully.")
        if exit_code == 0:
            if stdout_stream is not None:
                stdout_bytes = stdout_stream.read_bytes(1024, None)
                tmp_ = stdout_bytes.get_data()
                if tmp_ is not None:
                    result_str = tmp_.decode("utf-8")
        else:
            if stderr_stream is not None:
                stderr_bytes = stderr_stream.read_bytes(1024, None)
                tmp_ = stderr_bytes.get_data()
                if tmp_ is not None:
                    result_str = tmp_.decode("utf-8")
        # Display the result of a subprocess
        self.result_info_textview.set_label(result_str)
        self.display_result_info_vbox.set_visible(True)

    def on_subprocess_run(self, widget: Any, command_args: list[str]) -> None:
        """Run subprocess."""
        # Create a GSubprocess
        # 'flags' are important for proper I/O handling
        process = Gio.Subprocess.new(
            command_args,
            Gio.SubprocessFlags.STDOUT_PIPE | Gio.SubprocessFlags.STDERR_PIPE,
        )
        # Asynchronously watch for the process termination
        # When it exits, the callback function will be triggered
        process.wait_async(None, self.on_subprocess_exit)
