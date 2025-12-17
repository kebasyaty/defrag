"""Language."""

from __future__ import annotations

import contextlib
import locale

from app import constants


def get_language_code() -> None:
    """Get the current locale."""
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
        constants.USER_LANG = locale.normalize(language_code).split("_")[0]
