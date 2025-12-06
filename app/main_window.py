"""Window."""

from __future__ import annotations

__all__ = ("MainWindow",)


from gi.repository import Gtk  # pyright: ignore[reportMissingModuleSource]


class MainWindow(Gtk.ApplicationWindow):
    """Main Window."""

    def __init__(self) -> None:  # noqa: D107
        super().__init__()

        # Create a vertical box
        vbox = Gtk.Box.new(Gtk.Orientation.VERTICAL, 6)  # Spacing of 6 pixels
        self.set_child(vbox)  # Set the box as the main child of the window

        # Create a horizontal box
        hbox = Gtk.Box.new(Gtk.Orientation.HORIZONTAL, 6)
        vbox.append(hbox)  # Add the horizontal box to the vertical box

        # Create some buttons
        button1 = Gtk.Button.new_with_label("Button 1")
        button2 = Gtk.Button.new_with_label("Button 2")
        button3 = Gtk.Button.new_with_label("Button 3")

        # Add buttons to the horizontal box
        hbox.append(button1)
        hbox.append(button2)

        # Add another button directly to the vertical box
        vbox.append(button3)
