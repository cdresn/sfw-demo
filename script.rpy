# The script of the game goes in this file.

label start:

    $ player_name = renpy.input("What is your name?", default='guy')
    define p = Character('[player_name]', color='#006aff')

    jump cave_parent
        

style combine_button:
    color "#FFFFFF"
    hover_color "#66ff00"
    size 100
    background Solid("#00000099")

style big_question:
    size 225
    color "#FFFFFF"

