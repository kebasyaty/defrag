"""Left side of the application."""

from __future__ import annotations

__all__ = ("LeftBox",)

from typing import Any

from gi.repository import Gtk  # pyright: ignore[reportMissingModuleSource]


class LeftBox:
    """Main control buttons."""

    def __init__(self) -> None:  # noqa: D107
        # Create a left vertical box
        left_vbox = Gtk.Box.new(orientation=Gtk.Orientation.VERTICAL, spacing=6)
        self.main_hbox.append(left_vbox)

        # Create buttons for left vertical box
        btn_health = Gtk.Button(label="Health")  # Integrity check
        btn_cleaning = Gtk.Button(label="Cleaning")  # cleaning
        btn_analysis = Gtk.Button(label="Analysis")  # Analysis file fragmentation
        btn_defrag = Gtk.Button(label="Defrag")  # Run optimization

        # Connect handlers of buttons for left vertical box
        btn_health.connect("clicked", self.on_btn_health)
        btn_cleaning.connect("clicked", self.on_btn_cleaning)
        btn_analysis.connect("clicked", self.on_btn_analysis)
        btn_defrag.connect("clicked", self.on_btn_defrag)

        # Add buttons to left vertical box
        left_vbox.append(btn_health)
        left_vbox.append(btn_cleaning)
        left_vbox.append(btn_analysis)
        left_vbox.append(btn_defrag)

    def on_btn_health(self, widget: Any) -> None:
        """Handler for a Health button."""
        self.clean_content_box()
        self.title_content_box("Checking the integrity of HDD|SSD")

    def on_btn_cleaning(self, widget: Any) -> None:
        """Handler for a Cleaning button."""
        self.clean_content_box()
        self.title_content_box("cleaning")

    def on_btn_analysis(self, widget: Any) -> None:
        """Handler for a Analysis button."""
        self.clean_content_box()
        self.title_content_box("Analysis file fragmentation")

    def on_btn_defrag(self, widget: Any) -> None:
        """Handler for a Defrag button."""
        self.clean_content_box()
        self.title_content_box("Defragmentation")

    def title_content_box(self, title: str) -> None:
        """Add Title to `content_box`."""
        title_label = Gtk.Label(label=title)
        title_label.set_halign(Gtk.Align.CENTER)
        self.content_box.append(title_label)
