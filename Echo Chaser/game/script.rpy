define f = Character("Finn", color="#ad3232")
define a = Character("Ari", color="#0c8fa0")
define fr = Character("Frazier", color="#8322c4")

define wc = Character("Wall Cat", color="#56b35d")
#define mne = Character("Mene Tame", color="#8156b3")
image wallcat = "wallcat.png"
#image mene = "mene.png"
image bg coffee = "coffee-shop.png"
image teto = "teto.jpg"
image test movie = Movie(size = (1920,1080), channel="movie", play="movies/testwebm.webm", side_mask=True)

#screen main_menu:
    #add "main_menu"
    #textbutton "Start" action Start() xalign 0.5 yalign 0.5

init python:
    renpy.music.register_channel("voice", loop=False, stop_on_mute=True)

image finn = "finn.png"
image ari = "ari.png"
image frazier = "frazier.png"
image bg ilya = "ilya.jpg"
image bg 3dmodel = "3d-model.jpg"
image bg nyclamp = "nycgotham.jpg"
''' Template for two speaking at once
    f "im speaking over you." (multiple=2)
    $ renpy.pause(1.0)
    fr "yeah finn stfu" (multiple=2)
'''
transform bounce:
    pause .15
    yoffset 0
    easein .175 yoffset -100
    easeout .175 yoffset 0
    easein .175 yoffset -40
    easeout .175 yoffset 0
    yoffset 0
    repeat

transform double_size: 
    zoom 2.0
transform onehalf_size:
    zoom 1.5
transform half_size:
    zoom 0.5
"""
Template for character speech:  
        play sound "voice/characterline.mp3"
        Character "hi"
        stop sound

    (allows for S;G style voice lines with text)

    Idea for call function:

    label csay(saychar, msg, voiceline):
        play sound voiceline
        $ saychar(msg)
        stop sound
        return

    call csay(f, "Hi! How are you? This is long for testing.", "incorrect.mp3")

    Idea for define function:

    $ def CSay(saychar, msg, voiceline):
        play sound voiceline
        saychar msg
        stop sound
"""

label start:
    menu:
        "Test version 1.0":
            jump test1
        "Test version 1.1":
            jump test2
        "Test version 1.2":
            jump test3

label test1:
    "Test version 1.0 (nil)"
    "I'm going to try to jump to another script. (test1nil.rpy)"
    jump test1nil

label test2:
    "Test version 1.1"
    "I'm going to try to jump to another script. (test1one.rpy)"
    jump test1one

label test3:
    "Test version 1.2"
    "Jumping to test1two.rpy"
    jump test1two