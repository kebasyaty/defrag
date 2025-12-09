"""Main Window."""

from __future__ import annotations

__all__ = ("MainWindow",)

from gi.repository import Gtk  # pyright: ignore[reportMissingModuleSource]

from app.left_box import LeftBox
from app.right_box import RightBox


class MainWindow(Gtk.ApplicationWindow, LeftBox, RightBox):
    """Main Window."""

    def __init__(self, **kwargs) -> None:  # type: ignore[no-untyped-def]  # noqa: D107
        Gtk.ApplicationWindow.__init__(self, **kwargs)

        # Create the main horizontal box
        self.main_vbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=12)
        self.main_vbox.set_margin_top(12)
        self.main_vbox.set_margin_start(6)
        self.main_vbox.set_margin_end(6)
        self.main_vbox.set_margin_bottom(6)
        self.main_vbox.set_hexpand(True)
        self.set_child(self.main_vbox)  # Set the box as the main child of the window

        # Create main title horizontal box
        self.main_title_vbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=6)
        self.main_title_vbox.set_margin_top(12)
        self.main_title_vbox.set_hexpand(True)
        self.main_vbox.append(self.main_title_vbox)

        # Create main content horizontal box
        self.main_content_hbox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=6)
        self.main_content_hbox.set_margin_top(12)
        self.main_content_hbox.set_hexpand(True)
        self.main_vbox.append(self.main_content_hbox)

        LeftBox.__init__(self)
        RightBox.__init__(self)

        # Render content for the Health button
        self.on_btn_health(None)
