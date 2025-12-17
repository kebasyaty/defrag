"""Localization of translations."""

from __future__ import annotations

__all__ = (
    "get_current_locale",
    "get_translator",
)

import contextlib
import gettext as _gettext
import locale
from gettext import NullTranslations

from babel import Locale


def get_language_name(lang_code: str) -> str | None:
    """Get language name."""
    lang_name = Locale(lang_code).get_language_name(lang_code)
    if lang_name is not None:
        lang_name = lang_name.capitalize()
    return lang_name


LANGUAGES = {
    "en": get_language_name("en"),
    "ru": get_language_name("ru"),
}

# Current operating system locale (By default = en)
DEFAULT_LOCALE = "en"

TRANSLATIONS: dict[str, NullTranslations] = {
    lang: _gettext.translation(
        domain="messages",
        localedir="config/translations",
        languages=[lang],
        class_=None,
        fallback=True,
    )
    for lang in LANGUAGES
}


def get_current_locale() -> None:
    """Get the current locale."""
    global DEFAULT_LOCALE  # noqa: PLW0603
    # Enable locale awareness from the operating system's environment variables
    # An empty string "" tells setlocale to use the appropriate default settings
    # for the current user environment.
    with contextlib.suppress(locale.Error):
        locale.setlocale(locale.LC_ALL, "")
    # Get language code
    language_code = locale.getlocale()[0]
    # To get a simple two-letter language code (e.g., 'en', 'fr')
    if language_code:
        # Normalize the code and extract the first two characters
        DEFAULT_LOCALE = locale.normalize(language_code).split("_")[0]


def get_translator(lang: str = DEFAULT_LOCALE) -> NullTranslations:
    """Get an object of translation for the desired language."""
    return TRANSLATIONS.get(lang, TRANSLATIONS[DEFAULT_LOCALE])
