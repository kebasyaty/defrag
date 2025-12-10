"""Application."""

from __future__ import annotations

__all__ = ("Defrag",)


from gi.repository import Adw, GLib  # pyright: ignore[reportMissingModuleSource]

from app.constants import APP_ID, APP_NAME
from app.main_window import MainWindow


class Defrag(Adw.Application):
    """HDD/SSD defragmentation with BTRFS file system."""

    def __init__(self) -> None:  # noqa: D107
        super().__init__(application_id=APP_ID)
        self.connect("activate", self.on_activate)
        if not self.props.active_window:
            GLib.set_application_name(APP_NAME)

    def on_activate(self, app: Adw.Application) -> None:
        """Create main window."""
        window = self.props.active_window
        if not window:
            window = MainWindow(
                title=APP_NAME,
                application=app,
                default_width=640,
                default_height=480,
            )
        window.present()
