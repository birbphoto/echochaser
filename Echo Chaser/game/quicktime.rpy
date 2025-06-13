default qte_key = "a"
default qte_success = None

init python:
    import random
    import renpy.store as store
    import renpy.exports as renpy

    def start_qte():
        # Randomly choose a key for the QTE
        store.qte_key = random.choice(["a", "s", "d", "f"])
        store.qte_success = None
        # Instead of restarting interaction, just show the screen
        renpy.show_screen("quicktime_event", qte_key=store.qte_key, on_success=on_qte_success)

    def check_qte(event):
        if event == store.qte_key:
            store.qte_success = True
            renpy.jump("qte_success")
        else:
            store.qte_success = False
            renpy.jump("qte_fail")

    def on_qte_success():
        renpy.jump("qte_success")

style qte_text:
    size 50
    color "#FFFFFF"
    outlines [(3, "#000000")]
    xalign 0.5
    yalign 0.4

screen quicktime_event(qte_key, on_success):
    modal True
    tag qte

    text "Press [qte_key]!" xpos 0.5 ypos 0.4 style "qte_text"

    key qte_key action [Hide('quicktime_event'), Function(on_success)]
    timer 1.5 action Jump("qte_fail")

label qte_success:
    "Success! You pressed the right key in time!"
    a "I'm proud of you!"
    $ fail = False
    jump Success
    return

label qte_fail:
    "Too slow! Or wrong key!"
    a "wow you suck" #changed because ugh nono word :(
    $ fail = True
    return