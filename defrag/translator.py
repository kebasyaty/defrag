# Defrag - HDD/SSD defragmentation with BTRFS file system.
# Copyright (c) 2025 Gennady Kostyunin
# SPDX-License-Identifier: GPL-3.0-or-later
"""Localization of translations."""

from __future__ import annotations

__all__ = ("_",)

import contextlib
import gettext
import locale

from defrag import config


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


config.CURRENT_LOCALE = _get_current_locale()

_TRANSLATOR: gettext.NullTranslations = gettext.translation(
    domain=config.APP_DOMAIN,
    localedir=config.LOCALE_DIR,
    languages=[config.CURRENT_LOCALE],
    class_=None,
    fallback=True,
)

# Alias the gettext function for convenience
_ = _TRANSLATOR.gettext
