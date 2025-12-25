"""Left side of the application."""

from __future__ import annotations

__all__ = ("Sidebar",)


from typing import Any

from gi.repository import Gtk

from app.translator import gettext


class Sidebar:
    """Buttons of menu on the left side of the applicatio."""

    def __init__(self) -> None:  # noqa: D107
        # Create Sidebar box
        sidebar_vbox = Gtk.Box(
            orientation=Gtk.Orientation.VERTICAL,
            spacing=6,
            halign=Gtk.Align.START,
        )
        self.content_hbox.append(sidebar_vbox)

        # Create a Cleaning button
        self.btn_cleaning = Gtk.Button(sensitive=False)
        btn_cleaning_content_box = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=6)
        btn_cleaning_icon = Gtk.Image.new_from_icon_name("user-trash-symbolic")
        btn_cleaning_label = Gtk.Label(label=gettext("Cleaning"))
        btn_cleaning_content_box.append(btn_cleaning_icon)
        btn_cleaning_content_box.append(btn_cleaning_label)
        self.btn_cleaning.set_child(btn_cleaning_content_box)
        self.btn_cleaning.connect("clicked", self.on_btn_cleaning)
        sidebar_vbox.append(self.btn_cleaning)

        # Create a Health button
        self.btn_health = Gtk.Button()
        btn_health_content_box = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=6)
        btn_health_icon = Gtk.Image.new_from_icon_name("security-medium-rtl-symbolic")
        btn_health_label = Gtk.Label(label=gettext("Health"))
        btn_health_content_box.append(btn_health_icon)
        btn_health_content_box.append(btn_health_label)
        self.btn_health.set_child(btn_health_content_box)
        self.btn_health.connect("clicked", self.on_btn_health)
        sidebar_vbox.append(self.btn_health)

        # Create a Analysis button
        self.btn_analysis = Gtk.Button()
        btn_analysis_content_box = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=6)
        btn_analysis_icon = Gtk.Image.new_from_icon_name("applications-science-symbolic")
        btn_analysis_label = Gtk.Label(label=gettext("Analysis"))
        btn_analysis_content_box.append(btn_analysis_icon)
        btn_analysis_content_box.append(btn_analysis_label)
        self.btn_analysis.set_child(btn_analysis_content_box)
        self.btn_analysis.connect("clicked", self.on_btn_analysis)
        sidebar_vbox.append(self.btn_analysis)

        # Create a Defrag button
        self.btn_defrag = Gtk.Button()
        btn_defrag_content_box = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=6)
        btn_defrag_icon = Gtk.Image.new_from_icon_name("preferences-system-symbolic")
        btn_defrag_label = Gtk.Label(label=gettext("Defrag"))
        btn_defrag_content_box.append(btn_defrag_icon)
        btn_defrag_content_box.append(btn_defrag_label)
        self.btn_defrag.set_child(btn_defrag_content_box)
        self.btn_defrag.connect("clicked", self.on_btn_defrag)
        sidebar_vbox.append(self.btn_defrag)

    def on_btn_cleaning(self, widget: Any) -> None:
        """Handler for a Cleaning button."""
        self.btn_cleaning.set_sensitive(False)
        # Create a box for manage the service
        service_vbox = Gtk.Box(
            orientation=Gtk.Orientation.VERTICAL,
            spacing=6,
            halign=Gtk.Align.START,
        )
        # add button `btn_user_bleachbit_run`
        btn_user_bleachbit_run = Gtk.Button(
            label=gettext("Run BleachBit as user"),
            halign=Gtk.Align.START,
            sensitive=False,
        )
        btn_user_bleachbit_run.connect("clicked", self.on_subprocess_run, ["bleachbit"])
        service_vbox.append(btn_user_bleachbit_run)
        # add button `btn_admin_bleachbit_run`
        btn_admin_bleachbit_run = Gtk.Button(
            label=gettext("Run BleachBit as administrator"),
            halign=Gtk.Align.START,
            sensitive=False,
        )
        btn_admin_bleachbit_run.connect(
            "clicked",
            self.on_subprocess_run,
            [*self.gui_as_root_command, "bleachbit"],
        )
        service_vbox.append(btn_admin_bleachbit_run)
        # Add content to `dynamic_page_vbox`
        self.add_content_to_dynamic_page(
            title_page=gettext("Cleaning"),
            description_page=gettext(
                "Free up disk space and maintain privacy.\n"
                + "The BleachBit application is used for this task.\n"
                + "If this application is not on your computer,\n"
                + "you will be prompted to install it.",
            ),
            service_box=service_vbox,
        )

    def on_btn_health(self, widget: Any) -> None:
        """Handler for a Health button."""
        self.btn_health.set_sensitive(False)
        # Create a box for manage the service
        service_vbox = Gtk.Box(
            orientation=Gtk.Orientation.VERTICAL,
            spacing=6,
        )
        # add button `btn_run`
        btn_run = Gtk.Button(label=gettext("Run check health"))
        btn_run.connect("clicked", self.on_subprocess_run, ["ls", "-l"])
        service_vbox.append(btn_run)
        # Add content to `dynamic_page_vbox`
        self.add_content_to_dynamic_page(
            title_page=gettext("Checking the integrity of HDD|SSD"),
            description_page="???",
            service_box=service_vbox,
        )

    def on_btn_analysis(self, widget: Any) -> None:
        """Handler for a Analysis button."""
        self.btn_analysis.set_sensitive(False)
        # Create a box for manage the service
        service_vbox = Gtk.Box(
            orientation=Gtk.Orientation.VERTICAL,
            spacing=6,
        )
        # add button `btn_run`
        btn_run = Gtk.Button(label=gettext("Run analysis"))
        btn_run.connect("clicked", self.on_subprocess_run, ["ls", "-l"])
        service_vbox.append(btn_run)
        # Add content to `dynamic_page_vbox`
        self.add_content_to_dynamic_page(
            title_page=gettext("Analysis a files fragmentation"),
            description_page="???",
            service_box=service_vbox,
        )

    def on_btn_defrag(self, widget: Any) -> None:
        """Handler for a Defrag button."""
        self.btn_defrag.set_sensitive(False)
        # Create a box for manage the service
        service_vbox = Gtk.Box(
            orientation=Gtk.Orientation.VERTICAL,
            spacing=6,
        )
        # add button `btn_run`
        btn_run = Gtk.Button(label=gettext("Run defrag"))
        btn_run.connect("clicked", self.on_subprocess_run, ["ls", "-l"])
        service_vbox.append(btn_run)
        # Add content to `dynamic_page_vbox`
        self.add_content_to_dynamic_page(
            title_page=gettext("Defragmentation"),
            description_page="???",
            service_box=service_vbox,
        )

    def add_content_to_dynamic_page(
        self,
        title_page: str,
        description_page: str,
        service_box: Gtk.Box,
    ) -> None:
        """Add content to dynamic page."""
        # Remove all child elements in `dynamic_page_vbox`
        self.clean_dynamic_page()
        # Add Title of page
        title_label = Gtk.Label(halign=Gtk.Align.START)
        title_label.set_markup(f"<b>{title_page}</b>")
        self.dynamic_page_vbox.append(title_label)
        # Add description of page
        description_label = Gtk.Label(
            label=description_page,
            halign=Gtk.Align.START,
            margin_top=12,
        )
        self.dynamic_page_vbox.append(description_label)
        # Add a box for manage the service
        service_box.set_margin_top(12)
        self.dynamic_page_vbox.append(service_box)
        # Add info box for display result
        self.display_result_info_vbox = Gtk.Box(
            orientation=Gtk.Orientation.VERTICAL,
            spacing=6,
            margin_top=24,
            visible=False,
        )
        # add Label to info box
        result_info_label = Gtk.Label(halign=Gtk.Align.START)
        result_info_label.set_markup("<b>Info:</b>")
        self.display_result_info_vbox.append(result_info_label)
        # add TextView (Label) to info box
        self.result_info_textview = Gtk.Label(halign=Gtk.Align.START)
        self.display_result_info_vbox.append(self.result_info_textview)
        self.dynamic_page_vbox.append(self.display_result_info_vbox)
