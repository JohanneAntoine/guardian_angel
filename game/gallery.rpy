init python:
    g = Gallery()
    g.transition = fade
    g.navigation = True

    g.button("nadine_a")
    g.image("transformed")
    g.condition("persistent.unlock_1")

    g.button("xyz_a")
    g.image("detectives")
    g.condition("persistent.unlock_2")

    g.button("nadine_b")
    g.image("newlook")
    g.condition("persistent.unlock_3")

    
    #

    g.button("nadine_and_cody")
    g.unlock_image("friendship")

screen gallery():
    tag menu 

    frame:
        xalign 0.5
        yalign 1.0
        default page = 1
        hbox:
            textbutton "Page 1" action SetScreenVariable("page", 1)
            textbutton "Page 2" action SetScreenVariable("page", 2)

    vbox:
        xalign 0.5
        yalign 0.5
        spacing 20
        if page == 1:
            grid 2 2:
                spacing 10
                vbox:
                    add g.make_button(name="nadine_a", locked="thumb_locked", unlocked="transformed_thumbnail")
                vbox:
                    add g.make_button(name="xyz_a", locked="thumb_locked", unlocked="xyz_thumbnail")
                vbox:
                    add g.make_button(name="nadine_b", locked="thumb_locked", unlocked="newlook_thumbnail")
                vbox:
                    add g.make_button(name="nadine_and_cody", locked="thumb_locked", unlocked="newlook_thumbnail")


    #return
    frame:
        xalign 0.0
        yalign 1.0
        xpadding 10
        ypadding 10
        textbutton "Return" action Return()




