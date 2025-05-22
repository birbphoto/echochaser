label test1two:
    "Test 1.2"
    hide all
    menu:
        "Test transitions":
            jump transitions
        "Skip":
            jump posttst
label transitions:
    "Transitions test"
    "Dissolve"
    show finn with dissolve
    "Done"
    hide finn
    "Fade"
    show finn with fade
    "Done"
    hide finn
    "Pixellate"
    show finn with pixellate
    "Done"
    hide finn
    "Zoomin"
    show finn with zoomin
    "Done"
    hide finn with zoomout
    "Punches"
    show finn
    show finn with vpunch
    "V"
    show finn with hpunch
    "H"
    "Blinds"
    hide finn with blinds
    "Done"
label posttst:
    "Skipped or finished transition testing."
    hide all
    show finn
    "Anim tests"
    show finn at bounce with hpunch
    $ renpy.pause(1.0)
    hide finn
    show finn
    "Dialogue 1"
    show finn with hpunch
    "Exclamation!"
    "im acc so confused at what I want to test next"
    "send me the script already"
    "im bored as fuck please"
    "i beg <@248124>"
    