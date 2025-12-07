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
        right_vbox = Gtk.Box.new(orientation=Gtk.Orientation.VERTICAL, spacing=6)
        main_hbox.append(right_vbox)

        # Create buttons for left vertical box
        btn_health = Gtk.Button(label="Health")  # Integrity check
        btn_assess = Gtk.Button(label="Assess")  # Assess file fragmentation
        btn_defrag = Gtk.Button(label="Defrag")  # Run optimization

        # Connect handlers of buttons for left vertical box
        btn_health.connect("clicked", self.on_btn_health)
        btn_assess.connect("clicked", self.on_btn_assess)
        btn_defrag.connect("clicked", self.on_btn_defrag)

        # Add buttons to left vertical box
        left_vbox.append(btn_health)
        left_vbox.append(btn_assess)
        left_vbox.append(btn_defrag)

    def on_btn_health(self, widget: Any) -> None:
        """Handler for a Health button."""
        return

    def on_btn_assess(self, widget: Any) -> None:
        """Handler for a Assess button."""
        return

    def on_btn_defrag(self, widget: Any) -> None:
        """Handler for a Defrag button."""
        return
