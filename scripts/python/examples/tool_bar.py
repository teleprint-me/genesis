# examples/tool_bar.py
import dearpygui.dearpygui as dpg


def on_click_button(sender, app_data, user_data):
    print(user_data)


def main():
    dpg.create_context()

    with dpg.viewport_menu_bar():
        dpg.add_menu_item(
            label="Button 1", user_data="button_1", callback=on_click_button
        )
        dpg.add_menu_item(
            label="Button 2", user_data="button_2", callback=on_click_button
        )

    dpg.create_viewport(title="Custom Title", width=800, height=600)
    dpg.setup_dearpygui()
    dpg.show_viewport()
    dpg.start_dearpygui()
    dpg.destroy_context()


if __name__ == "__main__":
    main()
