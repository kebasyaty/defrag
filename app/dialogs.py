"""Custom Dialogs."""

from __future__ import annotations

__all__ = ("ProgressDialog",)

from gi.repository import Gtk


class ProgressDialog(Gtk.Dialog):
    """Custom dialog with progress bar."""

    def __init__(self, parent):  # noqa: D107
        super().__init__(title="Progress", transient_for=parent, modal=True)
        self.set_default_size(300, 100)

        # Get the content area
        content_area = self.get_content_area()

        # Add a label
        self.label = Gtk.Label(label="Starting operation...")
        content_area.append(self.label)

        # Add the progress bar
        self.progressbar = Gtk.ProgressBar()
        self.progressbar.set_fraction(0.0)
        self.progressbar.set_show_text(True)
        content_area.append(self.progressbar)

        # Add an "Abort" button
        self.add_button("Abort", Gtk.ResponseType.CANCEL)
        self.connect("response", self.on_response)

    def on_response(self, dialog, response) -> None:
        """Handle button response."""
        if response == Gtk.ResponseType.CANCEL:
            print("Operation aborted by user.")  # noqa: T201
            # Stopping the subprocess
            self.destroy()
