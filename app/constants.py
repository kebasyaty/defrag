"""Global variables.

List of variables:

- `APP_NAME` - Application name.
- `APP_ID` - Application ID.
- `USER_LANG` - Current operating system locale (By default = en)
"""

from __future__ import annotations

__all__ = (
    "APP_NAME",
    "APP_ID",
)


# Application name
APP_NAME: str = "Defrag"
# Application ID
APP_ID: str = "com.example.Defrag"
# Current operating system locale (By default = en)
USER_LANG: str = "en"
