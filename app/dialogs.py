"""Custom Dialogs."""

from __future__ import annotations

__all__ = ("SpinnerDialog",)

from gi.repository import Adw, Gtk


class SpinnerDialog(Gtk.Dialog):
    """Custom dialog with (progress bar) Spinner."""

    def __init__(self, parent):  # noqa: D107
        super().__init__(
            title="Starting operation",
            transient_for=parent,
            modal=True,
            deletable=False,
        )
        self.set_default_size(300, 100)

        # Get the content area
        content_area = self.get_content_area()

        # Add a top label
        self.top_label = Gtk.Label(
            label="The operation will take some time.",
            halign=Gtk.Align.CENTER,
            margin_top=24,
        )
        content_area.append(self.top_label)

        # Add the (progress bar) Spinner
        self.progressbar_spinner = Adw.Spinner(
            halign=Gtk.Align.CENTER,
            width_request=48,
            height_request=48,
            margin_top=24,
        )
        content_area.append(self.progressbar_spinner)

        # Add a bottom label
        self.bottom_label = Gtk.Label(
            label="Please wait...",
            halign=Gtk.Align.CENTER,
            margin_top=24,
        )
        content_area.append(self.bottom_label)

        # Add an "Abort" button
        self.add_button("Abort", Gtk.ResponseType.CANCEL)
        self.connect("response", self.on_response)

    def on_response(self, dialog, response) -> None:
        """Handle button response."""
        if response == Gtk.ResponseType.CANCEL:
            # Stopping the subprocess
            self.destroy()
