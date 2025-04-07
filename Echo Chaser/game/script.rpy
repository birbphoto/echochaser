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

label test1:
    "Test version 1.0 (nil)"
    "I'm going to try to jump to another script. (test1nil.rpy)"
    jump test1nil

label test2:
    "Test version 1.1"
    "I'm going to try to jump to another script. (test1one.rpy)"
    jump test1one
