"""Main Window."""

from __future__ import annotations

__all__ = ("MainWindow",)

from typing import Any

from gi.repository import Gtk  # pyright: ignore[reportMissingModuleSource]


class MainWindow(Gtk.ApplicationWindow):
    """Main Window."""

    def __init__(self, **kwargs) -> None:  # type: ignore[no-untyped-def]  # noqa: D107
        super().__init__(**kwargs)

        # Create the main horizontal box
        main_hbox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=12)
        main_hbox.set_margin_top(12)
        main_hbox.set_margin_start(6)
        main_hbox.set_margin_end(6)
        main_hbox.set_margin_bottom(6)
        self.set_child(main_hbox)  # Set the box as the main child of the window

        # Create a left vertical box
        left_vbox = Gtk.Box.new(orientation=Gtk.Orientation.VERTICAL, spacing=6)
        main_hbox.append(left_vbox)

        # Create a right vertical box
        self.right_vbox = Gtk.Box.new(orientation=Gtk.Orientation.VERTICAL, spacing=6)
        main_hbox.append(self.right_vbox)

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

        # Create a pages for right vertical box
        self.page_health = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=6)
        self.page_health.append(Gtk.Label(label="Checking the integrity of HDD|SSD"))
        self.page_health.set_visible(True)
        self.right_vbox.append(self.page_health)
        #
        self.page_cleaning = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=6)
        self.page_cleaning.append(Gtk.Label(label="cleaning"))
        self.page_cleaning.set_visible(False)
        self.right_vbox.append(self.page_cleaning)
        #
        self.page_analysis = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=6)
        self.page_analysis.append(Gtk.Label(label="Analysis file fragmentation"))
        self.page_analysis.set_visible(False)
        self.right_vbox.append(self.page_analysis)
        #
        self.page_defrag = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=6)
        self.page_defrag.append(Gtk.Label(label="Defragmentation"))
        self.page_defrag.set_visible(False)
        self.right_vbox.append(self.page_defrag)

    def on_btn_health(self, widget: Any) -> None:
        """Handler for a Health button."""
        self.page_cleaning.set_visible(False)
        self.page_analysis.set_visible(False)
        self.page_defrag.set_visible(False)
        self.page_health.set_visible(True)
        return

    def on_btn_cleaning(self, widget: Any) -> None:
        """Handler for a Cleaning button."""
        self.page_health.set_visible(False)
        self.page_analysis.set_visible(False)
        self.page_defrag.set_visible(False)
        self.page_cleaning.set_visible(True)
        return

    def on_btn_analysis(self, widget: Any) -> None:
        """Handler for a Assess button."""
        self.page_health.set_visible(False)
        self.page_cleaning.set_visible(False)
        self.page_defrag.set_visible(False)
        self.page_analysis.set_visible(True)
        return

    def on_btn_defrag(self, widget: Any) -> None:
        """Handler for a Defrag button."""
        self.page_health.set_visible(False)
        self.page_cleaning.set_visible(False)
        self.page_analysis.set_visible(False)
        self.page_defrag.set_visible(True)
        return
