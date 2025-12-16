"""Left side of the application."""

from __future__ import annotations

__all__ = ("Sidebar",)

from typing import Any

from gi.repository import Gtk  # pyright: ignore[reportMissingModuleSource]


class Sidebar:
    """Buttons of menu on the left side of the applicatio."""

    def __init__(self) -> None:  # noqa: D107
        # Create Sidebar box
        sidebar_vbox = Gtk.Box.new(orientation=Gtk.Orientation.VERTICAL, spacing=6)
        self.content_hbox.append(sidebar_vbox)

        # Create a Health button
        btn_health = Gtk.Button()
        btn_health_content_box = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=6)
        btn_health_icon = Gtk.Image.new_from_icon_name("security-medium-rtl-symbolic")
        btn_health_label = Gtk.Label(label="Health")
        btn_health_content_box.append(btn_health_icon)
        btn_health_content_box.append(btn_health_label)
        btn_health.set_child(btn_health_content_box)
        btn_health.connect("clicked", self.on_btn_health)
        sidebar_vbox.append(btn_health)

        # Create a Cleaning button
        btn_cleaning = Gtk.Button()
        btn_cleaning_content_box = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=6)
        btn_cleaning_icon = Gtk.Image.new_from_icon_name("user-trash-symbolic")
        btn_cleaning_label = Gtk.Label(label="Cleaning")
        btn_cleaning_content_box.append(btn_cleaning_icon)
        btn_cleaning_content_box.append(btn_cleaning_label)
        btn_cleaning.set_child(btn_cleaning_content_box)
        btn_cleaning.connect("clicked", self.on_btn_cleaning)
        sidebar_vbox.append(btn_cleaning)

        # Create a Analysis button
        btn_analysis = Gtk.Button()
        btn_analysis_content_box = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=6)
        btn_analysis_icon = Gtk.Image.new_from_icon_name("applications-science-symbolic")
        btn_analysis_label = Gtk.Label(label="Analysis")
        btn_analysis_content_box.append(btn_analysis_icon)
        btn_analysis_content_box.append(btn_analysis_label)
        btn_analysis.set_child(btn_analysis_content_box)
        btn_analysis.connect("clicked", self.on_btn_analysis)
        sidebar_vbox.append(btn_analysis)

        # Create a Defrag button
        btn_defrag = Gtk.Button()
        btn_defrag_content_box = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=6)
        btn_defrag_icon = Gtk.Image.new_from_icon_name("preferences-system-symbolic")
        btn_defrag_label = Gtk.Label(label="Defrag")
        btn_defrag_content_box.append(btn_defrag_icon)
        btn_defrag_content_box.append(btn_defrag_label)
        btn_defrag.set_child(btn_defrag_content_box)
        btn_defrag.connect("clicked", self.on_btn_defrag)
        sidebar_vbox.append(btn_defrag)

    def on_btn_health(self, widget: Any) -> None:
        """Handler for a Health button."""
        self.add_content_to_dynamic_page(
            title_page="Checking the integrity of HDD|SSD",
            btn_name="Run check health",
            command_args=["ls", "-l"],
        )

    def on_btn_cleaning(self, widget: Any) -> None:
        """Handler for a Cleaning button."""
        self.add_content_to_dynamic_page(
            title_page="Cleaning",
            btn_name="Run cleaning",
            command_args=["ls", "-l"],
        )

    def on_btn_analysis(self, widget: Any) -> None:
        """Handler for a Analysis button."""
        self.add_content_to_dynamic_page(
            title_page="Analysis file fragmentation",
            btn_name="Run analysis",
            command_args=["ls", "-l"],
        )

    def on_btn_defrag(self, widget: Any) -> None:
        """Handler for a Defrag button."""
        self.add_content_to_dynamic_page(
            title_page="Defragmentation",
            btn_name="Run defrag",
            command_args=["ls", "-l"],
        )

    def add_content_to_dynamic_page(
        self,
        title_page: str,
        btn_name: str,
        command_args: list[str],
    ) -> None:
        """Add content to dynamic page."""
        # Remove all child elements in `dynamic_page_vbox`
        self.clean_dynamic_page()
        # Add Title page
        title_label = Gtk.Label()
        title_label.set_markup(f"<b>{title_page}</b>")
        title_label.set_halign(Gtk.Align.START)
        self.dynamic_page_vbox.append(title_label)
        # Add button run
        btn_run = Gtk.Button(label=btn_name, margin_top=24)
        btn_run.connect("clicked", self.on_subprocess_run, command_args)
        self.dynamic_page_vbox.append(btn_run)
        # Create Box for display result info
        display_result_info_box = Gtk.Box(
            orientation=Gtk.Orientation.VERTICAL,
            spacing=6,
            margin_top=24,
        )
        result_info_label = Gtk.Label()
        result_info_label.set_markup("<b>Info:</b>")
        result_info_label.set_halign(Gtk.Align.START)
        display_result_info_box.append(result_info_label)
        result_info_textview = Gtk.TextView()
        self.result_info_textbuffer = result_info_textview.get_buffer()
        display_result_info_box.append(result_info_textview)
        self.dynamic_page_vbox.append(display_result_info_box)
