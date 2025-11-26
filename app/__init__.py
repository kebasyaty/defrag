"""Application."""

from __future__ import annotations

__all__ = ("Defrag",)

import gi
from gi.repository import GLib, Gtk

gi.require_version("Gtk", "4.0")


class Defrag(Gtk.Application):
    """HDD/SSD defragmentation with BTRFS file system."""

    def __init__(self) -> None:  # noqa: D107
        super().__init__(application_id="com.example.Defrag")
        GLib.set_application_name("Defrag")

    def do_activate(self) -> None:
        """???"""
        window = Gtk.ApplicationWindow(application=self, title="Defrag")
        window.present()
