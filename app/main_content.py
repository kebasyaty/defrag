"""Right side of the application."""

from __future__ import annotations

__all__ = ("MainContent",)

from gi.repository import Gtk  # pyright: ignore[reportMissingModuleSource]


class MainContent:
    """Main content area."""

    def __init__(self) -> None:  # noqa: D107
        # Create a page for dynamic content
        self.dynamic_page_vbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=6)
        self.dynamic_page_vbox.set_margin_start(30)
        self.dynamic_page_vbox.set_hexpand(True)
        self.content_hbox.append(self.dynamic_page_vbox)

    def clean_dynamic_page(self) -> None:
        """Remove all child elements in `dynamic_page_vbox`."""
        # Observe the children of `dynamic_page_vbox`
        children_model = self.dynamic_page_vbox.observe_children()
        # Iterate through the children of `dynamic_page_vbox`
        for i in range(children_model.get_n_items()):
            child = children_model.get_item(i)
            if isinstance(child, Gtk.Widget):
                self.dynamic_page_vbox.remove(child)
