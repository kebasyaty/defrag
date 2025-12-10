"""Run Application."""

from __future__ import annotations

import gi

gi.require_version("Gtk", "4.0")
gi.require_version("Adw", "1")

import sys  # noqa: E402

from app import Defrag  # noqa: E402


def main() -> None:
    """Business logic."""
    # Create an instance of the Defrag class
    app = Defrag()
    # Run application
    exit_status = app.run(sys.argv)
    sys.exit(exit_status)


if __name__ == "__main__":
    main()
