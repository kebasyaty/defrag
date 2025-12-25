#
#                          ,...
# `7MM"""Yb.             .d' ""
#   MM    `Yb.           dM`
#   MM     `Mb  .gP"Ya  mMMmm`7Mb,od8 ,6"Yb.  .P"Ybmmm
#   MM      MM ,M'   Yb  MM    MM' "'8)   MM :MI  I8
#   MM     ,MP 8M""""""  MM    MM     ,pm9MM  WmmmP"
#   MM    ,dP' YM.    ,  MM    MM    8M   MM 8M
# .JMMmmmdP'    `Mbmmd'.JMML..JMML.  `Moo9^Yo.YMMMMMb
#                                            6'     dP
#                                            Ybmmmd'
#
#
# Copyright (c) 2025 Gennady Kostyunin
# Defrag is free software under terms of the GPL-3.0 License.
# Repository https://github.com/kebasyaty/defrag
#
"""Application."""

from __future__ import annotations

__all__ = ("Defrag",)


from gi.repository import Adw, GLib

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
        self.window = self.props.active_window
        if not self.window:
            self.window = MainWindow(
                title=APP_NAME,
                application=app,
                default_width=640,
                default_height=480,
            )
        self.window.present()
