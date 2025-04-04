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
    f "IM A GAY MAN"
    fr "fr"