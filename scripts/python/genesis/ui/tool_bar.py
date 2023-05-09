# genesis/ui/tool_bar.py
import dearpygui.dearpygui as dpg

from genesis.ui import toggle_visibility


class Toolbar:
    def __init__(self):
        self.menu_window = None
        self.settings_window = None
        self.debug_window = None

    def create_toolbar(self):
        with dpg.viewport_menu_bar():
            dpg.add_menu_item(
                label="Menu",
                user_data="toggle_menu",
                callback=self.open_menu,
            )
            dpg.add_menu_item(
                label="Settings",
                user_data="toggle_settings",
                callback=self.open_settings,
            )
            dpg.add_menu_item(
                label="Debug",
                user_data="toggle_debug",
                callback=self.open_debug_tools,
            )

    def open_menu(self, sender, app_data, user_data):
        if self.menu_window is None:
            with dpg.window(label="Menu Window", autosize=True) as menu_window:
                self.menu_window = menu_window
                dpg.add_button(
                    label="Chat Interface",
                    callback=toggle_visibility,
                    user_data="chat_window",  # Pass the item ID as user_data
                )
                dpg.add_button(
                    label="Chat Settings",
                    callback=toggle_visibility,
                    user_data="chat_settings",
                )
        else:
            toggle_visibility(sender, app_data, self.menu_window)

    def open_settings(self, sender, app_data, user_data):
        if self.settings_window is None:
            with dpg.window(label="Settings Window", autosize=True) as settings_window:
                self.settings_window = settings_window
                # Add settings-related UI components here
        else:
            toggle_visibility(sender, app_data, self.settings_window)

    def open_debug_tools(self, sender, app_data, user_data):
        if self.debug_window is None:
            with dpg.window(label="Debug Tools", autosize=True) as debug_window:
                self.debug_window = debug_window
                dpg.add_button(label="Show Debug", callback=dpg.show_debug)
                dpg.add_button(label="Show Metrics", callback=dpg.show_metrics)
                dpg.add_button(
                    label="Show Item Registry",
                    callback=dpg.show_item_registry,
                )
                dpg.add_button(
                    label="Show Documentation",
                    callback=dpg.show_documentation,
                )
                dpg.add_button(
                    label="Show Style Editor",
                    callback=dpg.show_style_editor,
                )
                dpg.add_button(
                    label="Show Font Manager",
                    callback=dpg.show_font_manager,
                )

        else:
            toggle_visibility(sender, app_data, self.debug_window)
