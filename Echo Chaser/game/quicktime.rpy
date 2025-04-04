default qte_key = "a"
default qte_success = None

init python:
    import random
    import renpy.store as store
    import renpy.exports as renpy

    def start_qte():
        store.qte_key = random.choice(["a", "s", "d", "f"])  # Random key choice
        store.qte_success = None
        renpy.restart_interaction()

    def check_qte(event):
        if event == store.qte_key:
            store.qte_success = True
            renpy.jump("qte_success")
        else:
            store.qte_success = False
            renpy.jump("qte_fail")

style qte_text:
    size 50
    color "#FFFFFF"
    outlines [(3, "#000000")]  # Note: "outlines" (plural) instead of "outline"
    xalign 0.5
    yalign 0.4

screen quicktime_event(qte_key, on_success):
    modal True
    tag qte  # ensures it replaces other screens with the same tag

    text "Press [qte_key]!" xpos 0.5 ypos 0.4 style "qte_text"

    key qte_key action [Hide('quicktime_event'), Function(on_success)]

screen qte_screen:
    text "Press [qte_key]!" xpos 0.5 ypos 0.4 style "qte_text"

    key [qte_key] action Function(check_qte, qte_key)
    timer 1.5 action Jump("qte_fail")

label qte_success:
    "Success! You pressed the right key in time!"
    a "im proud"
    $ fail = False
    return

label qte_fail:
    "Too slow! Or wrong key!"
    a "you fucking suck jump off a cliff"
    $ fail = True
    return
