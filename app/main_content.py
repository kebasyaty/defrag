"""Right side of the application."""

from __future__ import annotations

__all__ = ("MainContent",)

from typing import Any

from gi.repository import Gio, Gtk  # pyright: ignore[reportMissingModuleSource]


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

    def on_process_exit(self, process: Gio.Subprocess, res: Any) -> None:
        """???"""
        # Read the output streams in the callback
        stdout_stream, stderr_stream = process.get_stdout_pipe(), process.get_stderr_pipe()

        # Note: Reading streams is also typically done asynchronously in a real app,
        # but for simplicity we use a blocking read here, which is fine since the process already finished
        stdout_str = "???"
        if stdout_stream is not None:
            stdout_bytes = stdout_stream.read_bytes(1024, None)
            tmp = stdout_bytes.get_data()
            if tmp is not None:
                stdout_str = tmp.decode("utf-8")

        stderr_str = "???"
        if stderr_stream is not None:
            stderr_bytes = stderr_stream.read_bytes(1024, None)
            tmp = stderr_bytes.get_data()
            if tmp is not None:
                stderr_str = tmp.decode("utf-8")

        exit_code = process.get_exit_status()
        if exit_code == 0:
            print(f"Async Command Output (Exit Code {exit_code}):\n{stdout_str}")  # noqa: T201
        else:
            print(f"Async Command Failed (Exit Code {exit_code}):\n{stderr_str}")  # noqa: T201

    def on_process_run(self, widget: Any, command_args: list[str]) -> None:
        """???"""
        # Create a GSubprocess
        # 'flags' are important for proper I/O handling
        process = Gio.Subprocess.new(
            command_args,
            Gio.SubprocessFlags.STDOUT_PIPE | Gio.SubprocessFlags.STDERR_PIPE,
        )

        # Asynchronously watch for the process termination
        # When it exits, the callback function will be triggered
        process.wait_async(None, self.on_process_exit)
