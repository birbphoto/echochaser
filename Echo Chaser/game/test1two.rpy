label test1two:
    "Test 1.2"
    hide all
    menu:
        "Test transitions":
            jump transitions
        "t1n2":
            jump t1n2start
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
    hide all with dissolve

label t1n2start:
    show bg coffee at double_size with dissolve
    show finn at right with dissolve
    show frazier at left with dissolve
    f "Tired of being what you want me to be"
    f "Feeling so faithless, lost under the surface"
    f "Don't know what you're expecting of me"
    f "Put under the pressure"
    f "of walking in your shoeeeeeeeeeessss" (multiple=2)
    $ renpy.pause(2.0)
    fr "(caught in the undertow, just caught in the undertow)" (multiple=2)
    f "Every step that I take"
    f "is another mistake to youuuuuuuuuu" (multiple=2)
    $ renpy.pause (2.0)
    fr "(caught in the undertow, just caught in the undertow)" (multiple=2)

    "that concludes the numbing check"
    "ok im sorry acc throw me off a cliff or sum that was stupid"
