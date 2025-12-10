"""Main Window."""

from __future__ import annotations

__all__ = ("MainWindow",)

from gi.repository import Adw, Gtk  # pyright: ignore[reportMissingModuleSource]

from app.right_box import RightBox
from app.sidebar import SideBar


class MainWindow(Adw.ApplicationWindow, SideBar, RightBox):
    """Main Window."""

    def __init__(self, **kwargs) -> None:  # type: ignore[no-untyped-def]  # noqa: D107
        Adw.ApplicationWindow.__init__(self, **kwargs)

        # Create the main box
        self.main_vbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=12)
        self.main_vbox.set_hexpand(True)
        self.set_content(self.main_vbox)  # Set the box as the main child of the window

        # Create the header box
        self.header_hbox = Gtk.Box.new(orientation=Gtk.Orientation.HORIZONTAL, spacing=6)
        self.header_hbox.set_hexpand(True)
        self.header = Adw.HeaderBar()
        self.header.set_hexpand(True)
        self.header_hbox.append(self.header)
        self.main_vbox.append(self.header_hbox)

        # Create the content box
        self.content_hbox = Gtk.Box.new(orientation=Gtk.Orientation.HORIZONTAL, spacing=6)
        self.content_hbox.set_margin_top(18)
        self.content_hbox.set_margin_start(12)
        self.content_hbox.set_margin_end(12)
        self.content_hbox.set_margin_bottom(12)
        self.content_hbox.set_hexpand(True)
        self.main_vbox.append(self.content_hbox)

        # Init mixins
        SideBar.__init__(self)
        RightBox.__init__(self)

        # Render content for the Health button
        self.on_btn_health(None)
