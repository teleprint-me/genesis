# chat.py
import dearpygui.dearpygui as dpg
from typing import Union, Optional
from pathlib import Path


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


# Toggle Window Visibility
def toggle_visibility(sender, app_data, user_data):
    item_id = user_data
    is_visible = dpg.get_item_state(item_id)["visible"]

    if is_visible:
        dpg.configure_item(item_id, show=False)
    else:
        dpg.configure_item(item_id, show=True)


# Callback function for the Chat Interface Send button
def on_send_button(sender, app_data, user_data):
    chat_log_id = user_data
    message = dpg.get_value("input")

    if message.strip():  # Check if the message is not empty or just spaces
        dpg.add_text(message, parent=chat_log_id)
        dpg.add_spacer(parent=chat_log_id)
        dpg.set_value("input", "")


# Callback function for the Chat Settings Apply button
def on_apply(sender, app_data, user_data):
    top_k = dpg.get_value(user_data["top_k"])
    top_p = dpg.get_value(user_data["top_p"])
    temperature = dpg.get_value(user_data["temperature"])

    print(f"Model settings updated:")
    print(f"Top-K: {top_k}, Top-P: {top_p}, Temperature: {temperature}")


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


def set_viewport_menu_bar() -> None:
    # Set the Viewport Menu Options
    with dpg.viewport_menu_bar():
        # Set the Chat Menu Options
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
        # Set the View Menu Options
        with dpg.menu(label="View"):
            dpg.add_menu_item(
                label="Chat Interface",
                callback=toggle_visibility,
                user_data="chat_window",  # Pass the item ID as user_data
            )
            dpg.add_menu_item(
                label="Chat Settings",
                callback=toggle_visibility,
                user_data="chat_settings",
            )
            dpg.add_menu_item(
                label="General Settings",
                callback=toggle_visibility,
                user_data="general_settings",
            )
            dpg.add_menu_item(
                label="Debug Tools",
                callback=toggle_visibility,
                user_data="debug_tools",
            )
        # Set the About Dialog


def set_chat_interface_window() -> None:
    with dpg.window(
        label="Chat Interface",
        id="chat_window",
        tag="chat_window",
        width=400,
    ):
        with dpg.child_window(
            height=400,
            width=-1,
            horizontal_scrollbar=True,
            id="chat_log",
            tag="chat_log",  # Added the tag
        ):
            dpg.add_spacer()

        with dpg.group(horizontal=False):
            dpg.add_input_text(
                tag="input",
                width=-1,
                height=100,  # Set a custom height for the multi-line input text widget
                multiline=True,  # Set this to True for multi-line input
                on_enter=True,
                callback=on_send_button,
                user_data="chat_log",
            )
            dpg.add_button(
                label="Send",
                callback=on_send_button,
                user_data="chat_log",
                width=-1,
            )


def set_chat_interface_settings_window() -> None:
    with dpg.window(
        label="Chat Settings",
        id="chat_settings",
        tag="chat_settings",
        width=350,
        pos=(400, 0),
        show=True,
    ):
        dpg.add_text("Mode:")
        mode_id = dpg.add_combo(
            items=["Complete", "Chat", "Insert", "Edit"],
            default_value="Chat",
            width=-1,
        )

        dpg.add_text("Model:")
        model_id = dpg.add_combo(
            items=["text-davinci-003", "gpt-3.5-turbo", "gpt-4"],
            default_value="gpt-4",
            width=-1,
        )

        dpg.add_text("Temperature:")
        temperature_id = dpg.add_slider_float(
            label="",
            default_value=0.75,
            min_value=0,
            max_value=1.0,
            width=-1,
        )

        dpg.add_text("Context Length:")
        context_length_id = dpg.add_slider_int(
            label="",
            default_value=512,
            min_value=1,
            max_value=8096,
            width=-1,
        )

        dpg.add_text("Top-P:")
        top_p_id = dpg.add_slider_float(
            label="",
            default_value=0.9,
            min_value=0.0,
            max_value=1.0,
            width=-1,
        )

        dpg.add_button(
            label="Apply",
            callback=on_apply,
            user_data={
                "mode": mode_id,
                "model": model_id,
                "temperature": temperature_id,
                "context_length": context_length_id,
                "top_p": top_p_id,
            },
            width=-1,
        )


def main():
    dpg.create_context()

    custom_font = set_font()

    set_viewport_menu_bar()

    set_chat_interface_window()

    set_chat_interface_settings_window()

    # Bind the custom font to the text items with tags "chat_log" and "input"
    dpg.bind_font(custom_font)

    dpg.show_font_manager()

    dpg.create_viewport(title="Custom Title", width=800, height=600)
    dpg.setup_dearpygui()
    dpg.show_viewport()
    dpg.start_dearpygui()
    dpg.destroy_context()


if __name__ == "__main__":
    main()
