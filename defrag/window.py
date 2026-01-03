# Defrag - HDD/SSD defragmentation with BTRFS file system.
# Copyright (c) 2025 Gennady Kostyunin
# SPDX-License-Identifier: GPL-3.0-or-later
#
"""Main application window."""

from __future__ import annotations

__all__ = ("DefragWindow",)

import os
import shlex
import threading
from typing import Any, Literal

from gi.repository import Adw, Gtk  # pyright: ignore[reportMissingModuleSource]

from defrag.blank_page import BlankPage
from defrag.dialogues import SpinnerDialog
from defrag.sidebar import Sidebar
from defrag.utils import WinToolsMixin


class DefragWindow(
    Adw.ApplicationWindow,
    WinToolsMixin,
    Sidebar,
    BlankPage,
):
    """Main application window."""

    def __init__(self, **kwargs) -> None:  # type: ignore[no-untyped-def]  # noqa: D107
        Adw.ApplicationWindow.__init__(self, **kwargs)

        # Init mixin
        WinToolsMixin.__init__(self)

        # Create command for run gui applications as administrator
        self.gui_as_root_command: str = shlex.join(
            ["pkexec", "env"]
            + [
                f"{key}={value}"
                for key, value in os.environ.copy().items()
                if key in ["WAYLAND_DISPLAY", "XDG_RUNTIME_DIR", "DISPLAY", "XAUTHORITY"]
            ],
        )

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

        # Init mixins
        Sidebar.__init__(self)
        BlankPage.__init__(self)

        # Render content for the Cleaning button
        self._on_sidebar_btn_cleaning(None)

    def sync_alert_dialog(
        self,
        message: str,
        detail: str,
        buttons: list[Literal["Cancel", "OK"]],
    ) -> None:
        """Simple Alert.

        Dialog uses the synchronous show() method.
        """
        dialog = Gtk.AlertDialog(
            modal=True,
            message=message,
            detail=detail,
            buttons=buttons,
        )
        dialog.show(parent=self)

    def _on_run_async_subprocess(
        self,
        widget: Any,
        command_str: str,
        is_abort_btn: bool = True,
    ) -> None:
        """Handler of button click for run asynchronous subprocess.

        Uses the (progress bar) SpinnerDialog.
        """
        # Clean a message to information box of service
        self.result_info_textview.set_label("")
        # Hide the information box with the result from the subprocess
        self.display_result_info_vbox.set_visible(False)
        # Create and show the progress dialog
        progress_dialog = SpinnerDialog(
            parent=self,
            command_str=command_str,
            is_abort_btn=is_abort_btn,
        )
        # Start the long operation in a new thread
        thread = threading.Thread(target=progress_dialog.run_operation)
        thread.start()
        # Present the dialog
        progress_dialog.present()
