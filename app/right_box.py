"""Right side of the application."""

from __future__ import annotations

__all__ = ("RightBox",)

from gi.repository import Gtk  # pyright: ignore[reportMissingModuleSource]


class RightBox:
    """Switchable content with basic functionality."""

    def __init__(self) -> None:  # noqa: D107
        # Create a right vertical box
        self.right_vbox = Gtk.Box.new(orientation=Gtk.Orientation.VERTICAL, spacing=6)
        self.right_vbox.set_hexpand(True)
        self.content_hbox.append(self.right_vbox)

        # Create a box for current content
        self.page_right_box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=6)
        self.page_right_box.set_margin_start(24)
        self.page_right_box.set_hexpand(True)
        self.right_vbox.append(self.page_right_box)

    def clean_page_right_box(self) -> None:
        """Remove all child elements in `page_right_box`."""
        # Observe the children of `page_right_box`
        children_model = self.page_right_box.observe_children()
        # Iterate through the children of `page_right_box`
        for i in range(children_model.get_n_items()):
            child = children_model.get_item(i)
            if isinstance(child, Gtk.Widget):
                self.page_right_box.remove(child)
