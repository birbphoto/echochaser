define f = Character("Finn", color="#ad3232")
define a = Character("Ari", color="#0c8fa0")
define fr = Character("Frazier", color="#8322c4")

init python:
    renpy.music.register_channel("voice", loop=False, stop_on_mute=True)

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
    # for testing purposes!! please remove goto if testing whole game.
    jump nyclamppo
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

label nyclamppo:
    show bg nyclamp with dissolve
    show finn at right with dissolve

    f "this is nyc ofc"

    show ari at left with dissolve

    a "ok this should work i think"
    
    jump Success # DEBUG!!! delete to test quicktime

label some_scene:
    "Test 1"
    $ start_qte()
    call screen qte_screen
    
label Success:
    "damn"
    #if fail == False:
    #   "hi ho"
    a "running fine still?"
    #test menu/variable
    menu:
        "Running OK?"

        "Yes.":
            a "good"
            $ running = True
        "No.":
            a "uh oh"
            $ running = False
        "nvfm jump":
            a "kk"
    
    "end of menu"
    if running:
        "Running fine"
    else:
        "Not running fine"
    f "im speaking over you." (multiple=2)
    fr "yeah finn stfu" (multiple=2)

    "Testing say with voice"
    play sound "incorrect.mp3"
    f "hi"
    stop sound
    fr "no"