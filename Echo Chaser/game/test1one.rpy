# image cutscene movie = Movie(play="images/testvideo.mp4", side_mask=True)

label test1one:
    "Success!"
    f "Definitions also work in between scripts."
    "Testing CSay function."
    # CSay(f, "Hi! How are you? This is long for testing.", "incorrect.mp3")
    "CSay function was skipped. Refine when it works."
    "Reverting to standard function (manual...)"
    "See large comment around line 25-30."
    "Testing video cutscenes"
    # This will be the skippable video cutscene

label cutscenetest:
    #window hide
    #with dissolve
    #show cutscene movie
    #"You are watching a skippable video cutscene."
    #window show
    #"The video has ended."
    #return
    $ renpy.movie_cutscene("testvideo.mp4")
