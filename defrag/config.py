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
- `APP_DOMAIN` - Define the translation domain.
- `LOCALE_DIR` - Define the directory where locale files will be stored.
- `CURRENT_LOCALE` - Current operating system locale (by default = en).
"""

from __future__ import annotations

__all__ = (
    "APP_NAME",
    "APP_ID",
    "WINDOW_DEFAULT_WIDTH",
    "WINDOW_DEFAULT_HEIGHT",
    "APP_DOMAIN",
    "LOCALE_DIR",
    "CURRENT_LOCALE",
)

from pathlib import Path

# Application name
APP_NAME: str = "Defrag"
# Application ID
APP_ID: str = "com.example.Defrag"
# Default application window width
WINDOW_DEFAULT_WIDTH: int = 640
# Default application window height
WINDOW_DEFAULT_HEIGHT: int = 480
# Define the translation domain
APP_DOMAIN: str = "messages"
# Define the directory where locale files will be stored
LOCALE_DIR: Path = Path(__file__).parent / "locales"
# Current operating system locale (by default = en)
CURRENT_LOCALE: str = "en"
