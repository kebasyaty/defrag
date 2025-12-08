"""Run Application."""

from __future__ import annotations

import gi

gi.require_version("Gtk", "4.0")

import sys  # noqa: E402

import darkdetect  # noqa: E402
from app import Defrag  # noqa: E402
from gi.repository import Gtk  # pyright: ignore[reportMissingModuleSource] # noqa: E402


def main() -> None:
    """Business logic."""
    # Replace application theme on system theme
    settings = Gtk.Settings.get_default()
    if settings is not None:
        settings.set_property(
            "gtk-application-prefer-dark-theme",
            darkdetect.isDark(),
        )
    # Create an instance of the Defrag class
    app = Defrag()
    # Run application
    exit_status = app.run(sys.argv)
    sys.exit(exit_status)


if __name__ == "__main__":
    main()
