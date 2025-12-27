"""Main application window."""

from __future__ import annotations

__all__ = ("MainWindow",)

import logging
import os
import shlex

import psutil
from gi.repository import Adw, Gio, Gtk  # pyright: ignore[reportMissingModuleSource]

from app.dynamic_page import DynamicPage
from app.sidebar import Sidebar
from app.translator import gettext


class MainWindow(Adw.ApplicationWindow, Sidebar, DynamicPage):
    """Main application window."""

    def __init__(self, **kwargs) -> None:  # type: ignore[no-untyped-def]  # noqa: D107
        Adw.ApplicationWindow.__init__(self, **kwargs)

        # Is installed BleachBit
        self.IS_INSTALLED_BLEACHBIT: bool = False
        self.check_installed_bleachbit()

        # List of all disk partitions and their details
        self.BTRFS_PARTITIONS_LIST: list[dict[str, str | float]] = []
        self.update_info_btrfs_partitions()

        # Create the main box
        self.main_vbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=12)
        self.main_vbox.set_hexpand(True)
        self.set_content(self.main_vbox)  # Set the box as the main child of the window

        # Create the header box
        self.header_hbox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=6)
        self.header_hbox.set_hexpand(True)
        self.header = Adw.HeaderBar()
        self.header.set_hexpand(True)
        self.header_hbox.append(self.header)
        self.main_vbox.append(self.header_hbox)

        # Create the content box
        self.content_hbox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=6)
        self.content_hbox.set_margin_top(12)
        self.content_hbox.set_margin_start(12)
        self.content_hbox.set_margin_end(12)
        self.content_hbox.set_margin_bottom(12)
        self.content_hbox.set_hexpand(True)
        self.main_vbox.append(self.content_hbox)

        # Create command for run gui applications as administrator
        self.gui_as_root_command = ["pkexec", "env"] + [
            f"{key}={value}"
            for key, value in os.environ.copy().items()
            if key in ["WAYLAND_DISPLAY", "XDG_RUNTIME_DIR", "DISPLAY", "XAUTHORITY"]
        ]

        # Init mixins
        Sidebar.__init__(self)
        DynamicPage.__init__(self)

        # Render content for the Cleaning button
        self.on_btn_cleaning(None)

    def simple_alert(self, message: str, detail: str, buttons: list[str]) -> None:
        """Simple Alert."""
        dialog = Gtk.AlertDialog(
            modal=True,
            message=message,
            detail=detail,
            buttons=buttons,
        )
        dialog.show(parent=self)

    def check_installed_bleachbit(self) -> None:
        """Check if BleachBit is installed on the user's computer."""
        # Flags for proper I/O handling
        flags = Gio.SubprocessFlags.STDOUT_PIPE | Gio.SubprocessFlags.STDERR_PIPE
        # Create commands
        command_string = "rpm -q bleachbit"
        command_args = shlex.split(command_string)
        # Create the subprocess
        try:
            process = Gio.Subprocess.new(command_args, flags)
            # Run synchronously, send optional input, get output
            success, stdout_buf, stderr_buf = process.communicate_utf8()
            if success:
                self.IS_INSTALLED_BLEACHBIT = "bleachbit" in stdout_buf
            else:
                self.simple_alert(
                    message=gettext("ERROR"),
                    detail=stderr_buf,
                    buttons=["Cancel"],
                )
        except Exception as err:
            # Log the exception and traceback
            logging.exception("Subprocess ended with an error")
            #
            self.simple_alert(
                message=gettext("ERROR"),
                detail=f"An error occurred:\n{err}",
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
                logging.exception("Mountpoint inaccessible")
                # Handle cases where mountpoints might be inaccessible
                continue
        self.BTRFS_PARTITIONS_LIST = partitions_list
