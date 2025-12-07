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
        self.set_child(main_hbox)
