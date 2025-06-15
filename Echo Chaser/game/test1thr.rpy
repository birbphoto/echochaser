define t = Character("Tarot", color="#ad3232")

label test1thr:
    "Testing tarot minigame"

    label tarot:
        $ draw_tarot_card()
        if current_orientation == "Upright":
            show test bg 1
        else:
            show test bg 2

    "You drew: [current_card] ([current_orientation])"
    
    menu:
        "Yes":
            jump tarot
        "No":
            return
