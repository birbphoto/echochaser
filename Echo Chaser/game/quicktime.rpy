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



screen qte_screen:
    text "Press [qte_key]!" xpos 0.5 ypos 0.4
    key [qte_key] action Function(check_qte, qte_key)
    timer 1.5 action Jump("qte_fail")

label qte_success:
    "Success! You pressed the right key in time!"
    return

label qte_fail:
    "Too slow! Or wrong key!"
    return
