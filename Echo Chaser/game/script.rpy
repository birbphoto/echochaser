define f = Character("Finn", color="#ad3232")
define a = Character("Ari", color="#0c8fa0")
define fr = Character("Frazier", color="#8322c4")

image finn = "finn.png"
image ari = "ari.png"
image frazier = "frazier.png"
image bg ilya = "ilya.jpg"
image bg 3dmodel = "3d-model.jpg"
image bg nyclamp = "nyc.jpg"

transform bounce:
    pause .15
    yoffset 0
    easein .175 yoffset -10
    easeout .175 yoffset 0
    easein .175 yoffset -4
    easeout .175 yoffset 0
    yoffset 0
    repeat

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
    play music "beethoven.mp3"
    "you will now hear some slow jazz"
    stop music fadeout 1.0
    f "oh no jazz no longer"
    hide finn with dissolve

    hide bg 3dmodel with dissolve

    "good job give yourself a pat on the back bc now we're acc getting to develop"
    "IF ONLY LUCA FINISHED HIS SCRIPT"
    "oml fr"
    f "do it now"
    fr "or at least send us the gist so we can get to work while"
    fr "you write"

    show frazier
    fr "hi its me the deer guy"
    fr "fr fr"
    show finn at bounce, center
    f "i bounced"
    f "cool amirite"
    hide finn
    hide frazier


    show bg nyclamp with dissolve
    show finn at right with dissolve

    f "this is nyc ofc"

    show ari at left with dissolve

    a "ok this should work i think"
    label some_scene:
    "A quick-time event is about to start!"
    $ start_qte()
    call screen qte_screen

    if qte_success:
        "You succeeded!"
    else:
        "You failed!"

    return
