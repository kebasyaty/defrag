"""Left side of the application."""

from __future__ import annotations

__all__ = ("LeftBox",)

from typing import Any

from gi.repository import Gtk  # pyright: ignore[reportMissingModuleSource]


class LeftBox:
    """Main control buttons."""

    def __init__(self) -> None:  # noqa: D107
        # Create vertical box
        left_vbox = Gtk.Box.new(orientation=Gtk.Orientation.VERTICAL, spacing=6)
        self.main_content_hbox.append(left_vbox)

        # Create a Health button
        btn_health = Gtk.Button()
        btn_health_content_box = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=6)
        btn_health_icon = Gtk.Image.new_from_icon_name("security-medium-rtl-symbolic")
        btn_health_label = Gtk.Label(label="Health")
        btn_health_content_box.append(btn_health_icon)
        btn_health_content_box.append(btn_health_label)
        btn_health.set_child(btn_health_content_box)
        btn_health.connect("clicked", self.on_btn_health)
        left_vbox.append(btn_health)

        # Create a Cleaning button
        btn_cleaning = Gtk.Button()
        btn_cleaning_content_box = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=6)
        btn_cleaning_icon = Gtk.Image.new_from_icon_name("user-trash-symbolic")
        btn_cleaning_label = Gtk.Label(label="Cleaning")
        btn_cleaning_content_box.append(btn_cleaning_icon)
        btn_cleaning_content_box.append(btn_cleaning_label)
        btn_cleaning.set_child(btn_cleaning_content_box)
        btn_cleaning.connect("clicked", self.on_btn_cleaning)
        left_vbox.append(btn_cleaning)

        # Create a Analysis button
        btn_analysis = Gtk.Button()
        btn_analysis_content_box = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=6)
        btn_analysis_icon = Gtk.Image.new_from_icon_name("applications-science-symbolic")
        btn_analysis_label = Gtk.Label(label="Analysis")
        btn_analysis_content_box.append(btn_analysis_icon)
        btn_analysis_content_box.append(btn_analysis_label)
        btn_analysis.set_child(btn_analysis_content_box)
        btn_analysis.connect("clicked", self.on_btn_analysis)
        left_vbox.append(btn_analysis)

        # Create a Defrag button
        btn_defrag = Gtk.Button()
        btn_defrag_content_box = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=6)
        btn_defrag_icon = Gtk.Image.new_from_icon_name("preferences-system-symbolic")
        btn_defrag_label = Gtk.Label(label="Defrag")
        btn_defrag_content_box.append(btn_defrag_icon)
        btn_defrag_content_box.append(btn_defrag_label)
        btn_defrag.set_child(btn_defrag_content_box)
        btn_defrag.connect("clicked", self.on_btn_defrag)
        left_vbox.append(btn_defrag)

    def on_btn_health(self, widget: Any) -> None:
        """Handler for a Health button."""
        self.clean_main_title_box()
        self.clean_content_box()
        self.set_main_title("Checking the integrity of HDD|SSD")

    def on_btn_cleaning(self, widget: Any) -> None:
        """Handler for a Cleaning button."""
        self.clean_main_title_box()
        self.clean_content_box()
        self.set_main_title("Cleaning")

    def on_btn_analysis(self, widget: Any) -> None:
        """Handler for a Analysis button."""
        self.clean_main_title_box()
        self.clean_content_box()
        self.set_main_title("Analysis file fragmentation")

    def on_btn_defrag(self, widget: Any) -> None:
        """Handler for a Defrag button."""
        self.clean_main_title_box()
        self.clean_content_box()
        self.set_main_title("Defragmentation")

    def set_main_title(self, title: str) -> None:
        """Add Title to `main_title_hbox`."""
        title_label = Gtk.Label(label=title)
        title_label.set_halign(Gtk.Align.CENTER)
        self.main_title_vbox.append(title_label)

    def clean_main_title_box(self) -> None:
        """Remove all child elements in `main_title_hbox`."""
        # Observe the children of `main_title_hbox`
        children_model = self.main_title_vbox.observe_children()
        # Iterate through the children of `main_title_hbox`
        for i in range(children_model.get_n_items()):
            child = children_model.get_item(i)
            if isinstance(child, Gtk.Widget):
                self.main_title_vbox.remove(child)
