"""Application."""

from __future__ import annotations

__all__ = ("Defrag",)

import gi

gi.require_version("Gtk", "4.0")

from gi.repository import GLib, Gtk  # pyright: ignore[reportMissingModuleSource]  # noqa: E402

from app.main_window import MainWindow  # noqa: E402


class Defrag(Gtk.Application):
    """HDD/SSD defragmentation with BTRFS file system."""

    def __init__(self) -> None:  # noqa: D107
        super().__init__(application_id="com.example.Defrag")
        GLib.set_application_name("Defrag")

    def do_activate(self) -> None:
        """Do activate."""
        window = MainWindow()
        window.set_application(self)
        window.set_title("Defrag")
        window.set_default_size(640, 480)
        window.present()
