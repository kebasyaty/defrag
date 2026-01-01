# Defrag - HDD/SSD defragmentation with BTRFS file system.
# Copyright (c) 2025 Gennady Kostyunin
# SPDX-License-Identifier: GPL-3.0-or-later
#
"""Run the application `Defrag`."""

from __future__ import annotations

__all__ = ("main",)

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


from defrag import Defrag


def main() -> int:
    """Run the application `Defrag`."""
    app = Defrag()
    return app.run(None)
