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
image test bg 1 = "test80p1.png"
image test bg 2 = "test80p2.png"

#screen main_menu:
    #add "main_menu"
    #textbutton "Start" action Start() xalign 0.5 yalign 0.5

init python:
    renpy.music.register_channel("voice", loop=False, stop_on_mute=True)
    import random
    tarot_cards = [
        "The Fool", "The Magician", "The High Priestess", "The Empress", "The Emperor",
        "The Hierophant", "The Lovers", "The Chariot", "Strength", "The Hermit",
        "Wheel of Fortune", "Justice", "The Hanged Man", "Death", "Temperance",
        "The Devil", "The Tower", "The Star", "The Moon", "The Sun",
        "Judgement", "The World",
    ]
    current_card = None
    def draw_tarot_card():
        global current_card, current_orientation
        current_card = random.choice(tarot_cards)
        current_orientation = random.choice(["Upright", "Reversed"])

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

label start: #make sure you call back afterwards on each testx.
    menu:
        "Test version 1.0":
            jump test1
        "Test version 1.1":
            jump test2
        "Test version 1.2":
            jump test3
        "Test version 1.3":
            jump test4

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

label test4:
    "Test version 1.3"
    "Jumping to test1thr.rpy"
    jump test1thr