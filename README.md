# TinyBunny ModTool
 Инструмент для управления модификациями
 
# Версия 1.1 для Эпизода 4
 
## Установка
1. Скачать архив
2. Распаковать в папку game

Если всё правильно сдално, то в меню игры появится кнопка Моды

![image](https://user-images.githubusercontent.com/35214019/158017880-c32f657a-33be-4b23-ad3e-5f895e85f928.png)

# API
Рекомендации:
* Все содиржимое мода должно находится в папке: mod/название_мода/
* Регестрацию ресурсов проводить в промежутках от -510 до -501 (рекомендованно: -505)

## Добавление кнопки в меню
Функция:
```python
Mod.insert_menu_button(index, name, action)
```
Пример:
```python
Mod.insert_menu_button(2, "Секреты", ShowMenu("secrets"))
```
![image](https://user-images.githubusercontent.com/35214019/158018498-8b09b201-47b6-4a11-97b6-8394909a11dd.png)

## Добавление кнопки в меню мода
Функция:
```python
Mod.mod_menu.insert_menu_button(index, name, action)
```
Пример:
```python
Mod.mod_menu.insert_menu_button(2, "Секреты", ShowMenu("secrets"))
```

![image](https://user-images.githubusercontent.com/35214019/158018518-f35ef59d-3506-45fa-a61a-2d686be4c484.png)

## Добавление эпизода
Функция:
```python
Mod.episodes.add(ModEpisode(name, author, start_label, icon, version, author_link = None))
```
Пример:
```python
Mod.episodes.add(ModEpisode("Антон и Пельмени", "_BrenD_", "anton_pelmeni_start", "mod/anton_pelmeni/images/icon.png", "1.0", "https://www.youtube.com/channel/UCATCV8pfte6-lyUy0sjGXUQ"))
```

![image](https://user-images.githubusercontent.com/35214019/158018551-b169e7b1-eed8-4ac1-bad8-d18f596fe800.png)

## Добавление инструмента
Функция:
```python
Mod.tools.register(ModTool(activate, deactivate, id, name, author, version, icon, author_link = None, label_callback = None))
```
> `activate` - вызывается, когда нужно включить инструмент
> 
> `deactivate` - вызывается, когда нужно выключить инструмент
> 
> `id` - имя папки мода
>
> `label_callback` - вызывается при смене сцены движком RenPy

Пример:
```python
def flags_inspector_activate():
    # Something for tool activation 

def flags_inspector_deactivate():
    # Something for tool deactivation 

def flags_inspector_label_callback(label, context): 
    # Something when label changes

Mod.tools.register(ModTool(flags_inspector_activate, flags_inspector_deactivate, "flags_inspector", "Flags inspector", "_BrenD_", "1.0", "mod/flags_inspector/icon.png", "https://www.youtube.com/channel/UCATCV8pfte6-lyUy0sjGXUQ", flags_inspector_label_callback))
```

## Примеры проектов
* Антон и Пельмени - https://github.com/brend32/Anton_Pelmeni
* Секретное меню - https://github.com/brend32/SecretMenu_TinyBunny
* Flags Inspector - https://github.com/brend32/FlagsInspector

## Обратная связь
* Почта: [brend.developer.ukr@gmail.com](mailto:brend.developer.ukr@gmail.com) 
* Instagram: [@\_brend\_\_](https://www.instagram.com/_brend__/) 
* Steam: [id/brend32/](https://steamcommunity.com/id/brend32/) 
* YouTube: [\_BrenD\_](https://www.youtube.com/channel/UCATCV8pfte6-lyUy0sjGXUQ) 
* TikTok: [@\_brend\_\_](https://www.tiktok.com/@_brend__) 
