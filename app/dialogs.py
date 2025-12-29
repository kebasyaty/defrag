"""Custom Dialogs."""

from __future__ import annotations

__all__ = ("ProgressDialog",)

from gi.repository import Gtk


class ProgressDialog(Gtk.Dialog):
    """Custom dialog with progress bar."""

    def __init__(self, parent):  # noqa: D107
        super().__init__(title="Progress")
        self.set_parent(parent=parent)
        self.add_button("_Cancel", Gtk.ResponseType.CANCEL)
        self.set_default_size(300, 100)

        # Content area
        content_area = self.get_content_area()
        self.label = Gtk.Label(label="Starting operation...")
        content_area.pack_start(self.label, True, True, 10)

        self.progress_bar = Gtk.ProgressBar()
        self.progress_bar.set_fraction(0.0)
        self.progress_bar.set_show_text(True)  # Show percentage text
        content_area.pack_start(self.progress_bar, True, True, 10)

        self.show_all()
