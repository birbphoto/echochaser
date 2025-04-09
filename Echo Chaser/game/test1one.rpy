define wc = Character("Wall Cat", color="#56b35d")
define mne = Character("Mene Tame", color="#8156b3")
image wallcat = "wallcat.png"
image mene = "mene.png"
image bg coffee = "coffee-shop.png"
transform double_size: 
    zoom 2.0
transform onehalf_size:
    zoom 1.5
transform half_size:
    zoom 0.5

#label start: 
# image cutscene movie = Movie(play="images/testvideo.mp4", side_mask=True)

label test1one:
    "Success!"
    f "Definitions also work in between scripts."
    "Testing CSay function."
    # CSay(f, "Hi! How are you? This is long for testing.", "incorrect.mp3")
    "CSay function was skipped. Refine when it works."
    "Reverting to standard function (manual...)"
    "See large comment around line 25-30."

    show bg coffee at double_size with dissolve
    "Test conversation!! Yippee!"
    show wallcat at onehalf_size, left with dissolve
    play sound "voice/cameron/test1.wav"
    wc "The Center is an afternoon music program that aired on BET. It debuted on March"
    stop sound

    play sound "voice/cameron/test2.wav"
    wc "3, 2003, replacing Hits from the Street. The program focused on music, entertainment and lifestyle."
    stop sound

    play sound "voice/cameron/test3.wav"
    wc "The program was originally hosted by R&B singer Amerie, but in September 2003"
    stop sound

    play sound "voice/cameron/test4.wav"
    wc "he left to work on her new music. On March 8, 2004, Tiffany Withers, host of BET.com"
    stop sound

    play sound "voice/cameron/test5.wav"
    wc "Countdown, left that program and became the new host of The Center."
    stop sound

    show ari at right with dissolve
    play sound "voice/madison/1.ogg"
    a "At a time like this, negative people choose to focus on their grief. Well, I hate those people because I am a very positive person. I remember the good times, like when Heather and I got our ears pierced at the mall. I can still hear those late night talks on the phone."
    stop sound
    
    show frazier with dissolve
    play sound "voice/hannah/1.ogg"
    fr "lebronnn lebronn lebron james lebron james lebrooon james lebron james lebron james"
    stop sound

    play sound "voice/madison/2.ogg"
    a "Should've thought of that before you killed me. God, I'm gonna be coughing up drain cleaning for eternity. Ugh, Heatherduke is such a sad little poser. Veronica, tell her to stop touching my stuff. Veronica? Veronica?!"
    stop sound

    play sound "voice/madison/3.ogg"
    a "And they lived happily ever after. You really believed that. You'd think it would go back to normal. Don't give me that wounded look. You know exactly what he is and you love it. Only a true dead best friend would give it to you straight."
    stop sound

    hide ari with dissolve
    hide bg coffee with dissolve
    hide wallcat with dissolve
    
    show mene at half_size, right with dissolve
    mne "i am losing my mind or sum idk"

   
#"Testing video cutscenes"
# This will be the skippable video cutscene

#
#label cutscenetest:
    #window hide
    #with dissolve
    #show cutscene movie
    #"You are watching a skippable video cutscene."
    #window show
    #"The video has ended."
    #return
    #$ renpy.movie_cutscene("testvideo.mp4") -- currently uses wrong video codec, too lazy to find another test video :P