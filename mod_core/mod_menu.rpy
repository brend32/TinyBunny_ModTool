init -510 python:
    class ModMenu:

        def __init__(self):
            self.buttons = [
                [ "Эпизоды", ShowMenu("mod_episodes") ],
                [ "Инструменты", ShowMenu("mod_tools") ],
                [ "О моде", ShowMenu("mod_about") ],
                [ "<- Назад", SetVariable("Mod.mod_menu.visible", False) ],
            ]
            self.visible = False

        def insert_menu_button(self, index, name, action):
            self.buttons.insert(index, [name, action])

init -510 python:
    Mod.mod_menu = ModMenu()