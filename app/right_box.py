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
        self.main_content_hbox.append(self.right_vbox)

        # Create a box for current content
        self.content_box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=6)
        self.content_box.set_hexpand(True)
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
