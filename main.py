"""Run Application."""

from __future__ import annotations

import sys

from app import Defrag


def main() -> None:
    """Business logic."""
    app = Defrag()
    exit_status = app.run(sys.argv)
    sys.exit(exit_status)


if __name__ == "__main__":
    main()
