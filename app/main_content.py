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

    def unlock_buttons_to_sidebar(self, active_button_name: str) -> None:
        """Unlock all buttons on sidebar and lock active button."""
        # Observe the children of `sidebar_vbox`
        children_model = self.sidebar_vbox.observe_children()
        # Iterate through the children of `sidebar_vbox`
        for idx in range(children_model.get_n_items()):
            child = children_model.get_item(idx)
            if isinstance(child, Gtk.Button):
                child.set_sensitive(True)
        # Lock active button
        self.__dict__[active_button_name].set_sensitive(False)

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
            del self.__dict__["result_info_label"]
            del self.__dict__["result_info_textview"]
            del self.__dict__["display_result_info_vbox"]

    def on_subprocess_exit(self, process: Gio.Subprocess, res: Any) -> None:
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
                    if len(result_str) == 0:
                        result_str = gettext("The operation was completed successfully.")
                    self.result_info_textview.set_label(result_str)
        else:
            if stderr_stream is not None:
                stderr_bytes = stderr_stream.read_bytes(1024, None)
                error__bytes = stderr_bytes.get_data()
                if error__bytes is not None:
                    error_str = error__bytes.decode("utf-8")
                    label_str = gettext("ERROR")
                    self.result_info_label.set_markup(f"<b>{label_str}:</b>")
                    self.result_info_textview.set_label(error_str)
        # Display the result of a subprocess
        self.display_result_info_vbox.set_visible(True)

    def on_subprocess_run(self, widget: Any, command_args: list[str]) -> None:
        """Starts a main subprocess asynchronously."""
        # Flags for proper I/O handling
        flags = Gio.SubprocessFlags.STDOUT_PIPE | Gio.SubprocessFlags.STDERR_PIPE
        # Create the subprocess
        process = Gio.Subprocess.new(command_args, flags)
        # Asynchronously watch for the process termination
        # When it exits, the callback function will be triggered
        process.wait_async(callback=self.on_subprocess_exit)
