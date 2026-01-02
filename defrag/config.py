# Defrag - HDD/SSD defragmentation with BTRFS file system.
# Copyright (c) 2025 Gennady Kostyunin
# SPDX-License-Identifier: GPL-3.0-or-later
#
"""Global variables.

List of variables:

- `APP_NAME` - Application name.
- `APP_ID` - Application ID.
- `WINDOW_DEFAULT_WIDTH` - Default application window width.
- `WINDOW_DEFAULT_HEIGHT` - Default application window height.
"""

from __future__ import annotations

__all__ = (
    "APP_NAME",
    "APP_ID",
    "WINDOW_DEFAULT_WIDTH",
    "WINDOW_DEFAULT_HEIGHT",
)


# Application name
APP_NAME: str = "Defrag"
# Application ID
APP_ID: str = "com.example.Defrag"
# Default application window width
WINDOW_DEFAULT_WIDTH: int = 640
# Default application window height
WINDOW_DEFAULT_HEIGHT: int = 480
