# ui/__init__.py
import dearpygui.dearpygui as dpg


# Toggle Window Visibility
def toggle_visibility(sender, app_data, user_data):
    item_id = user_data
    is_visible = dpg.get_item_state(item_id)["visible"]

    if is_visible:
        dpg.configure_item(item_id, show=False)
    else:
        dpg.configure_item(item_id, show=True)
