# app.py
from pathlib import Path
from typing import Optional, Union

import dearpygui.dearpygui as dpg

from genesis.ui.chat.interface import (
    set_chat_interface_settings_window,
    set_chat_interface_window,
)
from genesis.ui.tool_bar import Toolbar


def set_font(
    font_path: Optional[Union[str, Path]] = None,
    font_size: Optional[int] = None,
) -> Union[int, str]:
    # Load the custom font from a TTF file
    default_path = "/usr/share/fonts/adobe-source-code-pro/SourceCodePro-Medium.otf"
    font_path = font_path or default_path
    font_size = font_size or 15

    with dpg.font_registry():
        custom_font = dpg.add_font(font_path, font_size)

    return custom_font


def set_viewport_toolbar() -> None:
    toolbar = Toolbar()
    toolbar.create_toolbar()


def main():
    dpg.create_context()

    custom_font = set_font()

    set_viewport_toolbar()

    set_chat_interface_window()

    set_chat_interface_settings_window()

    # Bind the custom font to the text items with tags "chat_log" and "input"
    dpg.bind_font(custom_font)

    dpg.create_viewport(title="Custom Title", width=800, height=600)
    dpg.setup_dearpygui()
    dpg.show_viewport()
    dpg.start_dearpygui()
    dpg.destroy_context()


if __name__ == "__main__":
    main()
