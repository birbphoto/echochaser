define f = Character("Finn", color="#ad3232")
define a = Character("Ari", color="#0c8fa0")
define fr = Character("Frazier", color="#8322c4")

image finn = "finn.png"
image ari = "ari.png"
image frazier = "frazier.png"
image bg ilya = "ilya.jpg"
image bg 3dmodel = "3d-model.jpg"

label start:
    show finn at right
    f "finn test"
    show ari
    a "ari test"
    show frazier at left
    fr "gay deer test"
    "clear"
    hide frazier
    "frazier should be hidden now"
    hide finn
    "finn should be hidden now"
    hide ari
    "ari should be hidden now"
    "SHOULD BE CLEAR"

    "backgrounds now"
    show bg 3dmodel with dissolve

    "bg should be shown now"  

    show finn at right with dissolve
    f "im finn ofc ofc"
    fr "fr"

    "testing sound now"
    play sound "incorrect.mp3"
    "WRONGGGG"

    "testing music"
    play music "beethoven.mp3" with fadein
    "you will now hear some slow jazz"
    stop music fadeout 1.0
    f "fuck jazz no longer"
    hide finn with dissolve

    