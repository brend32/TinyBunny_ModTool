init screen link_button(buttontext, link):
    button:
        text buttontext:
            size 50
            font "font/russia.ttf"
            hover_underline True
            hover_color "#285999"
        action OpenURL(link)

screen mod_about():
    style_prefix "pref"

    modal True tag menu
    on "show" action Play("test_five", "sounds/menu/menu-window-4.ogg")
    on "replace" action Play("test_five", "sounds/menu/menu-window-4.ogg")
    add "bg_menu_about" at conf_fon

    viewport id "autor":
        at for_yes_no_10
        draggable True
        mousewheel True
        xsize 1400
        ysize 800
        xalign 0.5
        xoffset -60
        yalign 0.5
        

        has vbox:
            xalign 0.5
            spacing 0
            xsize 1400

        text _("Мод позволяющий легко добавлять свои поделки в игру. На данный момент инструмент поддерживает добавление своих эпизодов, инструментов. Также можно добавлять кнопки в меню игры и меню мода. \n\nДокументацию и примеры можно найти в {a=https://github.com/brend32/TinyBunny_ModTool}{size=+5}GitHub-е{/size}{/a}"):
            size 50
            color "#fff"
            font "font/russia.ttf"

        text _("Также можете написать мне в соцсети для консультации или сотрудничества: "):
            size 50
            color "#fff"
            font "font/russia.ttf"

        vbox:
            xoffset 20
            use link_button("Почта: brend.developer.ukr@gmail.com", 'mailto:brend.developer.ukr@gmail.com')
            use link_button("Instagram: @_brend__", 'https://www.instagram.com/_brend__/')
            use link_button("Steam: id/brend32/", 'https://steamcommunity.com/id/brend32/')
            use link_button("YouTube: _BrenD_", 'https://www.youtube.com/channel/UCATCV8pfte6-lyUy0sjGXUQ')
            use link_button("TikTok: @_brend__", 'https://www.tiktok.com/@_brend__')


    vbar:
        value YScrollValue("autor")
        xpos 1600
        yalign 0.5
        xsize 20
        ysize 800
        at for_yes_no_10

    text _("О моде"):
        at for_yes_no_10
        size 80
        color "#fff"
        xalign 0.5
        ypos 30

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