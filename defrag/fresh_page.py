# Defrag - HDD/SSD defragmentation with BTRFS file system.
# Copyright (c) 2025 Gennady Kostyunin
# SPDX-License-Identifier: GPL-3.0-or-later
#
"""Right side of the application."""

from __future__ import annotations

__all__ = ("FreshPage",)


from gi.repository import Gtk

from defrag.translator import gettext


class FreshPage:
    """An area with dynamically updated content.

    Located to the left of the sidebar.
    """

    def __init__(self) -> None:  # noqa: D107
        # Create a page for dynamic content
        self.fresh_page_vbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=6)
        self.fresh_page_vbox.set_margin_start(30)
        self.fresh_page_vbox.set_hexpand(True)
        self.content_hbox.append(self.fresh_page_vbox)

    def unlock_buttons_to_sidebar(self, active_button_name: str) -> None:
        """Unlock all buttons on sidebar and lock active button."""
        # Observe the children of `sidebar_vbox`
        children_model = self.sidebar_vbox.observe_children()
        # Iterate through the children of `sidebar_vbox`
        for idx in range(children_model.get_n_items()):
            child = children_model.get_item(idx)
            if isinstance(child, Gtk.Button):
                child.set_sensitive(True)
        # Lock active button
        self.__dict__[active_button_name].set_sensitive(False)

    def refreshing_page(self) -> None:
        """Remove all child elements in `fresh_page_vbox`."""
        # Observe the children of `fresh_page_vbox`
        children_model = self.fresh_page_vbox.observe_children()
        # Iterate through the children of `fresh_page_vbox`
        child_list: list[Gtk.Widget] = []
        for idx in range(children_model.get_n_items()):
            child = children_model.get_item(idx)
            if isinstance(child, Gtk.Widget):
                child_list.append(child)
        for child in child_list:
            self.fresh_page_vbox.remove(child)
        # Additionally remove the following keys
        if len(child_list) > 0:
            del self.__dict__["result_info_label"]
            del self.__dict__["result_info_textview"]
            del self.__dict__["display_result_info_vbox"]

    def create_btn_run(
        self,
        label: str,
        icon_name: str = "system-run-symbolic",
        is_sensitive: bool = True,
    ) -> Gtk.Button:
        """Create a start button for the service."""
        btn_content_box = Gtk.Box(
            orientation=Gtk.Orientation.HORIZONTAL,
            halign=Gtk.Align.START,
            spacing=6,
        )
        btn_icon = Gtk.Image.new_from_icon_name(icon_name)
        btn_label = Gtk.Label(label=label)
        btn_content_box.append(btn_icon)
        btn_content_box.append(btn_label)
        btn_run = Gtk.Button(halign=Gtk.Align.START, sensitive=is_sensitive)
        btn_run.set_child(btn_content_box)
        return btn_run

    def add_content_to_fresh_page(
        self,
        title_page: str,
        description_page: str,
        service_box: Gtk.Box,
    ) -> None:
        """Add content to fresh page."""
        # Remove all child elements in `fresh_page_vbox`
        self.refreshing_page()
        # Add Title of page
        title_label = Gtk.Label(halign=Gtk.Align.START)
        title_label.set_markup(f"<b>{title_page}</b>")
        self.fresh_page_vbox.append(title_label)
        # Add description of page
        description_label = Gtk.Label(
            label=description_page,
            halign=Gtk.Align.START,
            margin_top=12,
        )
        self.fresh_page_vbox.append(description_label)
        # Add box for control of service
        service_box.set_margin_top(12)
        self.fresh_page_vbox.append(service_box)
        # Add info box for display result
        self.display_result_info_vbox = Gtk.Box(
            orientation=Gtk.Orientation.VERTICAL,
            spacing=6,
            margin_top=24,
            visible=False,
        )
        # add Label to info box
        self.result_info_label = Gtk.Label(halign=Gtk.Align.START)
        label_str = gettext("INFO")
        self.result_info_label.set_markup(f"<b>{label_str}:</b>")
        self.display_result_info_vbox.append(self.result_info_label)
        # add TextView (Label) to info box
        self.result_info_textview = Gtk.Label(halign=Gtk.Align.START)
        self.display_result_info_vbox.append(self.result_info_textview)
        self.fresh_page_vbox.append(self.display_result_info_vbox)
