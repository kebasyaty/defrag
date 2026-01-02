# Defrag - HDD/SSD defragmentation with BTRFS file system.
# Copyright (c) 2025 Gennady Kostyunin
# SPDX-License-Identifier: GPL-3.0-or-later

if __name__ == "__main__":
    import sys
    from defrag import main

    sys.exit(main.main())
