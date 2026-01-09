# Defrag - HDD/SSD defragmentation with BTRFS file system.
# Copyright (c) 2025 Gennady Kostyunin
# SPDX-License-Identifier: GPL-3.0-or-later
"""Left side of the application."""

from __future__ import annotations

__all__ = ("Sidebar",)


from typing import Any

from gi.repository import Gtk

from defrag.translator import _


class Sidebar:
    """Buttons of menu on the left side of the applicatio."""

    def __init__(self) -> None:  # noqa: D107
        # Create Sidebar box
        self.sidebar_vbox = Gtk.Box(
            orientation=Gtk.Orientation.VERTICAL,
            spacing=6,
            halign=Gtk.Align.START,
        )
        self.main_content_hbox.append(self.sidebar_vbox)

        # Create a Cleaning button
        self.btn_cleaning = Gtk.Button(name="btn_cleaning", sensitive=False)
        btn_cleaning_content_box = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=6)
        btn_cleaning_icon = Gtk.Image.new_from_icon_name("user-trash-symbolic")
        btn_cleaning_label = Gtk.Label(label=_("Cleaning"))
        btn_cleaning_content_box.append(btn_cleaning_icon)
        btn_cleaning_content_box.append(btn_cleaning_label)
        self.btn_cleaning.set_child(btn_cleaning_content_box)
        self.btn_cleaning.connect("clicked", self._on_sidebar_btn_cleaning)
        self.sidebar_vbox.append(self.btn_cleaning)

        # Create a Health button
        self.btn_health = Gtk.Button(name="btn_health")
        btn_health_content_box = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=6)
        btn_health_icon = Gtk.Image.new_from_icon_name("security-medium-rtl-symbolic")
        btn_health_label = Gtk.Label(label=_("Health"))
        btn_health_content_box.append(btn_health_icon)
        btn_health_content_box.append(btn_health_label)
        self.btn_health.set_child(btn_health_content_box)
        self.btn_health.connect("clicked", self._on_sidebar_btn_health)
        self.sidebar_vbox.append(self.btn_health)

        # Create a Analysis button
        self.btn_analysis = Gtk.Button(name="btn_analysis")
        btn_analysis_content_box = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=6)
        btn_analysis_icon = Gtk.Image.new_from_icon_name("applications-science-symbolic")
        btn_analysis_label = Gtk.Label(label=_("Analysis"))
        btn_analysis_content_box.append(btn_analysis_icon)
        btn_analysis_content_box.append(btn_analysis_label)
        self.btn_analysis.set_child(btn_analysis_content_box)
        self.btn_analysis.connect("clicked", self._on_sidebar_btn_analysis)
        self.sidebar_vbox.append(self.btn_analysis)

        # Create a Defrag button
        self.btn_defrag = Gtk.Button(name="btn_defrag")
        btn_defrag_content_box = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=6)
        btn_defrag_icon = Gtk.Image.new_from_icon_name("preferences-system-symbolic")
        btn_defrag_label = Gtk.Label(label=_("Defrag"))
        btn_defrag_content_box.append(btn_defrag_icon)
        btn_defrag_content_box.append(btn_defrag_label)
        self.btn_defrag.set_child(btn_defrag_content_box)
        self.btn_defrag.connect("clicked", self._on_sidebar_btn_defrag)
        self.sidebar_vbox.append(self.btn_defrag)

    def unlock_buttons_to_sidebar(self, active_button_name: str) -> None:
        """Unlock all buttons on sidebar and lock active button."""
        # Observe the children of `sidebar_vbox`
        children_model = self.sidebar_vbox.observe_children()
        # Iterate through the children of `sidebar_vbox`
        for idx in range(children_model.get_n_items()):
            child = children_model.get_item(idx)
            if isinstance(child, Gtk.Button):
                child.set_sensitive(True)
        # Lock active button
        self.__dict__[active_button_name].set_sensitive(False)

    def _on_sidebar_btn_cleaning(self, widget: Any) -> None:
        """Handler for a Cleaning button."""
        # Unlock all buttons on sidebar and lock active button
        self.unlock_buttons_to_sidebar(active_button_name=self.btn_cleaning.get_name())
        # Check if BleachBit is installed on the user's computer
        if not self.IS_INSTALLED_BLEACHBIT:
            err_mag = _("To clean the system,\n" + "you need to install the BleachBit application.")
            installation_list = [
                "# On Debian, Ubuntu, Mint",
                "sudo apt install bleachbit",
                "# On Fedora, CentOS, RHEL",
                "sudo dnf install bleachbit",
                "# On Arch Linux",
                "sudo pacman -S bleachbit",
                "# On OpenSUSE",
                "sudo zypper install bleachbit",
                "# On Alpine Linux",
                "sudo apk add bleachbit",
            ]
            installation_str = "\n".join(installation_list)
            # Raise a modal window with an error message
            self.sync_alert_dialog(
                message=_("Warning"),
                detail=f"{err_mag}\n\n{installation_str}",
                buttons=["OK"],
            )
        # Create a box for manage the service
        page_service_vbox = Gtk.Box(
            orientation=Gtk.Orientation.VERTICAL,
            spacing=6,
            halign=Gtk.Align.START,
        )
        # add button `btn_user_bleachbit_run`
        btn_user_bleachbit_run = self.create_btn_run(
            label=_("Run BleachBit as user"),
            is_sensitive=self.IS_INSTALLED_BLEACHBIT,  # pyrefly: ignore[bad-argument-type]
        )
        btn_user_bleachbit_run.connect(
            "clicked",
            self._on_run_async_subprocess,
            "bleachbit",
            False,
        )
        page_service_vbox.append(btn_user_bleachbit_run)
        # add button `btn_admin_bleachbit_run`
        btn_admin_bleachbit_run = self.create_btn_run(
            label=_("Run BleachBit as administrator"),
            is_sensitive=self.IS_INSTALLED_BLEACHBIT,  # pyrefly: ignore[bad-argument-type]
        )
        btn_admin_bleachbit_run.connect(
            "clicked",
            self._on_run_async_subprocess,
            f"{self.gui_as_root_command} bleachbit",
            False,
        )
        page_service_vbox.append(btn_admin_bleachbit_run)
        # Add content to `page_vbox`
        self.add_content_to_page(
            title_page=_("Cleaning"),
            description_page=_(
                "Free up disk space and maintain privacy.\n" + "The BleachBit application is used for this task.",
            ),
            page_service_box=page_service_vbox,
        )

    def _on_sidebar_btn_health(self, widget: Any) -> None:
        """Handler for a Health button."""
        # Unlock all buttons on sidebar and lock active button
        self.unlock_buttons_to_sidebar(active_button_name=self.btn_health.get_name())
        # Create a box for manage the service
        page_service_vbox = Gtk.Box(
            orientation=Gtk.Orientation.VERTICAL,
            spacing=6,
        )
        # add button `btn_run`
        btn_run = self.create_btn_run(label=_("Run check health"))
        btn_run.connect("clicked", self._on_run_async_subprocess, "ls -l")
        page_service_vbox.append(btn_run)
        # Add content to `fresh_page_vbox`
        self.add_content_to_page(
            title_page=_("Checking the integrity of HDD|SSD"),
            description_page=_(
                "Integrity check of the Btrfs file system,\n"
                + "which sequentially reads all data and metadata,\n"
                + "verifies their checksums and,\n"
                + "in the case of a multi-disk array (RAID),\n"
                + "automatically restores damaged blocks using redundant copies,\n"
                + "detecting and correcting errors without stopping the file system.\n"
                + "This is an important tool for maintaining Btrfs health,\n"
                + "especially in redundant configurations.",
            ),
            page_service_box=page_service_vbox,
        )

    def _on_sidebar_btn_analysis(self, widget: Any) -> None:
        """Handler for a Analysis button."""
        # Unlock all buttons on sidebar and lock active button
        self.unlock_buttons_to_sidebar(active_button_name=self.btn_analysis.get_name())
        # Create a box for manage the service
        page_service_vbox = Gtk.Box(
            orientation=Gtk.Orientation.VERTICAL,
            spacing=6,
        )
        # add button `btn_run`
        btn_run = self.create_btn_run(label=_("Run analysis"))
        btn_run.connect("clicked", self._on_run_async_subprocess, "ls -l")
        page_service_vbox.append(btn_run)
        # Add content to `fresh_page_vbox`
        self.add_content_to_page(
            title_page=_("Analysis a files fragmentation"),
            description_page=_("Assess the overall state of file fragmentation."),
            page_service_box=page_service_vbox,
        )

    def _on_sidebar_btn_defrag(self, widget: Any) -> None:
        """Handler for a Defrag button."""
        # Unlock all buttons on sidebar and lock active button
        self.unlock_buttons_to_sidebar(active_button_name=self.btn_defrag.get_name())
        # Create a box for manage the service
        page_service_vbox = Gtk.Box(
            orientation=Gtk.Orientation.VERTICAL,
            spacing=6,
        )
        # add button `btn_run`
        btn_run = self.create_btn_run(label=_("Run defrag"))
        btn_run.connect("clicked", self._on_run_async_subprocess, "ls -l")
        page_service_vbox.append(btn_run)
        # Add content to `fresh_page_vbox`
        self.add_content_to_page(
            title_page=_("Defragmentation"),
            description_page=_("Optimize partitions formatted with the BtrFS file system."),
            page_service_box=page_service_vbox,
        )
