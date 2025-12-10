"""Right side of the application."""

from __future__ import annotations

__all__ = ("MainArea",)

from gi.repository import Gtk  # pyright: ignore[reportMissingModuleSource]


class MainArea:
    """Main content area."""

    def __init__(self) -> None:  # noqa: D107
        # Create a right vertical box
        self.main_area_vbox = Gtk.Box.new(orientation=Gtk.Orientation.VERTICAL, spacing=6)
        self.main_area_vbox.set_hexpand(True)
        self.content_hbox.append(self.main_area_vbox)

        # Create a page for dynamic content
        self.content_page_vbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=6)
        self.content_page_vbox.set_margin_start(24)
        self.content_page_vbox.set_hexpand(True)
        self.main_area_vbox.append(self.content_page_vbox)

    def clean_content_page(self) -> None:
        """Remove all child elements in `content_page_vbox`."""
        # Observe the children of `page_vbox`
        children_model = self.content_page_vbox.observe_children()
        # Iterate through the children of `page_vbox`
        for i in range(children_model.get_n_items()):
            child = children_model.get_item(i)
            if isinstance(child, Gtk.Widget):
                self.content_page_vbox.remove(child)
