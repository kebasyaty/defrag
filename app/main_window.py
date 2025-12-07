"""Main Window."""

from __future__ import annotations

__all__ = ("MainWindow",)

from gi.repository import Gtk  # pyright: ignore[reportMissingModuleSource]

from app.left_box import LeftBox


class MainWindow(Gtk.ApplicationWindow, LeftBox):
    """Main Window."""

    def __init__(self, **kwargs) -> None:  # type: ignore[no-untyped-def]  # noqa: D107
        Gtk.ApplicationWindow.__init__(self, **kwargs)

        # Create the main horizontal box
        self.main_hbox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=12)
        self.main_hbox.set_margin_top(12)
        self.main_hbox.set_margin_start(6)
        self.main_hbox.set_margin_end(6)
        self.main_hbox.set_margin_bottom(6)
        self.set_child(self.main_hbox)  # Set the box as the main child of the window

        LeftBox.__init__(self)

        # Create a right vertical box
        self.right_vbox = Gtk.Box.new(orientation=Gtk.Orientation.VERTICAL, spacing=6)
        self.main_hbox.append(self.right_vbox)

        # Create a content_box
        self.content_box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=6)
        self.right_vbox.append(self.content_box)

    def clean_content_box(self) -> None:
        """Remove all child elements in the content box."""
        # Observe the children of `content_box`
        children_model = self.content_box.observe_children()
        # Iterate through the children of `content_box`
        for i in range(children_model.get_n_items()):
            child = children_model.get_item(i)
            if isinstance(child, Gtk.Widget):
                self.content_box.remove(child)
