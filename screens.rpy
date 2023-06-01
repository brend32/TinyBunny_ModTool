









init -1 style default:
    properties gui.text_properties()
    language gui.language

init -1 style input:
    properties gui.text_properties("input", accent=True)
    adjust_spacing False

init -1 style hyperlink_text:
    properties gui.text_properties("hyperlink", accent=True)
    hover_underline True

init -1 style gui_text:
    properties gui.text_properties("interface")


init -1 style button:
    properties gui.button_properties("button")

init -1 style button_text is gui_text:
    properties gui.text_properties("button")
    yalign 0.5


init -1 style label_text is gui_text:
    properties gui.text_properties("label", accent=True)

init -1 style prompt_text is gui_text:
    properties gui.text_properties("prompt")


init -1 style bar:
    ysize gui.bar_size
    left_bar Frame("gui/bar/left.png", gui.bar_borders, tile=gui.bar_tile)
    right_bar Frame("gui/bar/right.png", gui.bar_borders, tile=gui.bar_tile)

init -1 style vbar:
    xsize gui.bar_size
    top_bar Frame("gui/bar/top.png", gui.vbar_borders, tile=gui.bar_tile)
    bottom_bar Frame("gui/bar/bottom.png", gui.vbar_borders, tile=gui.bar_tile)

