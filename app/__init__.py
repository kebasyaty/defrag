"""Application."""

from __future__ import annotations

__all__ = ("Defrag",)

import gi

gi.require_version("Gtk", "4.0")


import darkdetect  # noqa: E402
from gi.repository import GLib, Gtk  # pyright: ignore[reportMissingModuleSource]  # noqa: E402

from app.constants import APP_ID, APP_NAME  # noqa: E402
from app.main_window import MainWindow  # noqa: E402


class Defrag(Gtk.Application):
    """HDD/SSD defragmentation with BTRFS file system."""

    def __init__(self) -> None:  # noqa: D107
        super().__init__(application_id=APP_ID)
        GLib.set_application_name(APP_NAME)

    def do_activate(self) -> None:
        """Do activate."""
        # Replace application theme on system theme
        settings = Gtk.Settings.get_default()
        if settings is not None:
            settings.set_property(
                "gtk-application-prefer-dark-theme",
                darkdetect.isDark(),
            )
        # Create an instance of the MainWindow class
        window = self.props.active_window
        if not window:
            window = MainWindow(
                title=APP_NAME,
                application=self,
                default_width=640,
                default_height=480,
            )
            window.present()
