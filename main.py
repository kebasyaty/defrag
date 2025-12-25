#
#                          ,...
# `7MM"""Yb.             .d' ""
#   MM    `Yb.           dM`
#   MM     `Mb  .gP"Ya  mMMmm`7Mb,od8 ,6"Yb.  .P"Ybmmm
#   MM      MM ,M'   Yb  MM    MM' "'8)   MM :MI  I8
#   MM     ,MP 8M""""""  MM    MM     ,pm9MM  WmmmP"
#   MM    ,dP' YM.    ,  MM    MM    8M   MM 8M
# .JMMmmmdP'    `Mbmmd'.JMML..JMML.  `Moo9^Yo.YMMMMMb
#                                            6'     dP
#                                            Ybmmmd'
#
# Copyright (c) 2025 kebasyaty - Gennady Kostyunin
# Defrag is free software under terms of the GPL-3.0 License.
# Repository https://github.com/kebasyaty/defrag
#
"""Run Application."""

from __future__ import annotations

import gi

gi.require_version("Gtk", "4.0")
gi.require_version("Adw", "1")


import sys  # noqa: E402

from app import Defrag  # noqa: E402
from app.check_bleachbit import check_installed_bleachbit  # noqa: E402


def main() -> None:
    """Run Application."""
    check_installed_bleachbit()
    app = Defrag()
    exit_status = app.run(sys.argv)
    sys.exit(exit_status)


if __name__ == "__main__":
    main()
