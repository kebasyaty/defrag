"""Main Window."""

from __future__ import annotations

__all__ = ("MainWindow",)

import os

from gi.repository import Adw, Gtk  # pyright: ignore[reportMissingModuleSource]

from app.main_content import MainContent
from app.sidebar import Sidebar


class MainWindow(Adw.ApplicationWindow, Sidebar, MainContent):
    """Main Window."""

    def __init__(self, **kwargs) -> None:  # type: ignore[no-untyped-def]  # noqa: D107
        Adw.ApplicationWindow.__init__(self, **kwargs)

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
