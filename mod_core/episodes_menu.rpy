screen episode(episode):
    frame:
        xysize (1370, 250)
        background Frame("images/interface/panel.png")

        frame:
            pos (38, 48)
            xysize (154, 154)
            background "#a2a2a2"

        frame:
            pos (40, 50)
            xysize (150, 150)
            background Frame(episode.icon)

        text _(episode.name):
            size 80
            pos (210, 40)
            font "font/russia.ttf"
            color "#fff"

        default has_link = (episode.author_link is None) == False
        button:
            xpos 210
            yalign 1.0
            yoffset -40
            text _("Автор: [episode.author]"):
                size 60
                font "font/russia.ttf"
                color "#979797"
                if has_link:
                    hover_underline True
                    hover_color "#285999"
            if has_link:
                action OpenURL(episode.author_link)
        
        text _("Версия: [episode.version]"):
            xalign 1.0
            yalign 1.0
            offset (-280, -40)
            size 60
            font "font/russia.ttf"
            color "#979797"

        frame:   
            style_prefix "main_menu"
            xysize (230, 50)
            align (1.0, 1.0)
            offset (-20, -60)
            background Null() 
            button:
                background Frame("interface/main_meny/plaska.png")
                text _("Запустить"):
                    xoffset -10
                at filepic_but
                xsize 230
                action [ Stop("music"), Start(episode.start_label) ]

screen mod_episodes():
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
            spacing 46
            xsize 1400

        for mod_episode in Mod.episodes.episodes:
            use episode(mod_episode)


    vbar:
        value YScrollValue("autor")
        xpos 1600
        yalign 0.5
        xsize 20
        ysize 800
        at for_yes_no_10

    text _("Эпизоды"):
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