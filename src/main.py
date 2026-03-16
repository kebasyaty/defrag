# main.py
#
# Copyright 2025 Kebasyaty
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.
#
# SPDX-License-Identifier: GPL-3.0-or-later
"""Run the application `Defrag`."""

from __future__ import annotations

__all__ = ("DefragApplication",)

import logging
import sys

import gi

try:
    gi.require_version("Adw", "1")
    gi.require_version("Gio", "2.0")
    gi.require_version("GLib", "2.0")
    gi.require_version("Gtk", "4.0")
except Exception:
    logging.exception("Error: GObject dependencies not met.")
    exit()

from gi.repository import Adw, Gio

from .config import Config
from .window import DefragWindow


class DefragApplication(Adw.Application):
    """The main application singleton class."""

    def __init__(self):  # noqa: D107
        super().__init__(
            application_id=Config.APP_ID,
            flags=Gio.ApplicationFlags.DEFAULT_FLAGS,
            resource_base_path=Config.RESOURCE_BASE_PATH,
        )
        self.connect("activate", self.on_activate)

    def on_activate(self, event) -> None:
        """Called when the application is activated.

        We raise the application's main window, creating it if
        necessary.
        """
        win = self.props.active_window
        if not win:
            win = DefragWindow(
                title=Config.APP_NAME,
                application=self,
                default_width=Config.WINDOW_WIDTH,
                default_height=Config.WINDOW_HEIGHT,
            )

        win.present()


def main(version):  # noqa: ARG001
    """The application's entry point."""
    app = DefragApplication()
    return app.run(sys.argv)
