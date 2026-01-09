# Defrag - HDD/SSD defragmentation with BTRFS file system.
# Copyright (c) 2025 Gennady Kostyunin
# SPDX-License-Identifier: GPL-3.0-or-later
"""Run the application `Defrag`."""

from __future__ import annotations

__all__ = ("main",)

from defrag import Defrag


def main() -> int:
    """Run the application `Defrag`."""
    app = Defrag()
    return app.run(None)
