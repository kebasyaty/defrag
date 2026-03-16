# config.py
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
"""Application settings."""

from __future__ import annotations

__all__ = ("Config",)

from pathlib import Path
from typing import ClassVar, final


@final
class Config:
    """Application settings."""

    # Application name
    APP_NAME: ClassVar[str] = "Defrag"
    # Application ID
    APP_ID: ClassVar[str] = "com.github.kebasyaty.defrag"
    # Path to base resources
    RESOURCE_BASE_PATH: ClassVar[str] = "/com/github/kebasyaty/defrag"
    # Default application window width
    WINDOW_WIDTH: ClassVar[int] = 640
    # Default application window height
    WINDOW_HEIGHT: ClassVar[int] = 480
    # Define the translation domain
    APP_DOMAIN: ClassVar[str] = "messages"
    # Define the directory where locale files will be stored
    LOCALE_DIR: ClassVar[Path] = Path(__file__).parent / "locales"
    # Current operating system locale (by default = en)
    current_locale: ClassVar[str] = "en"
