# Defrag - HDD/SSD defragmentation with BTRFS file system.
# Copyright (c) 2025 Gennady Kostyunin
# SPDX-License-Identifier: GPL-3.0-or-later
#
"""Set of auxiliary tools."""

from __future__ import annotations

__all__ = ("WinToolsMixin",)

import logging
import os
import shlex

import psutil
from gi.repository import Gio  # pyright: ignore[reportMissingModuleSource]

from defrag.translator import _


class WinToolsMixin:
    """Helper tools for the application window."""

    def __init__(self, **kwargs) -> None:  # type: ignore[no-untyped-def]  # noqa: D107
        # Is installed BleachBit
        self.IS_INSTALLED_BLEACHBIT: bool = False
        self.check_installed_bleachbit()

        # List of all disk partitions and their details
        self.BTRFS_PARTITIONS_LIST: list[dict[str, str | float]] = []
        self.update_info_btrfs_partitions()

        # Create command for run gui applications as administrator
        self.gui_as_root_command: str = shlex.join(
            ["pkexec", "env"]
            + [
                f"{key}={value}"
                for key, value in os.environ.copy().items()
                if key in ["WAYLAND_DISPLAY", "XDG_RUNTIME_DIR", "DISPLAY", "XAUTHORITY"]
            ],
        )

    def check_installed_bleachbit(self) -> None:
        """Check if BleachBit is installed on the user's computer."""
        # Flags for proper I/O handling
        flags = Gio.SubprocessFlags.STDOUT_PIPE | Gio.SubprocessFlags.STDERR_PIPE
        # Create commands
        command_str = "which bleachbit"
        command_args = shlex.split(command_str)
        # Create the subprocess
        try:
            process = Gio.Subprocess.new(command_args, flags)
            # Run synchronously, send optional input, get output
            success, stdout_buf, stderr_buf = process.communicate_utf8()
            if success:
                self.IS_INSTALLED_BLEACHBIT = "bleachbit" in stdout_buf
            else:
                # Raise a modal window with an error message
                self.sync_alert_dialog(
                    message=_("ERROR"),
                    detail=stderr_buf,
                    buttons=["Cancel"],
                )
        except Exception as err:
            # Log the exception and traceback
            logging.exception("Checking for BleachBit presence failed with an error.")
            # Raise a modal window with an error message
            self.sync_alert_dialog(
                message=_("ERROR"),
                detail=str(err),
                buttons=["Cancel"],
            )

    def update_info_btrfs_partitions(self) -> None:
        """Retrieves a list of all disk partitions and their details.

        Only BtrFS partitions.
        """
        partitions_list: list[dict[str, str | float]] = []
        # all=False returns all mounted partitions
        for partition in psutil.disk_partitions(all=False):
            try:
                fstype = partition.fstype
                if fstype == "btrfs":
                    usage = psutil.disk_usage(partition.mountpoint)
                    partitions_list.append(
                        {
                            "device": partition.device,
                            "mountpoint": partition.mountpoint,
                            "fstype": fstype,
                            "total_size_gb": round(usage.total / (1024**3), 2),
                            "used_gb": round(usage.used / (1024**3), 2),
                            "free_gb": round(usage.free / (1024**3), 2),
                            "percent_used": usage.percent,
                        },
                    )
            except OSError:
                # Log the exception and traceback
                logging.info("Info: Mountpoint inaccessible.")
                # Handle cases where mountpoints might be inaccessible
                continue
        self.BTRFS_PARTITIONS_LIST = partitions_list
