# genesis/ui/chat/menu_bar.py
import dearpygui.dearpygui as dpg

from genesis.ui import toggle_visibility


def open_chat_history(sender, app_data, user_data):
    # Code to open a chat history file
    pass


def save_chat_history(sender, app_data, user_data):
    # Code to save the current chat history
    pass


def save_chat_history_as(sender, app_data, user_data):
    # Code to save the current chat history with a new file name
    pass


def close_viewport(sender, app_data, user_data):
    # Code to close the viewport
    pass


class ChatMenuBar:
    def __init__(self):
        pass

    def create_chat_menu(self):
        with dpg.menu(label="Chat"):
            dpg.add_menu_item(
                label="Open",
                callback=open_chat_history,
                user_data="open_chat_history",  # Pass the item ID as user_data
            )
            dpg.add_menu_item(
                label="Save",
                callback=save_chat_history,
                user_data="save_chat_history",
            )
            dpg.add_menu_item(
                label="Save as",
                callback=save_chat_history_as,
                user_data="save_chat_history_as",
            )
            dpg.add_menu_item(
                label="Close",
                callback=close_viewport,
                user_data="close_viewport",
            )

    def create_view_menu(self):
        with dpg.menu(label="View"):
            dpg.add_menu_item(
                label="Chat Settings",
                callback=toggle_visibility,
                user_data="chat_settings",
            )
