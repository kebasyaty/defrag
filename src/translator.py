# translator.py
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
"""Localization of translations."""

from __future__ import annotations

__all__ = ("_",)

import contextlib
import gettext
import locale

from .config import Config


def _get_current_locale() -> str:
    """Get the current locale."""
    # Enable locale awareness from the operating system's environment variables
    # An empty string "" tells setlocale to use the appropriate default settings
    # for the current user environment.
    with contextlib.suppress(locale.Error):
        locale.setlocale(locale.LC_ALL, "")
    # Get language code
    language_code: str | None = locale.getlocale()[0]
    # To get a simple two-letter language code (e.g., 'en', 'fr').
    # Normalize the code and extract the first two characters.
    return locale.normalize(language_code).split("_")[0] if language_code is not None else "en"


Config.current_locale = _get_current_locale()

_TRANSLATOR: gettext.NullTranslations = gettext.translation(
    domain=Config.APP_DOMAIN,
    localedir=Config.LOCALE_DIR,
    languages=[Config.current_locale],
    class_=None,
    fallback=True,
)

# Alias the gettext function for convenience
_ = _TRANSLATOR.gettext
