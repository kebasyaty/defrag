# Defrag - HDD/SSD defragmentation with BTRFS file system.
# Copyright (c) 2025 Gennady Kostyunin
# SPDX-License-Identifier: GPL-3.0-or-later
#
"""Localization of translations."""

from __future__ import annotations

__all__ = (
    "_",
    "ngettext",
)

import contextlib
import gettext
import locale
from pathlib import Path

# Define the translation domain
APP_DOMAIN = "messages"
# Define the directory where locale files will be stored
LOCALE_DIR = Path(__file__).parent / "locales"


def _get_current_locale() -> str:
    """Get the current locale."""
    # Enable locale awareness from the operating system's environment variables
    # An empty string "" tells setlocale to use the appropriate default settings
    # for the current user environment.
    with contextlib.suppress(locale.Error):
        locale.setlocale(locale.LC_ALL, "")
    # Get language code
    language_code = locale.getlocale()[0]
    # To get a simple two-letter language code (e.g., 'en', 'fr').
    # Normalize the code and extract the first two characters.
    return locale.normalize(language_code).split("_")[0] if language_code else "en"


# Current operating system locale (By default = en)
CURRENT_LOCALE: str = _get_current_locale()

TRANSLATOR: gettext.NullTranslations = gettext.translation(
    domain=APP_DOMAIN,
    localedir=LOCALE_DIR,
    languages=[CURRENT_LOCALE],
    class_=None,
    fallback=True,
)

# Alias the gettext function for convenience
_ = TRANSLATOR.gettext
ngettext = TRANSLATOR.ngettext
