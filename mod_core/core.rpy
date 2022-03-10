init -510 python:
    class Core:

        def __init__(self):
            self.menu_buttons = [
                [ "Новая игра", Show("black_screen") ],
                [ "Загрузить", ShowMenu("load") ],
                [ "Настройки", ShowMenu("preferences") ],
                [ "Моды", SetVariable("Mod.mod_menu.visible", True) ],
                [ "Об авторах", ShowMenu("about_me") ],
                [ "Выход", Quit(confirm=False) ],
            ]
            self.developer = False

        def insert_menu_button(self, index, name, action):
            self.menu_buttons.insert(index, [name, action])

        
init -510 python:
    global Mod
    Mod = Core()
