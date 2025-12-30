"""Custom Dialogs."""

from __future__ import annotations

__all__ = ("SpinnerDialog",)

import logging
import shlex
import signal

from gi.repository import Adw, Gio, Gtk

from app.translator import gettext

logger = logging.getLogger(__name__)


class SpinnerDialog(Gtk.Dialog):
    """Custom dialog with (progress bar) Spinner."""

    def __init__(  # noqa: D107
        self,
        parent: Adw.ApplicationWindow,
        command_str: str,
        is_abort_btn: bool = True,
    ):
        super().__init__(
            title=gettext("Operation started"),
            transient_for=parent,
            modal=True,
            deletable=False,
        )
        self.set_default_size(300, 100)

        # Add application window
        self.app_window = parent

        # Split the command string into a list of arguments
        self.command_args = shlex.split(command_str)

        # Get the content area
        content_area = self.get_content_area()

        # Add a top label
        self.top_label = Gtk.Label(
            label=gettext("The process will take some time."),
            halign=Gtk.Align.CENTER,
            margin_top=24,
        )
        content_area.append(self.top_label)

        # Add the (progress bar) Spinner
        self.progressbar_spinner = Adw.Spinner(
            halign=Gtk.Align.CENTER,
            width_request=48,
            height_request=48,
            margin_top=24,
        )
        content_area.append(self.progressbar_spinner)

        # Add a bottom label
        if is_abort_btn:
            self.bottom_label = Gtk.Label(
                label=gettext("Please wait..."),
                halign=Gtk.Align.CENTER,
                margin_top=24,
                margin_bottom=24,
            )
            content_area.append(self.bottom_label)

        # Add an "Abort" button
        self.add_button(gettext("Abort"), Gtk.ResponseType.CANCEL)
        self.connect("response", self.on_response)

    def on_response(self, dialog, response) -> None:
        """Handle button response."""
        if response == Gtk.ResponseType.CANCEL:
            # Stopping the process
            self.process.send_signal(signal.SIGTERM)
            # Log ERROR.
            logger.info("Premature termination of a process by the user.")
            # Add a message to information box of service
            self.app_window.result_info_textview.set_label(
                gettext("Premature termination of a process by the user."),
            )
            # Display the result of a subprocess
            self.app_window.display_result_info_vbox.set_visible(True)
            # Close dialog
            self.destroy()

    def run_operation(self) -> None:
        """For start a operation in a separate thread."""
        # Define flags to pipe stdout and stderr
        flags = Gio.SubprocessFlags.STDOUT_PIPE | Gio.SubprocessFlags.STDERR_PIPE
        # Create the subprocess
        try:
            self.process = Gio.Subprocess.new(self.command_args, flags)
            # Run synchronously, send optional input, get output
            # Returns a tuple: (success, stdout_buf, stderr_buf)
            success, stdout_buf, stderr_buf = self.process.communicate_utf8(
                stdin_buf=None,
                cancellable=None,
            )
            if success:
                if len(stdout_buf) == 0:
                    stdout_buf = gettext("The operation was completed successfully.")
                # Add a message to information box of service
                self.app_window.result_info_textview.set_label(stdout_buf)
            else:
                # Log ERROR.
                logger.error(stderr_buf)
                # Add a error message to information box of service
                label_str = gettext("ERROR")
                self.app_window.result_info_label.set_markup(f"<b>{label_str}:</b>")
                self.app_window.result_info_textview.set_label(stderr_buf)

        except Exception as err:
            err_msg = "Subprocess ended with an error"
            # Log the exception and traceback
            logger.exception(err_msg)
            # Add a error message to information box of service
            label_str = gettext("ERROR")
            self.app_window.result_info_label.set_markup(f"<b>{label_str}:</b>")
            self.app_window.result_info_textview.set_label(f"{err_msg}:\n{err}")

        # Display the result of a subprocess
        self.display_result_info_vbox.set_visible(True)
        # Stop the (progress bar) Spinner
        self.destroy()
