
# The script of the game goes in this file.
init:
    define config.default_voice_volume = 0.0
    default preferences.text_cps = 20
    define show_quick_menu = False
    define config.hard_rollback_limit = 100

    $ config.developer = True
    $ config.console = True

jump defaults

# Declare characters used by this game. The color argument colorizes the
# name of the character.
jump characters

jump images

label end:
    $ renpy.quit()

label splashscreen:
    if not Android:
        scene warning with Fade(0,1,3)
        menu:
            "Yes, I'm 18 years old":
                pass
            "No, I am under 18":
                jump end
    scene jj with Fade(.5,0,3)
    $ main_menu = True
    show screen main_menu()
    with Fade(0,0,3)
return

# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.
    scene black

    $ main_menu = False
    hide screen main_menu
    with dissolve

    init:
        define config.developer = True
        define config.console = True

    jump intro

label fail:
    $ config.rollback_enabled = False
    scene fail with Dissolve(1.0):
    pause
    $ renpy.full_restart()

label tbc:
    play music "music/tbc.mp3"
    scene tbc with wipeleft
    $ renpy.pause(1.0, hard=True)
    jump endgame

label endgame:
    $ renpy.pause(1.0, hard=True)
    $ renpy.block_rollback()
    scene gg with flashbulb
    "You have finished the current version."
    jump dr
    return

label dr:
    scene smc1 with dissolve
    ad "I am the American dream, also known as DR. Are you trying to fight me, bald man?"
    scene smc2 with dissolve
    "I'm going to destroy you, old man."
    scene smc3 with dissolve
    "Try to resist my bald spot."
    scene smc4 with dissolve
    ad "Try to accept my blow."
    "Dodge!!!!"
    scene smc5 with dissolve
    "Shit!"
    $ renpy.full_restart()


    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.


    # These display lines of dialogue.



    # This ends the game.

    return
