"""Remove .flatpak-builder and .flatpak directories."""

from __future__ import annotations

import os
from pathlib import Path
from shutil import rmtree


def flatpak_cleaning(root_dir_path: str) -> None:
    """Remove .flatpak-builder and .flatpak directories."""
    print("Start removing .flatpak-builder and .flatpak directories")  # noqa: T201
    rmtree(Path(*(root_dir_path, ".flatpak-builder")))
    rmtree(Path(*(root_dir_path, ".flatpak")))
    print("Done")  # noqa: T201


if __name__ == "__main__":
    flatpak_cleaning("..")
