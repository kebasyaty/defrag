"""Main Window."""

from __future__ import annotations

__all__ = ("MainWindow",)
from gi.repository import Gtk  # pyright: ignore[reportMissingModuleSource]


class MainWindow(Gtk.ApplicationWindow):
    """Main Window."""

    def __init__(self, **kwargs) -> None:  # type: ignore[no-untyped-def]  # noqa: D107
        super().__init__(**kwargs)

        # Create the main horizontal box
        main_hbox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=12)
        main_hbox.set_margin_top(12)
        main_hbox.set_margin_start(6)
        main_hbox.set_margin_end(6)
        main_hbox.set_margin_bottom(6)
        self.set_child(main_hbox)  # Set the box as the main child of the window

        # Create a left vertical box
        left_vbox = Gtk.Box.new(orientation=Gtk.Orientation.VERTICAL, spacing=6)
        main_hbox.append(left_vbox)

        # Create a right vertical box
        right_vbox = Gtk.Box.new(orientation=Gtk.Orientation.VERTICAL, spacing=6)
        main_hbox.append(right_vbox)
