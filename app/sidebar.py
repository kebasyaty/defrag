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
        sidebar_vbox.add_css_class("colored-box")
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
        self.clean_dynamic_page()
        self.set_title_to_dynamic_page("Checking the integrity of HDD|SSD")

    def on_btn_cleaning(self, widget: Any) -> None:
        """Handler for a Cleaning button."""
        self.clean_dynamic_page()
        self.set_title_to_dynamic_page("Cleaning")

    def on_btn_analysis(self, widget: Any) -> None:
        """Handler for a Analysis button."""
        self.clean_dynamic_page()
        self.set_title_to_dynamic_page("Analysis file fragmentation")

    def on_btn_defrag(self, widget: Any) -> None:
        """Handler for a Defrag button."""
        self.clean_dynamic_page()
        self.set_title_to_dynamic_page("Defragmentation")

    def set_title_to_dynamic_page(self, title: str) -> None:
        """Add Title to `content_page_vbox`."""
        title_label = Gtk.Label()
        title_label.set_markup(f"<b>{title}</b>")
        title_label.set_halign(Gtk.Align.START)
        self.dynamic_page_vbox.append(title_label)
