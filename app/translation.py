"""Localization of translations."""

from __future__ import annotations

__all__ = (
    "gettext",
    "ngettext",
)

import contextlib
import gettext as _gettext
import locale


def get_current_locale() -> str:
    """Get the current locale."""
    # Enable locale awareness from the operating system's environment variables
    # An empty string "" tells setlocale to use the appropriate default settings
    # for the current user environment.
    with contextlib.suppress(locale.Error):
        locale.setlocale(locale.LC_ALL, "")
    # Get language code
    language_code = locale.getlocale()[0]
    # To get a simple two-letter language code (e.g., 'en', 'fr')
    # Normalize the code and extract the first two characters
    return locale.normalize(language_code).split("_")[0] if language_code else "en"


# Current operating system locale (By default = en)
DEFAULT_LOCALE: str = get_current_locale()

TRANSLATION: _gettext.NullTranslations = _gettext.translation(
    domain="messages",
    localedir="config/translations",
    languages=[DEFAULT_LOCALE],
    class_=None,
    fallback=True,
)

gettext = TRANSLATION.gettext
ngettext = TRANSLATION.ngettext
