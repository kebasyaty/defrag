"""Application."""

from __future__ import annotations

__all__ = ("Defrag",)


from gi.repository import Adw, GLib, Gtk  # pyright: ignore[reportMissingModuleSource]

from app.constants import APP_ID, APP_NAME
from app.main_window import MainWindow


class Defrag(Adw.Application):
    """HDD/SSD defragmentation with BTRFS file system."""

    def __init__(self) -> None:  # noqa: D107
        super().__init__(application_id=APP_ID)
        GLib.set_application_name(APP_NAME)

    def do_activate(self) -> None:
        """Do activate."""
        # Replace application theme on system theme
        settings = Gtk.Settings.get_default()
        if settings is not None:
            settings.set_property("gtk-icon-theme-name", "Adwaita")
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
