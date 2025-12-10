"""Main Window."""

from __future__ import annotations

__all__ = ("MainWindow",)

from gi.repository import Adw, Gtk  # pyright: ignore[reportMissingModuleSource]

from app.left_box import LeftBox
from app.right_box import RightBox


class MainWindow(Adw.ApplicationWindow, LeftBox, RightBox):
    """Main Window."""

    def __init__(self, **kwargs) -> None:  # type: ignore[no-untyped-def]  # noqa: D107
        Adw.ApplicationWindow.__init__(self, **kwargs)

        # Create the main horizontal box
        self.main_hbox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=12)
        self.main_hbox.set_margin_top(18)
        self.main_hbox.set_margin_start(6)
        self.main_hbox.set_margin_end(6)
        self.main_hbox.set_margin_bottom(6)
        self.main_hbox.set_hexpand(True)
        self.set_content(self.main_hbox)  # Set the box as the main child of the window

        LeftBox.__init__(self)
        RightBox.__init__(self)

        # Render content for the Health button
        self.on_btn_health(None)
