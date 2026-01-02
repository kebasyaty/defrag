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
# Copyright (c) 2025 Gennady Kostyunin
# SPDX-License-Identifier: GPL-3.0-or-later
#
"""Defrag - HDD/SSD defragmentation with BTRFS file system."""

from __future__ import annotations

__all__ = ("Defrag",)

import logging

import gi

try:
    gi.require_version("Adw", "1")
    gi.require_version("Gio", "2.0")
    gi.require_version("GLib", "2.0")
    gi.require_version("Gtk", "4.0")
except Exception:
    logging.exception("Error: GObject dependencies not met.")
    exit()

from gi.repository import Adw, GLib

from defrag.config import (
    APP_ID,
    APP_NAME,
    WINDOW_DEFAULT_HEIGHT,
    WINDOW_DEFAULT_WIDTH,
)
from defrag.window import DefragWindow


class Defrag(Adw.Application):
    """HDD/SSD defragmentation with BTRFS file system."""

    def __init__(self) -> None:  # noqa: D107
        super().__init__(application_id=APP_ID)
        self.connect("activate", self.on_activate)
        if not self.props.active_window:
            GLib.set_application_name(APP_NAME)

    def on_activate(self, app: Adw.Application) -> None:
        """Create app window."""
        self.window = self.props.active_window
        if not self.window:
            self.window = DefragWindow(
                title=APP_NAME,
                application=app,
                default_width=WINDOW_DEFAULT_WIDTH,
                default_height=WINDOW_DEFAULT_HEIGHT,
            )
        self.window.present()