init -1 style scrollbar:
    ysize gui.scrollbar_size
    base_bar Frame("gui/scrollbar/horizontal_[prefix_]bar.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/scrollbar/horizontal_[prefix_]thumb.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)

init -1 style vscrollbar:
    xsize gui.scrollbar_size
    base_bar Frame("gui/scrollbar/vertical_[prefix_]bar.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/scrollbar/vertical_[prefix_]thumb.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)

init -1 style slider:
    ysize gui.slider_size
    base_bar Frame("gui/slider/horizontal_[prefix_]bar.png", gui.slider_borders, tile=gui.slider_tile)
    thumb "gui/slider/horizontal_[prefix_]thumb.png"

init -1 style vslider:
    xsize gui.slider_size
    base_bar Frame("gui/slider/vertical_[prefix_]bar.png", gui.vslider_borders, tile=gui.slider_tile)
    thumb "gui/slider/vertical_[prefix_]thumb.png"


init -1 style frame:
    padding gui.frame_borders.padding
    background Frame("gui/frame.png", gui.frame_borders, tile=gui.frame_tile)







init -501 screen choice(items):
    style_prefix "choice"

    vbox:
        xalign 0.5
        yalign 0.1
        for i in items:
            textbutton i.caption action i.action


init -501 screen say(who, what):
    zorder 3
    style_prefix "say"
    window:
        id "window"
        if who is not None:
            window:
                id "namebox"
                style "namebox"
                text who id "who" xpos 42
        text what id "what"
    if not renpy.variant("small"):
        add SideImage() xalign 0.0 yalign 1.0

    use qq_menu


init -1 python:
    config.character_id_prefixes.append('namebox')

init -1 style window is default
init -1 style say_label is default
init -1 style say_dialogue is default
init -1 style say_thought is say_dialogue

init -1 style namebox is default
init -1 style namebox_label is say_label

init -1 style window:
    xalign 0.5
    yalign gui.textbox_yalign
    ysize gui.textbox_height
    xsize 1820
    background Frame("images/interface/panel.png", xalign=0.5, yalign=1.0, ysize=gui.textbox_height, xsize=1600)

init -1 style namebox:
    xpos gui.name_xpos
    xanchor gui.name_xalign
    xsize gui.namebox_width
    ypos gui.name_ypos
    ysize gui.namebox_height
    background Frame("images/interface/polosa.png", gui.namebox_borders, tile=gui.namebox_tile, xalign=gui.name_xalign)
    padding gui.namebox_borders.padding

init -1 style say_label:
    properties gui.text_properties("name", accent=True)
    xalign gui.name_xalign
    yalign 0.5
    ypos -45
    xpos 30
    outlines [ (absolute(1), "#000000", absolute(0), absolute(0)) ]

init -1 style say_dialogue:
    properties gui.text_properties("dialogue")
    xpos gui.dialogue_xpos
    xsize gui.dialogue_width
    ypos gui.dialogue_ypos
    line_spacing 1

init 499 image q_base:
    "interface/quick_menu/q06.png"

init 499 image q_adv:
    contains:
        "interface/quick_menu/q06.png"
    contains:
        "interface/quick_menu/q06.png"
        block:
            alpha 1 zoom 1
            linear .5 alpha 0 zoom 1.4
            repeat


init -501 screen qq_menu():
    zorder 5

    key "t" action Language(None)
    key "y" action Language("english")

    hbox:
        yalign 0.99
        xalign 0.5
        spacing 190

        button:
            xsize 54
            ysize 40
            background "interface/quick_menu/q01.png"
            hover_sound "sounds/menu/menu-button-select-new-3-27_dB.ogg"
            activate_sound "sounds/menu/menu-button-push-1_1-14_dB.ogg"
            action ShowMenu("history")
            tooltip (450, __("ИСТОРИЯ"))
            at for_say_buttons

        button:
            xsize 54
            ysize 40
            background "interface/quick_menu/q02.png"
            hover_sound "sounds/menu/menu-button-select-new-3-27_dB.ogg"
            activate_sound "sounds/menu/menu-button-push-1_1-14_dB.ogg"
            action Preference("auto-forward", "toggle")
            tooltip (680, __("АВТО"))
            at for_say_buttons

        button:
            xsize 54
            ysize 40
            background "interface/quick_menu/q03.png"
            hover_sound "sounds/menu/menu-button-select-new-3-27_dB.ogg"
            activate_sound "sounds/menu/menu-button-push-1_1-14_dB.ogg"
            action Skip()
            tooltip (935, __("ПЕРЕМОТКА"))
            at for_say_buttons

        button:
            xsize 54
            ysize 40
            background "interface/quick_menu/q04.png"
            hover_sound "sounds/menu/menu-button-select-new-3-27_dB.ogg"
            activate_sound "sounds/menu/menu-button-push-1_1-14_dB.ogg"
            action ShowMenu("quick_menu")
            tooltip (1170, __("МЕНЮ"))
            at for_say_buttons

        button:
            xsize 54
            ysize 40
            hover_sound "sounds/menu/menu-button-select-new-3-27_dB.ogg"
            activate_sound "sounds/menu/menu-button-push-1_1-14_dB.ogg"
            action ShowMenu('dictionary_scr')
            tooltip (1420, __("СЛОВАРЬ"))

            if not new_words:
                add "q_base":
                    align (.5,.5)
                    at for_say_buttons
            else:
                add "q_base":
                    align (.5,.5)
                    at for_say_buttons_new

    button:
        xpos 1675
        ypos 850
        xsize 54
        ysize 40
        background "interface/quick_menu/q07.png"
        hover_sound "sounds/menu/menu-button-select-new-3-27_dB.ogg"
        activate_sound "sounds/menu/menu-button-push-1_1-14_dB.ogg"
        action HideInterface()
        tooltip (None, __("СКРЫТЬ"))
        at for_say_buttons

    $ tt = GetTooltip()
    if tt:
        if tt[0] is not None:
            text tt[1] yalign 0.99 yoffset 5 xpos tt[0] xanchor 1. size 44
        else:
            text tt[1] xpos 1675 ypos 870 xanchor 1. yanchor .5 size 38






init -501 screen input(prompt):
    style_prefix "input"
    window:
        has vbox:
            xalign gui.dialogue_text_xalign
            xpos gui.dialogue_xpos
            xsize gui.dialogue_width
            ypos gui.dialogue_ypos
        text prompt style "input_prompt"
        input id "input"

init -1 style input_prompt is default

init -1 style input_prompt:
    xalign gui.dialogue_text_xalign
    properties gui.text_properties("input_prompt")

init -1 style input:
    xalign gui.dialogue_text_xalign
    xmaximum gui.dialogue_width







init -501 screen quick_menu():

    zorder 100
    modal True
    style_prefix "quick" tag menu
    on "show" action Play("test_five", "sounds/menu/menu-pause-3.ogg")
    on "replace" action Play("test_five", "sounds/menu/menu-pause-3.ogg")
    add "bg_menu_quick"
    vbox:
        xalign 0.47
        yalign 0.38
        textbutton _("Продолжить"):
            background Null(10, 10)
            action Return()
        textbutton _("Сохранить"):
            action ShowMenu("save")
            sensitive is_save_allowed
        textbutton _("Загрузить"):
            action ShowMenu("load")
        textbutton _("Настройки"):
            action ShowMenu("preferences")
        textbutton _("В меню"):
            action MainMenu(confirm=True)
        textbutton _("Выход"):
            action Quit(confirm=True)
        at qm_elements
    vbox:
        xalign 0.47
        yalign 0.38
        button:
            background "interface/main_meny/plaska.png"
            text _("Продолжить")
            at mm_but
            action Return()
        button:
            background "interface/main_meny/plaska.png"
            text _("Сохранить")
            at mm_but
            action ShowMenu("save")
            sensitive is_save_allowed
        button:
            background "interface/main_meny/plaska.png"
            text _("Загрузить")
            at mm_but
            action ShowMenu("load")
        button:
            background "interface/main_meny/plaska.png"
            text _("Настройки")
            at mm_but
            action ShowMenu("preferences")
        button:
            background "interface/main_meny/plaska.png"
            text _("В меню")
            at mm_but
            action MainMenu(confirm=True)
        button:
            background "interface/main_meny/plaska.png"
            text _("Выход")
            at mm_but
            action Quit(confirm=True)
        at qm_elements

    on "show" action Show("block_screen")
    timer 0.4 action Hide("block_screen")

default -1 quick_menu = True

init -1 style quick_button is default
init -1 style quick_button_text is button_text

init -1 style quick_button:
    properties gui.button_properties("quick_button")
    activate_sound "sounds/menu/menu-button-click-1.ogg"
    hover_sound "sounds/menu/menu-button-select-1.ogg"
    xminimum 250
    yminimum 75

init -1 style quick_button_text:
    properties gui.button_text_properties("quick_button")

init -1 style quick_text:
    properties gui.text_properties("quick_text")
    yalign 0.5

init -1 style quick_textbutton:
    background Null(10, 10)
    xminimum 250
    yminimum 75
    xalign 0.5
    yalign 0.5


init -501 screen black_screen():
    modal True
    add "bg_black":
        at for_black_screen

    timer 1.0 action Start()

transform -1 for_black_screen:
    alpha 0.0
    linear 0.9 alpha 1.0

##############################################################################
#                        Изменнёный участок                                  #
##############################################################################
init -501 screen menu_button(but_text, act):
    frame:   
        style_prefix "main_menu"
        xsize 150
        ysize 60
        background Null()    
        textbutton _(but_text):
            action act
        button:
            background "interface/main_meny/plaska.png"
            text _(but_text)
            at mm_but
            action act

init python:
    config.developer = Mod.developer
##############################################################################


init -501 screen main_menu():

    style_prefix "main_menu" tag menu

    add gui.main_menu_background
    if persistent.animal_unlock[3]:
        add "interface/main_meny/fon_05.png"
    if persistent.animal_unlock[0]:
        add "interface/main_meny/fon_02.png"
    if persistent.animal_unlock[4]:
        add "interface/main_meny/fon_06.png"
    add "menu002_1"
    add "menu002_2"
    add "chastichka_2"
    if persistent.animal_unlock[1]:
        add "interface/main_meny/fon_03.png"
    if persistent.animal_unlock[2]:
        add "interface/main_meny/fon_04.png"
    add "menu001_1"
    add "menu001_2"
    add "chastichka_1_1"
    add "main_menu_bg"
    add "chastichka_1_2"

    add "bg_black" at mm_bg_diss_1to0

    add "[logo!t]" xalign 0.47 yalign 0.09 at mm_elements

##############################################################################
#                        Изменнёный участок                                  #
##############################################################################
    $ config.developer = Mod.developer
    $ Mod.tools.init()

    text _("Mod Tool [Mod.version]"):
        size 40
        xalign 0.57
        yalign 0.22
        color "#fff"
        at mm_elements
    
##############################################################################

    hbox:

        xpos 80
        ypos 100
        button:
            xsize 103
            ysize 192
            background "interface/main_meny/lapka_01.png"
            if preferences.language != None:
                hover_sound "sounds/menu/menu-button-select-3.ogg"
            else:
                hover_sound None
            activate_sound "sounds/menu/language-sellect-1.ogg"
            action Language(None)
            text "РУС":
                xpos 40
                ypos 105
                font "font/razor_k.ttf"
                color "000000"
                size 40
            at mm_but_lang
        at mm_elements
    hbox:

        xpos 180
        ypos 200
        button:
            xsize 103
            ysize 192
            background "interface/main_meny/lapka_02.png"
            if preferences.language != "english":
                hover_sound "sounds/menu/menu-button-select-3.ogg"
            else:
                hover_sound None
            activate_sound "sounds/menu/language-sellect-1.ogg"
            action Language("english")
            text "ENG":
                xpos 35
                ypos 105
                font "font/razor_k.ttf"
                color "000000"
                size 40
            at mm_but_lang
        at mm_elements
    hbox:

        xpos 80
        ypos 300
        button:
            xsize 103
            ysize 192
            background "interface/main_meny/lapka_04.png"
            if preferences.language != "chinese":
                hover_sound "sounds/menu/menu-button-select-3.ogg"
            else:
                hover_sound None
            activate_sound "sounds/menu/language-sellect-1.ogg"
            action Language("chinese")
            at mm_but_lang
        at mm_elements
    hbox:

        xpos 180
        ypos 400
        button:
            xsize 103
            ysize 192
            background "interface/main_meny/lapka_02.png"
            if preferences.language != "italiano":
                hover_sound "sounds/menu/menu-button-select-3.ogg"
            else:
                hover_sound None
            activate_sound "sounds/menu/language-sellect-1.ogg"
            action Language("italiano")
            text "ITA":
                xpos 35
                ypos 105
                font "font/razor_k.ttf"
                color "000000"
                size 40
            at mm_but_lang
        at mm_elements
    hbox:

        xpos 80
        ypos 500
        button:
            xsize 103
            ysize 192
            background "interface/main_meny/lapka_01.png"
            if preferences.language != "turkish":
                hover_sound "sounds/menu/menu-button-select-3.ogg"
            else:
                hover_sound None
            activate_sound "sounds/menu/language-sellect-1.ogg"
            action Language("turkish")
            text "TÜR":
                xalign .5
                xoffset 5
                ypos 105
                font "font/razor_k.ttf"
                color "000000"
                size 40
            at mm_but_lang
        at mm_elements

    vbox:
        xalign 0.47
        yalign 0.4
##############################################################################
#                        Изменнёный участок                                  #
##############################################################################
        for value in (Mod.mod_menu.buttons if Mod.mod_menu.visible else Mod.menu_buttons):
            use menu_button(*value)
            pass
##############################################################################
        at mm_elements

    key "game_menu" action Quit(confirm=True)

    if not config.developer:
        on "show" action Show("block_screen")
        timer 3.2 action Hide("block_screen")

    if config.developer:
        use devolver_menu()

init -1 style main_menu_frame is empty
init -1 style main_menu_text is quick_text
init -1 style main_menu_title is main_menu_text
init -1 style main_menu_version is main_menu_text
init -1 style main_menu_button is quick_button
init -1 style main_menu_button_text is quick_button_text
init -1 style main_meny_textbutton is quick_textbutton


init -501 screen devolver_menu():
    if True or config.developer:
        vbox:
            xalign 1.0
            xoffset -20
            yalign 0.0
            yoffset 20
            text "[config.name!t]":
                xalign 1.0
                size 25
                color "#FFFFFF"
                font "font/SaikonoFont.ttf"

            text "[config.version]":
                xalign 1.0
                size 20
                color "#FFFFFF"
                font "font/SaikonoFont.ttf"

        hbox:
            xalign 1.0
            yalign 1.0
            vbox:
                vbox:
                    text "1 день":
                        size 20
                        color "#FFFFFF"
                    button:
                        background "#FFFFFF20"
                        hover_background "#FFFFFF40"
                        ysize 30
                        text "Кухня с запиской" size 20
                        action [Stop('music'), Start('bunny_hall_day1_prepare')]
                    button:
                        background "#FFFFFF20"
                        hover_background "#FFFFFF40"
                        ysize 30
                        text "Варежка висит" size 20
                        action [Stop('music'), Start('main_choose2')]
                    button:
                        background "#FFFFFF20"
                        hover_background "#FFFFFF40"
                        ysize 30
                        text "Репортаж в комнате Оли" size 20
                        action [Stop('music'), Start('bunny_day1_olya_room')]
                    button:
                        background "#FFFFFF20"
                        hover_background "#FFFFFF40"
                        ysize 30
                        text "Камера медленно плыла" size 20
                        action [Stop('music'), Start('staruha1')]

                vbox:
                    text "2 день":
                        size 20
                        color "#FFFFFF"
                    button:
                        background "#FFFFFF20"
                        hover_background "#FFFFFF40"
                        ysize 30
                        text "Пробуждение" size 20
                        action [Stop('music'), Start('day_2')]
                    button:
                        background "#FFFFFF20"
                        hover_background "#FFFFFF40"
                        ysize 30
                        text "Конфета Лисы" size 20
                        action [Stop('music'), Start('dev_night_meet_fox')]
                    button:
                        background "#FFFFFF20"
                        hover_background "#FFFFFF40"
                        ysize 30
                        text "Территория школы" size 20
                        action [Stop('music'), Start('bunny_school_night1')]
                    button:
                        background "#FFFFFF20"
                        hover_background "#FFFFFF40"
                        ysize 30
                        text "Вход в класс" size 20
                        action [Stop('music'), Start('bunny2_school_classroom1')]
                    button:
                        background "#FFFFFF20"
                        hover_background "#FFFFFF40"
                        ysize 30
                        text "Бьeм Семeна" size 20
                        action [Stop('music'), Stop('sound'), Start('bunny_day2_semen')]
                    button:
                        background "#FFFFFF20"
                        hover_background "#FFFFFF40"
                        ysize 30
                        text "Полина или Лиса" size 20
                        action [Stop('music'), Stop('sound'), Start('bunny_day2_polina_or_fox')]
                    button:
                        background "#FFFFFF20"
                        hover_background "#FFFFFF40"
                        ysize 30
                        text "Встреча с гопниками" size 20
                        action [Stop('music'), Stop('sound'), Start('bunny_day2_gop_stop')]
                    button:
                        background "#FFFFFF20"
                        hover_background "#FFFFFF40"
                        ysize 30
                        text "На**й или Маска" size 20
                        action [Stop('music'), Stop('sound'), Start('bunny_day2_mask_dev')]
                    button:
                        background "#FFFFFF20"
                        hover_background "#FFFFFF40"
                        ysize 30
                        text "Счастливая семья" size 20
                        action [Stop('music'), Stop('sound'), Start('bunny2_happy_family_nightmare')]
                    button:
                        background "#FFFFFF20"
                        hover_background "#FFFFFF40"
                        ysize 30
                        text "Гараж" size 20
                        action [Stop('music'), Stop('sound'), Start('bunny2_fox_garage_dev')]
                    button:
                        background "#FFFFFF20"
                        hover_background "#FFFFFF40"
                        ysize 30
                        text "Ночь в комнате" size 20
                        action [Stop('music'), Stop('sound'), Start('bunny2_night_room_anton_table')]
                    button:
                        background "#FFFFFF20"
                        hover_background "#FFFFFF40"
                        ysize 30
                        text "Кошмар с Катей" size 20
                        action [Stop('music'), Stop('sound'), Start('day2_nightmare')]
                    button:
                        background "#FFFFFF20"
                        hover_background "#FFFFFF40"
                        ysize 30
                        text "Финал дня" size 20
                        action [Stop('music'), Stop('sound'), Start('day_2_f')]
                vbox:
                    text "3 день":
                        size 20
                        color "#FFFFFF"
                    button:
                        background "#FFFFFF20"
                        hover_background "#FFFFFF40"
                        ysize 30
                        text "> НАЧАЛО <" size 20
                        action [Stop('music'), Start('d3_0')]
                    button:
                        background "#FFFFFF20"
                        hover_background "#FFFFFF40"
                        ysize 30
                        text "Неделю спустя" size 20
                        action [Stop('music'), Start('dev_day3_week')]
                    button:
                        background "#FFFFFF20"
                        hover_background "#FFFFFF40"
                        ysize 30
                        text "Анкета" size 20
                        action [Stop('music'), Start('dev_day3_anketa')]
                    button:
                        background "#FFFFFF20"
                        hover_background "#FFFFFF40"
                        ysize 30
                        text "Встреча в углу" size 20
                        action [Stop('music'), Start('dev_day3_cornermeet')]
                    button:
                        background "#FFFFFF20"
                        hover_background "#FFFFFF40"
                        ysize 30
                        text "Общение с сестрой" size 20
                        action [Stop('music'), Start('dev_d3_olyatalk')]
                    button:
                        background "#FFFFFF20"
                        hover_background "#FFFFFF40"
                        ysize 30
                        text "Денди" size 20
                        action [Stop('music'), Start('day3_goosehunt')]
                    button:
                        background "#FFFFFF20"
                        hover_background "#FFFFFF40"
                        ysize 30
                        text "Звонок Полины" size 20
                        action [Stop('music'), Start('dev_d3_polinacall')]
                    button:
                        background "#FFFFFF20"
                        hover_background "#FFFFFF40"
                        ysize 30
                        text "Ночь с конфетами" size 20
                        action [Stop('music'), Start('dev_bunny3_candyjumps')]
                    button:
                        background "#FFFFFF20"
                        hover_background "#FFFFFF40"
                        ysize 30
                        text "Суефа" size 20
                        action [Stop('music'), Start('dev_suefa')]

                    button:
                        background "#FFFFFF20"
                        hover_background "#FFFFFF40"
                        ysize 30
                        text "Папка" size 20
                        action [Stop('music'), Start('minigame_case_start')]
                    button:
                        background "#FFFFFF20"
                        hover_background "#FFFFFF40"
                        ysize 30
                        text "Концовка" size 20
                        action [Stop('music'), Start('dev_day3_end_titr')]

            vbox:
                vbox:
                    text "4 день":
                        size 20
                        color "#FFFFFF"
                    button:
                        background "#FFFFFF20"
                        hover_background "#FFFFFF40"
                        ysize 30
                        text "mold.FF's test" size 20
                        action [Stop('music'), Stop('sound'), Start('mold_test')]
                    button:
                        background "#FFFFFF20"
                        hover_background "#FFFFFF40"
                        ysize 30
                        text "> НАЧАЛО <" size 20
                        action [Stop('music'), Start('d4_setup')]
                    button:
                        background "#FFFFFF20"
                        hover_background "#FFFFFF40"
                        ysize 30
                        text "ВОЛЬТРОН - БЯША" size 20
                        action [Stop('music'), Stop('sound'), Start('dev_byasha')]
                    button:
                        background "#FFFFFF20"
                        hover_background "#FFFFFF40"
                        ysize 30
                        text "Спасение Кати" size 20
                        action [Stop('music'), Stop('sound'), Start('dev_d4_save_katya')]
                    button:
                        background "#FFFFFF20"
                        hover_background "#FFFFFF40"
                        ysize 30
                        text "ПОЛИЦЕЙСКИЙ УЧАСТОК" size 20
                        action [Stop('music'), Stop('sound'), Start('dev_d4_police')]
                    button:
                        background "#FFFFFF20"
                        hover_background "#FFFFFF40"
                        ysize 30
                        text "ДОМ ПОЛИНЫ" size 20
                        action [Stop('music'), Stop('sound'), Start('d4_polhouse_begin.dev')]
                    button:
                        background "#FFFFFF20"
                        hover_background "#FFFFFF40"
                        ysize 30
                        text "РОМА" size 20
                        action [Stop('music'), Stop('sound'), Start('d4_polhouse_after.dev')]
                    button:
                        background "#FFFFFF20"
                        hover_background "#FFFFFF40"
                        ysize 30
                        text "ДОМ ПЕТРОВЫХ" size 20
                        action [Stop('music'), Stop('sound'), Start('d4_home.dev')]
                    button:
                        background "#FFFFFF20"
                        hover_background "#FFFFFF40"
                        ysize 30
                        text "ДВОРЕЦ ДЕДА МОРОЗА" size 20
                        action [Stop('music'), Stop('sound'), Start('d4_palace_dev')]
                    button:
                        background "#FFFFFF20"
                        hover_background "#FFFFFF40"
                        ysize 30
                        text "ОТКАЗ 1" size 20
                        action [Stop('music'), Stop('sound'), Start('d4_beasts_choice_refuse')]
                    button:
                        background "#FFFFFF20"
                        hover_background "#FFFFFF40"
                        ysize 30
                        text "ОТКАЗ 2" size 20
                        action [Stop('music'), Stop('sound'), Start('d4_beasts_choice2_refuse')]
                    button:
                        background "#FFFFFF20"
                        hover_background "#FFFFFF40"
                        ysize 30
                        text "ОТКАЗ 3" size 20
                        action [Stop('music'), Stop('sound'), Start('d4_beasts_choice3_refuse')]
                    button:
                        background "#FFFFFF20"
                        hover_background "#FFFFFF40"
                        ysize 30
                        text "УГОЩЕНИЕ" size 20
                        action [Stop('music'), Stop('sound'), Start('d4_beasts_choice_take.dev')]
                    button:
                        background "#FFFFFF20"
                        hover_background "#FFFFFF40"
                        ysize 30
                        text "ПРОБУЖДЕНИЕ" size 20
                        action [Stop('music'), Stop('sound'), Start('d4_wake_up.dev')]
                    button:
                        background "#FFFFFF20"
                        hover_background "#FFFFFF40"
                        ysize 30
                        text "ТИТРЫ" size 20
                        action [Stop('music'), Stop('sound'), Start('d4_ending_bad_needle')]







init -501 screen about_me():


    modal True tag menu
    on "show" action Play("test_five", "sounds/menu/menu-window-4.ogg")
    on "replace" action Play("test_five", "sounds/menu/menu-window-4.ogg")
    add "bg_menu_about" at conf_fon

    viewport id "autor":
        draggable True
        mousewheel True
        xsize 1600
        ysize 900
        xalign 0.5
        yalign 0.5

        has vbox:
            xalign 0.5
            spacing 46
            xsize 1600

        vbox:
            style_group "about"
            xsize 1600
            xalign 0.5
            text _("{size=+10}По мотивам рассказа Дмитрия Мордаса «Зайчик»"):
                xalign 0.5
            at for_yes_no_10

        vbox:
            style_group "about"
            spacing 5
            xsize 1400
            text _("Продюсер:  {size=+10}SAIKONO")
            text _("Сценарист:  {size=+10}Евгений Сокарев")
            text _("Писатели:  {size=+10}Евгений Сокарев, Максим Кабир")
            text _("Художник:  {size=+10}SAIKONO")
            text _("Аутсорс 2D:  {size=+10}Вячеслав Софронов")
            text _("Аутсорс 3D:  {size=+10}Евгений Слушев-SURAFIN")
            text _("Композиторы:  {size=+10}Владимир Булаев, NIKITA KRYUKOV, EL-METALLICO, EICHON, Никита Лагунов, _BLACKSMITH_, DVAR, Степан Корныхин")
            text _("Звуковой дизайн:  {size=+10}N1K-O, SAIKONO,  ЕГОР АПРЕЛЬЦЕВ")
            text _("Геймдизайн:  {size=+10}Евгений Сокарев")
            text _("Программисты:  {size=+10}ДАНИЛ MOLD.FF, RUZURA INTERACTIVE, Носочек")
            text _("Редакторы:  {size=+10}Ольга Апальчук, KURJATEGIJA")
            text _("Корректор:  {size=+10}INSANECHRONOS")
            text _("Скриптер:  {size=+10}DETH, SAIKONO, Хромушка")
            text _("Переводчики:  {size=+10}Aesthetic Dialectic (английский), Kakihara_MasO (китайский), Mizraim (Итальянский), Cansun Coşkun (Турецкий)")
            at for_yes_no_10

        vbox:
            style_group "about"
            spacing 5
            xsize 1500
            text _("{size=+10}АКТЕРЫ ОЗВУЧИВАНИЯ"):
                xalign 0.5
            text ""
            text _("{size=+10}АНДРЕЙ ЯРОСЛАВЦЕВ")
            text _("{size=+10}АЛИЯ НАСЫРОВА")
            text _("{size=+10}БОРИС РЕПЕТУР")
            text _("{size=+10}ВЛАДИМИР ВЕРЕТЕНОВ")
            text _("{size=+10}ЕВА ФИНКЕЛЬШТЕЙН")
            text _("{size=+10}ИРИНА КИРЕЕВА")
            text _("{size=+10}ИГОРЬ СЕМЫКИН")
            text _("{size=+10}КРИСТИНА ШЕРМАН")
            text _("{size=+10}ЛЮДМИЛА ИЛЬИНА")
            text _("{size=+10}МАРГАРИТА КОРШ")
            text _("{size=+10}МАРИЯ ОВЧИННИКОВА")
            text _("{size=+10}МАРИНА  БАКИНА")
            text _("{size=+10}МИХАИЛ ГЛУШКОВСКИЙ")
            text _("{size=+10}ТАИСИЯ ТРИШИНА")
            at for_yes_no_10

        vbox:
            style_group "about"
            spacing 5
            xsize 1500
            text _("ХУДОЖЕСТВЕННЫЕ РУКОВОДИТЕЛИ:  {size=+10}ЕВГЕНИЙ СОКАРЕВ, SAIKONO")
            text _("ЗВУКОРЕЖИССЁ  РЫ:  {size=+10}СЕРГЕЙ \"HOGART\" ПЕТРОВ,  ВИКТОР ВОРОН")
            text _("ЗАПИСЬ ПРОШЛА НА СТУДИЯ ОЗВУЧАНИЯ «RAVENCAT»")
            at for_yes_no_10

    vbar:
        value YScrollValue("autor")
        xpos 1600
        yalign 0.5
        xsize 20
        ysize 900
        at for_yes_no_10

    imagemap:
        ground Null(1920, 1080)
        insensitive Null(1920, 1080)
        idle "interface/preferences/button/05.png"
        hover "interface/preferences/button/05.png"
        selected_idle "interface/preferences/button/05.png"
        selected_hover "interface/preferences/button/05.png"
        alpha True
        at for_yes_no_10

        hotspot (1673,821,108,88):
            hover_sound "sounds/menu/menu-button-select-1.ogg"
            activate_sound "sounds/menu/menu-button-click-1.ogg"
            action Return()
            at filepic_but3

init -1 style about_text:
    font "font/razor_k.ttf"
    color "FFFFFF"
    size 36


init -501 screen save():
    tag menu
    add "bg_black"
    use file_slots(_("Сохранить"))

init -501 screen load():
    tag menu
    add "bg_black"
    use file_slots(_("Загрузить"))

init -501 screen file_slots(title):
    on "show" action Play("test_five", "sounds/menu/menu-save_load-1.ogg")
    on "replace" action Play("test_five", "sounds/menu/menu-save_load-1.ogg")
    add "bg_menu_save_load" at conf_fon

    $ columns = 2
    $ rows = 2

    imagemap:
        ground Null(1920, 1080)
        insensitive Null(1920, 1080)
        idle Null(1920, 1080)
        hover "interface/save_load_menu/16.png"
        selected_idle "interface/save_load_menu/16.png"
        selected_hover "interface/save_load_menu/16.png"
        alpha False
        at for_show_save_load

        hotspot (310,126,415,107):
            action ShowMenu("save")
            sensitive is_save_allowed
            text _("Сохранить"):
                xalign 0.4
                yalign 0.6
                style "text_font_interface"
                size 55
                color "FFFFFF"
                at filepic_elements
            at filepic_but4

        hotspot (310,126,415,107):
            action ShowMenu("save")
            sensitive is_save_allowed
            if renpy.get_screen("load"):
                hover_sound "sounds/menu/menu-button-select-1.ogg"
                activate_sound "sounds/menu/menu-button-click-1.ogg"
            text _("Сохранить"):
                xalign 0.4
                yalign 0.6
                style "text_font_interface"
                size 55
                color "000000"
            at filepic_but4_2

        hotspot (965,126,415,107):
            action ShowMenu("load")
            text _("Загрузить"):
                xalign 0.4
                yalign 0.6
                style "text_font_interface"
                size 55
                color "FFFFFF"
                at filepic_elements
            at filepic_but5

        hotspot (965,126,415,107):
            action ShowMenu("load")
            if renpy.get_screen("save"):
                hover_sound "sounds/menu/menu-button-select-1.ogg"
                activate_sound "sounds/menu/menu-button-click-1.ogg"
            text _("Загрузить"):
                xalign 0.4
                yalign 0.6
                style "text_font_interface"
                size 55
                color "000000"
            at filepic_but5_2

    vbox:
        xpos 897
        ypos 821
        xminimum 100
        yminimum 100
        text FilePageName():
            xalign 0.5
            yalign 0.5
            size 55
            font "font/razor_k.ttf"
        at for_show_save_load

    imagemap:
        ground "interface/save_load_menu/01.png"
        insensitive "interface/save_load_menu/01.png"
        idle "interface/save_load_menu/14.png"
        hover "interface/save_load_menu/14.png"
        alpha True
        at for_show_save_load

        hotspot (1673,821,108,88):
            action Return()
            hover_sound "sounds/menu/menu-button-select-1.ogg"
            activate_sound "sounds/menu/menu-button-click-1.ogg"
            at filepic_but3

        hotspot (724,821,188,88):
            hover_sound "sounds/menu/menu-button-select-1.ogg"
            activate_sound "sounds/menu/menu-button-click-1.ogg"
            if int(FilePageName()) != 1:
                action FilePagePrevious()
            at filepic_but1

        hotspot (986,821,188,88):
            hover_sound "sounds/menu/menu-button-select-1.ogg"
            activate_sound "sounds/menu/menu-button-click-1.ogg"
            action FilePageNext(999)
            at filepic_but2


        for i in range(1, columns * rows + 1):
            if i == 1:
                $ x = 356
                $ y = 275
            elif i == 2:
                $ x = 1034
                $ y = 275
            elif i == 3:
                $ x = 356
                $ y = 573
            elif i == 4:
                $ x = 1034
                $ y = 573

            hotspot (x, y, config.thumbnail_width+6, config.thumbnail_height+6):
                action FileAction(i)

                add FileScreenshot(i):
                    xpos 3
                    ypos 2
                key "save_delete" action FileDelete(i)

            vbox:

                xpos x + config.thumbnail_width + 15
                ypos y + 10
                xsize 140
                ysize 200
                $ file_name = FileSlotName(i, columns * rows)
                $ file_time = FileTime(i, empty=_("Слот пуст"))
                $ save_name = FileSaveName(i)
                $ nomber_of_del = i
                text "[file_time!t]\n[save_name!t]":
                    style "text_font_interface"
                    size 30
                    xalign 0.5

                if file_time != _("Слот пуст"):
                    frame:
                        background Null()
                        yalign 1.0
                        textbutton _("УДАЛИТЬ") at filepic_but:
                            background Null()
                            hover_sound "sounds/menu/delete-1.ogg"
                            activate_sound "sounds/menu/menu-button-click-1.ogg"
                            text_style "text_font_interface"
                            text_size 40
                            text_color "FFFFFF"
                            action FileDelete(nomber_of_del, True)

    key "game_menu" action Return()
    on "show" action Show("block_screen")
    timer 1.0 action Hide("block_screen")

init -1 style text_font_interface:
    font "font/razor_k.ttf"


init -501 screen preferences():
    style_prefix "pref"

    modal True tag menu
    on "show" action Play("test_five", "sounds/menu/menu-window-2.ogg")
    on "replace" action Play("test_five", "sounds/menu/menu-window-2.ogg")
    add "bg_menu_preferences" at conf_fon

    frame:
        background Null()
        style_group "pref"
        at for_yes_no_10

        vbox:
            ypos 150
            xpos 1000
            spacing 50

            hbox:
                xsize 600
                ysize 75

                text _("Громкость"):
                    size 55

                hbox:
                    xalign 1.
                    spacing 50

                    text _("По умолчанию") yalign 1.

                    imagebutton:
                        idle "interface/preferences/button/00.png"
                        action SetMixer("music", 0.795), SetMixer("sfx", 0.795), SetMixer("voice", 1.0)
                        at transform:
                            zoom .75
                            on hover:
                                linear 0.01 xoffset renpy.random.randint(-5,5) yoffset renpy.random.randint(-5,5)
                                linear 0.01 xoffset renpy.random.randint(-5,5) yoffset renpy.random.randint(-5,5)
                                linear 0.01 xoffset renpy.random.randint(-5,5) yoffset renpy.random.randint(-5,5)
                                linear 0.01 xoffset renpy.random.randint(-5,5) yoffset renpy.random.randint(-5,5)
                                linear 0.01 xoffset renpy.random.randint(-5,5) yoffset renpy.random.randint(-5,5)
                                linear 0.01 xoffset renpy.random.randint(-5,5) yoffset renpy.random.randint(-5,5)
                                linear 0.01 xoffset renpy.random.randint(-5,5) yoffset renpy.random.randint(-5,5)
                                linear 0.01 xoffset renpy.random.randint(-5,5) yoffset renpy.random.randint(-5,5)
                                linear 0.01 xoffset renpy.random.randint(-5,5) yoffset renpy.random.randint(-5,5)
                                linear 0.01 xoffset renpy.random.randint(-5,5) yoffset renpy.random.randint(-5,5)
                                linear 0.01 xoffset renpy.random.randint(-5,5) yoffset renpy.random.randint(-5,5)
                                linear 0.01 xoffset renpy.random.randint(-5,5) yoffset renpy.random.randint(-5,5)
                                linear 0.01 xoffset renpy.random.randint(-5,5) yoffset renpy.random.randint(-5,5)
                                linear 0.01 xoffset renpy.random.randint(-5,5) yoffset renpy.random.randint(-5,5)
                                linear 0.01 xoffset renpy.random.randint(-5,5) yoffset renpy.random.randint(-5,5)
                                linear 0.01 xoffset renpy.random.randint(-5,5) yoffset renpy.random.randint(-5,5)
                                linear 0.01 xoffset 0 yoffset 0

            hbox:
                spacing 50
                xsize 600

                text _("Музыка"):
                    ypos 20

                frame:
                    background "interface/preferences/button/panel.png"
                    xalign 1.0
                    bar:
                        xpos 327
                        ypos 28
                        ysize 24
                        xsize 306
                        value Preference("music volume")


            hbox:
                spacing 50
                xsize 600

                text _("Звук"):
                    ypos 20

                frame:
                    background "interface/preferences/button/panel.png"
                    xalign 1.0
                    bar:
                        xpos 327
                        ypos 28
                        ysize 24
                        xsize 306
                        value Preference("sound volume")


            hbox:
                spacing 50
                xsize 600

                text _("Голос"):
                    ypos 20

                frame:
                    background "interface/preferences/button/panel.png"
                    xalign 1.0
                    bar:
                        xpos 327
                        ypos 28
                        ysize 24
                        xsize 306
                        value Preference("voice volume")


            null width 50

            text _("Скорость"):
                size 55

            hbox:
                spacing 50
                xsize 600

                text _("Текст"):
                    ypos 20

                frame:
                    background "interface/preferences/button/panel.png"
                    xalign 1.0
                    bar:
                        xpos 327
                        ypos 28
                        ysize 24
                        xsize 306
                        value Preference("text speed")


            hbox:
                spacing 50
                xsize 600

                text _("Авточтение"):
                    ypos 20

                frame:
                    background "interface/preferences/button/panel.png"
                    xalign 1.0
                    bar:
                        xpos 327
                        ypos 28
                        ysize 24
                        xsize 306
                        value Preference("auto-forward time")



        text _("Режим"):
            xpos 400
            ypos 150
            size 55

        text _("Пропуск"):
            xpos 400
            ypos 590
            size 55

    frame:
        background Null()
        style_prefix "main_menu"
        at for_yes_no_10

        vbox:
            xalign 0.2
            yalign 0.78
            textbutton _("Весь текст"):
                action Preference("skip", "all")
                xsize 350
            textbutton _("Прочитанный"):
                action Preference("skip", "seen")
                xsize 350

        vbox:
            xalign 0.2
            yalign 0.78
            button:
                background Frame("interface/main_meny/plaska.png")
                text _("Весь текст")
                at mm_but
                xsize 350
                action Preference("skip", "all")
            button:
                background Frame("interface/main_meny/plaska.png")
                text _("Прочитанный")
                at mm_but
                xsize 350
                action Preference("skip", "seen")


    frame:
        background Null()
        style_prefix "main_menu"
        at for_yes_no_10

        vbox:
            xalign 0.2
            yalign 0.3
            textbutton _("Оконный"):
                action Preference("display", "window")
                xsize 350
            textbutton _("Полноэкранный"):
                action Preference("display", "fullscreen")
                xsize 350

        vbox:
            xalign 0.2
            yalign 0.3
            button:
                background Frame("interface/main_meny/plaska.png")
                text _("Оконный")
                at mm_but
                xsize 350
                action Preference("display", "window")
            button:
                background Frame("interface/main_meny/plaska.png")
                text _("Полноэкранный")
                at mm_but
                xsize 350
                action Preference("display", "fullscreen")

    imagemap:
        ground Null(1920, 1080)
        insensitive Null(1920, 1080)
        idle "interface/preferences/button/05.png"
        hover "interface/preferences/button/05.png"
        selected_idle "interface/preferences/button/05.png"
        selected_hover "interface/preferences/button/05.png"
        alpha True
        at for_yes_no_10

        hotspot (1673,821,108,88):
            hover_sound "sounds/menu/menu-button-select-1.ogg"
            activate_sound "sounds/menu/menu-button-click-1.ogg"
            action Return()
            at filepic_but3

    key "game_menu" action Return()
    on "show" action Show("block_screen")
    timer 1.0 action Hide("block_screen")

init -1 style pref_text is text
init -1 style pref_slider is gui_slider

init -1 style pref_text:
    font "font/razor_k.ttf"
    color "FFFFFF"
    size 35

init -1 style pref_slider:
    right_bar Null(10, 10)
    left_bar "interface/preferences/button/right_bar.png"
    xsize 300
    xalign 1.0
    thumb None










init -501 screen confirm(message, yes_action, no_action):

    modal True
    zorder 200
    style_prefix "confirm"
    on "show" action Play("test_five", "sounds/menu/menu-settings-1.ogg")
    on "replace" action Play("test_five", "sounds/menu/menu-settings-1.ogg")
    add "bg_menu_yes_no" at conf_fon

    vbox:
        xalign .5
        yalign .4
        spacing 30
        text message style "imagemap_text" ypos -10 text_align 0.5
        at for_yes_no_10
    hbox:
        xalign 0.5
        yalign 0.5
        spacing 100
        textbutton _("Да"):
            text_style "confirm_textbutton"
            background Null(10, 10)
            xsize 250
            ysize 75
            xalign 0.5
            yalign 0.5
            action yes_action
        textbutton _("Нет"):
            text_style "confirm_textbutton"
            background Null(10, 10)
            xsize 250
            ysize 75
            xalign 0.5
            yalign 0.5
            action no_action
        at for_yes_no_10

    hbox:
        xalign 0.5
        yalign 0.5
        spacing 100
        button:
            xsize 250
            ysize 75
            background "interface/main_meny/plaska.png"
            text _("Да") style "confirm_button_text"
            at mm_but
            action yes_action
        button:
            xsize 250
            ysize 75
            background "interface/main_meny/plaska.png"
            text _("Нет") style "confirm_button_text"
            at mm_but
            action no_action
        at for_yes_no_10


    key "game_menu" action no_action
    on "show" action Show("block_screen")
    timer 1.0 action Hide("block_screen")


init -1 style confirm_frame is gui_frame
init -1 style confirm_prompt is gui_prompt
init -1 style confirm_prompt_text is gui_prompt_text
init -1 style confirm_button is gui_medium_button
init -1 style confirm_button_text is gui_medium_button_text

init -1 style confirm_frame:
    background Frame([ "gui/confirm_frame.png", "gui/frame.png"], gui.confirm_frame_borders, tile=gui.frame_tile)
    padding gui.confirm_frame_borders.padding
    xalign .5
    yalign .5

init -1 style confirm_prompt_text:
    text_align 0.5
    layout "subtitle"

init -1 style confirm_button:
    properties gui.button_properties("confirm_button")

init -1 style confirm_button_text:
    properties gui.button_text_properties("confirm_button")
    xalign 0.5
    yalign 0.5
    font "font/razor_k.ttf"
    size 40
    color "000000"
    xoffset -10

init -1 style confirm_textbutton:
    xalign 0.5
    yalign 0.5
    font "font/razor_k.ttf"
    size 40
    color "FFFFFF"
    xoffset -10






init -501 screen skip_indicator():

    zorder 100
    style_prefix "skip"

    frame:

        has hbox:
            spacing 9

        text _("Пропускаю") style "text_font_interface" size gui.notify_text_size color "#000"

        text "▸" at delayed_blink(0.0, 1.0) style "skip_triangle"
        text "▸" at delayed_blink(0.2, 1.0) style "skip_triangle"
        text "▸" at delayed_blink(0.4, 1.0) style "skip_triangle"



transform -1 delayed_blink(delay, cycle):
    alpha .5

    pause delay
    block:

        linear .2 alpha 1.0
        pause .2
        linear .2 alpha 0.5
        pause (cycle - .4)
        repeat


init -1 style skip_frame is empty
init -1 style skip_text is gui_text
init -1 style skip_triangle is skip_text

init -1 style skip_frame:
    ypos gui.skip_ypos
    background Frame("gui/skip.png", gui.skip_frame_borders, tile=gui.frame_tile)
    padding gui.skip_frame_borders.padding

init -1 style skip_text:
    size gui.notify_text_size

init -1 style skip_triangle:

    font "DejaVuSans.ttf"









init -501 screen notify(message):

    zorder 100
    style_prefix "notify"

    frame at notify_appear:
        text "[message!tq]"

    timer 3.25 action Hide('notify')


transform -1 notify_appear:
    on show:
        alpha 0
        linear .25 alpha 1.0
    on hide:
        linear .5 alpha 0.0


init -1 style notify_frame is empty
init -1 style notify_text is gui_text

init -1 style notify_frame:
    ypos gui.notify_ypos

    background Frame("gui/notify.png", gui.notify_frame_borders, tile=gui.frame_tile)
    padding gui.notify_frame_borders.padding

init -1 style notify_text:
    properties gui.text_properties("notify")









init -501 screen nvl(dialogue, items=None):

    window:
        style "nvl_window"

        has vbox:
            spacing gui.nvl_spacing


        if gui.nvl_height:

            vpgrid:
                cols 1
                yinitial 1.0

                use nvl_dialogue(dialogue)

        else:

            use nvl_dialogue(dialogue)



        for i in items:

            textbutton i.caption:
                action i.action
                style "nvl_button"

    add SideImage() xalign 0.0 yalign 1.0


init -501 screen nvl_dialogue(dialogue):

    for d in dialogue:

        window:
            id d.window_id

            has fixed:
                yfit gui.nvl_height is None

            if d.who is not None:

                text d.who:
                    id d.who_id

            text d.what:
                id d.what_id



define -1 config.nvl_list_length = gui.nvl_list_length

init -1 style nvl_window is default
init -1 style nvl_entry is default

init -1 style nvl_label is say_label
init -1 style nvl_dialogue is say_dialogue

init -1 style nvl_button is button
init -1 style nvl_button_text is button_text

init -1 style nvl_window:
    xfill True
    yfill True

    background "gui/nvl.png"
    padding gui.nvl_borders.padding

init -1 style nvl_entry:
    xfill True
    ysize gui.nvl_height

init -1 style nvl_label:
    xpos gui.nvl_name_xpos
    xanchor gui.nvl_name_xalign
    ypos gui.nvl_name_ypos
    yanchor 0.0
    xsize gui.nvl_name_width
    min_width gui.nvl_name_width
    text_align gui.nvl_name_xalign

init -1 style nvl_dialogue:
    xpos gui.nvl_text_xpos
    xanchor gui.nvl_text_xalign
    ypos gui.nvl_text_ypos
    xsize gui.nvl_text_width
    min_width gui.nvl_text_width
    text_align gui.nvl_text_xalign
    layout ("subtitle" if gui.nvl_text_xalign else "tex")

init -1 style nvl_thought:
    xpos gui.nvl_thought_xpos
    xanchor gui.nvl_thought_xalign
    ypos gui.nvl_thought_ypos
    xsize gui.nvl_thought_width
    min_width gui.nvl_thought_width
    text_align gui.nvl_thought_xalign
    layout ("subtitle" if gui.nvl_text_xalign else "tex")

init -1 style nvl_button:
    properties gui.button_properties("nvl_button")
    xpos gui.nvl_button_xpos
    xanchor gui.nvl_button_xalign

init -1 style nvl_button_text:
    properties gui.button_text_properties("nvl_button")


init -501 screen history():

    modal True
    on "show" action Play("test_five", "sounds/menu/menu-window-4.ogg")
    on "replace" action Play("test_five", "sounds/menu/menu-window-4.ogg")

    predict False
    style_prefix "history" tag menu

    add "bg_menu_yes_no" at conf_fon

    text _("История"):
        xpos 800
        ypos 20
        size 60
        color "#FFFFFF"
        style "text_font_interface"
        at for_yes_no_10

    viewport at for_yes_no_10:
        xalign 0.1
        yalign 0.5
        xsize 1500
        ysize 780
        mousewheel True
        yinitial 1.0

        draggable True
        has vbox
        for h in _history_list:
            window:


                has fixed:
                    yfit True

                vbox:
                    if h.who:

                        label h.who:
                            style "history_name"



                            if "color" in h.who_args:
                                text_color h.who_args["color"]

                    $ what = renpy.filter_text_tags(h.what, allow=gui.history_allow_tags)
                    text what
            null height 5
        if not _history_list:
            label _("История диалогов пуста.")


    imagemap:
        ground Null(1920, 1080)
        insensitive Null(1920, 1080)
        idle "interface/preferences/button/05.png"
        hover "interface/preferences/button/05.png"
        selected_idle "interface/preferences/button/05.png"
        selected_hover "interface/preferences/button/05.png"
        alpha True
        at for_yes_no_10

        hotspot (1673,821,108,88):
            hover_sound "sounds/menu/menu-button-select-1.ogg"
            activate_sound "sounds/menu/menu-button-click-1.ogg"
            action Return()
            at filepic_but3



define -1 gui.history_allow_tags = set()


init -1 style history_window is empty

init -1 style history_name is gui_label
init -1 style history_name_text is gui_label_text
init -1 style history_text is gui_text

init -1 style history_text is gui_text

init -1 style history_label is gui_label
init -1 style history_label_text is gui_label_text

init -1 style history_window:
    xfill True
    ysize gui.history_height

init -1 style history_name:
    xpos gui.history_name_xpos
    xanchor gui.history_name_xalign
    ypos gui.history_name_ypos
    xsize gui.history_name_width

init -1 style history_name_text:
    min_width gui.history_name_width
    text_align gui.history_name_xalign
    font "font/russia.ttf"
    size 55

init -1 style history_text:
    xpos gui.history_text_xpos
    ypos gui.history_text_ypos
    xanchor gui.history_text_xalign
    xsize gui.history_text_width
    min_width gui.history_text_width
    text_align gui.history_text_xalign
    layout ("subtitle" if gui.history_text_xalign else "tex")
    color "#FFFFFF"
    font "font/russia.ttf"
    size 50

init -1 style history_label:
    xfill True

init -1 style history_label_text:
    xalign 0.5






init -1 style pref_vbox:
    variant "medium"
    xsize 675




init -501 screen quick_menu():
    variant "touch"

    zorder 100

    hbox:
        style_prefix "quick"

        xalign 0.5
        yalign 1.0

        textbutton _("Назад") action Rollback()
        textbutton _("Пропуск") action Skip() alternate Skip(fast=True, confirm=True)
        textbutton _("Авто") action Preference("auto-forward", "toggle")
        textbutton _("Меню") action ShowMenu()


init -1 style window:
    variant "small"
    background "gui/phone/textbox.png"

init -1 style radio_button:
    variant "small"
    foreground "gui/phone/button/check_[prefix_]foreground.png"

init -1 style check_button:
    variant "small"
    foreground "gui/phone/button/check_[prefix_]foreground.png"

init -1 style nvl_window:
    variant "small"
    background "gui/phone/nvl.png"

init -1 style main_menu_frame:
    variant "small"
    background "gui/phone/overlay/main_menu.png"

init -1 style game_menu_outer_frame:
    variant "small"
    background "gui/phone/overlay/game_menu.png"

init -1 style game_menu_navigation_frame:
    variant "small"
    xsize 510

init -1 style game_menu_content_frame:
    variant "small"
    top_margin 0

init -1 style pref_vbox:
    variant "small"
    xsize 600

init -1 style bar:
    variant "small"
    ysize gui.bar_size
    left_bar Frame("gui/phone/bar/left.png", gui.bar_borders, tile=gui.bar_tile)
    right_bar Frame("gui/phone/bar/right.png", gui.bar_borders, tile=gui.bar_tile)

init -1 style vbar:
    variant "small"
    xsize gui.bar_size
    top_bar Frame("gui/phone/bar/top.png", gui.vbar_borders, tile=gui.bar_tile)
    bottom_bar Frame("gui/phone/bar/bottom.png", gui.vbar_borders, tile=gui.bar_tile)

init -1 style scrollbar:
    variant "small"
    ysize gui.scrollbar_size
    base_bar Frame("gui/phone/scrollbar/horizontal_[prefix_]bar.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/phone/scrollbar/horizontal_[prefix_]thumb.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)

init -1 style vscrollbar:
    variant "small"
    xsize gui.scrollbar_size
    base_bar Frame("gui/phone/scrollbar/vertical_[prefix_]bar.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/phone/scrollbar/vertical_[prefix_]thumb.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)

init -1 style slider:
    variant "small"
    ysize gui.slider_size
    base_bar Frame("gui/phone/slider/horizontal_[prefix_]bar.png", gui.slider_borders, tile=gui.slider_tile)
    thumb "gui/phone/slider/horizontal_[prefix_]thumb.png"

init -1 style vslider:
    variant "small"
    xsize gui.slider_size
    base_bar Frame("gui/phone/slider/vertical_[prefix_]bar.png", gui.vslider_borders, tile=gui.slider_tile)
    thumb "gui/phone/slider/vertical_[prefix_]thumb.png"

init -1 style slider_pref_vbox:
    variant "small"
    xsize None

init -1 style slider_pref_slider:
    variant "small"
    xsize 900


init -501 screen block_screen():
    imagebutton idle "interface/empty_full.png":
        action NullAction()




default -1 forced_pause = False
init -501 screen forced_pause_timer(delay):
    timer delay action [SetVariable("forced_pause", False),Hide('forced_pause_timer')]


label forced_pause_start(delay):
    $ forced_pause = True
    show screen forced_pause_timer(delay)
    return

label forced_pause_loop:
    while renpy.get_screen("forced_pause_timer"):
        $ renpy.pause(.1, hard=True)
    return

init -501 screen forced_timer(delay):
    timer delay action Return()


init -501 screen for_click_to_c():
    imagebutton idle "interface/empty_full.png":
        action Return()


init -501 screen memory_ramka():
    zorder 2
    add "ramka" at qm_elements
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
