"""Global variables.

List of variables:

- `APP_NAME` - Application name.
- `APP_ID` - Application ID.
- `IS_DARK_THEME` - Does the system use a dark theme.
"""

from __future__ import annotations

__all__ = (
    "APP_NAME",
    "APP_ID",
    "IS_DARK_THEME",
)

import darkdetect

# Application name
APP_NAME: str = "Defrag"
# Application ID
APP_ID: str = "com.example.Defrag"
# Does the system use a dark theme
IS_DARK_THEME: bool = darkdetect.isDark()
