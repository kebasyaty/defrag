# Defrag - HDD/SSD defragmentation with BTRFS file system.
# Copyright (c) 2025 Gennady Kostyunin
# SPDX-License-Identifier: GPL-3.0-or-later
#
"""Custom dialog with (progress bar) Spinner."""

from __future__ import annotations

__all__ = ("SpinnerDialog",)

import logging
import shlex
import signal

from gi.repository import Adw, Gio, GLib, Gtk

from defrag.translator import _


class SpinnerDialog(Gtk.Dialog):
    """Custom dialog with (progress bar) Spinner."""

    def __init__(  # noqa: D107
        self,
        parent: Adw.ApplicationWindow,
        command_str: str,
        is_abort_btn: bool = True,
    ):
        super().__init__(
            title=_("Operation started"),
            transient_for=parent,
            modal=True,
            deletable=False,
        )
        self.set_default_size(300, 100)

        # Add application window (To access parent fields and methods)
        self.app_window = parent

        # Split the command string into a list of arguments
        self.command_args = shlex.split(command_str)

        # Get the content area
        content_area = self.get_content_area()

        # Add a top label
        self.top_label = Gtk.Label(
            label=_("The process will take some time."),
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
        self.bottom_label = Gtk.Label(
            label=_("Please wait..."),
            halign=Gtk.Align.CENTER,
            margin_top=24,
            margin_bottom=24,
        )
        content_area.append(self.bottom_label)

        # Add an "Abort" button
        if is_abort_btn:
            self.add_button(_("Abort"), Gtk.ResponseType.CANCEL)
            self.connect("response", self.on_response)

    def on_response(self, dialog, response) -> None:
        """Handle button response."""
        if response == Gtk.ResponseType.CANCEL:
            # Stopping the process
            self.process.send_signal(signal.SIGTERM)
            # Log ERROR.
            logging.info("Premature termination of a process by the user.")
            # Add a message to information box of service
            self.app_window.page_info_textview.set_label(
                _("Premature termination of a process by the user."),
            )
            # Display the result of a subprocess
            self.app_window.page_info_vbox.set_visible(True)
            # Close dialog the (progress bar) SpinnerDialog
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
                    stdout_buf = _("The operation is completed.")
                # Add a message to information box of service
                self.app_window.page_info_textview.set_label(stdout_buf)
            else:
                # Log ERROR.
                logging.error(stderr_buf)
                # Add a error message to information box of service
                label_str = _("ERROR")
                self.app_window.page_info_label.set_markup(f"<b>{label_str}:</b>")
                self.app_window.page_info_textview.set_label(stderr_buf)

        except Exception as err:
            err_msg = "Subprocess ended with an error"
            # Log the exception and traceback
            logging.exception(err_msg)
            # Add a error message to information box of service
            label_str = _("ERROR")
            self.app_window.page_info_label.set_markup(f"<b>{label_str}:</b>")
            self.app_window.page_info_textview.set_label(f"{err_msg}:\n{err}")

        # Display the result of a subprocess
        self.app_window.page_info_vbox.set_visible(True)
        # Close dialog the (progress bar) SpinnerDialog
        GLib.idle_add(self.destroy)
