# cave_broadside

label cave_act_crack_outside_stick:
    scene bg_cave_interact_crack_outside_stick with fade
    p "Urrrghh."
    p "I don't think it'll budge."
    p "If I try to force it, it might break the stick."
    p "Better not. I have a feeling it might come in handly later."
    $ cave_flags['crack_stick_outside'] = True
    $ renpy.notify("Avoided wasting the [Stick]!")
    jump cave_broadside


# cave_treasure

label cave_act_dig:
    scene bg_cave_dig_1 with fade
    pause
    p "What kind of dirt even is this? It's so thick."
    p "This'll be tough."
    p "Hnnng!"
    menu:
        p "Oof. It's not budging... should I give up?"

        "The dirt is too strong":
            jump cave_treasure
        "I am slightly stronger":
            scene bg_cave_dig_2 with dissolve
            pause
            p "Hnnnnggg!"
            "{b}{i}{size=69}CRACK{/size}{/i}{/b}"
            scene bg_black
            pause 1
            scene bg_cave_dig_3 with fade
            pause
            p "Ow."
            p "It broke..."
            scene bg_cave_dig_4 with dissolve
            p "It REALLY broke."
            p "Well, I guess that could've been worse."
            p "Might as well hang onto the pieces..."
            $ renpy.notify("Lost the [Shovel]... but acquired some [Shovel Pieces]?")
            $ inv.remove('cave_shovel')
            $ cave_flags['shovel_broken'] = True
            $ inv.append('cave_shaft')
            $ inv.append('cave_hook')
            jump cave_treasure

label cave_act_dig_pick:
    scene bg_cave_dig_pick_1 with fade
    p "Finally time to dig this thing up."
    scene bg_cave_dig_pick_2 with dissolve
    pause .25
    scene bg_cave_dig_pick_1 with dissolve
    pause .25
    scene bg_cave_dig_pick_2 with dissolve
    pause .25
    scene bg_cave_dig_pick_1 with dissolve
    pause .25
    scene bg_black with fade
    pause .75
    $ inv.remove('cave_pick')
    $ cave_flags['pile_dug'] = True
    $ renpy.notify('No more use for the [Pick]...')
    jump cave_treasure

label cave_act_end_cave:
    scene cave_cs_outro_1 with fade
    pause
    p "Oh dang."
    "{i}{size=69}To be confinued???{/size}{/i}"
    return

# cave_tent

label cave_act_fire_lantern:
    scene bg_cave_lantern_break_1 with fade
    pause
    p "Well, only one way I can think of to get the oil out is to break the whole thing."
    menu:
        p "Am I sure I want to break it?"

        "No, I'm a coward":
            p "Maybe I'll hold onto it for now."
            jump cave_tent
        "See you in hell, lantern":
            scene bg_cave_lantern_break_2 with dissolve
            pause
            p "I hope this works."
            scene bg_cave_lantern_break_3 with dissolve
            pause 0.25
            scene bg_cave_lantern_break_4 with dissolve
            pause
            "{b}{i}{size=69}CRASH{/size}{/i}{/b}"
            p "Huh. It actually did."
            p "Now I just have to find some way to light this."
            $ cave_flags['lantern_smashed'] = True
            $ inv.remove('cave_lantern')
            $ renpy.notify("Lost the [Lantern]...")
            jump cave_tent

label cave_act_fire_flintlock:
    if cave_flags['lantern_smashed']:
        scene bg_cave_interact_fire_pistol_1 with fade
        pause
    else:
        scene bg_cave_interact_fire_pistol_fail_1 with fade
        pause
    p "Let's see if ol' Sparky here can light this."
    if cave_flags['lantern_smashed']:
        scene bg_cave_interact_fire_pistol_2 with dissolve
        pause
    else:
        scene bg_cave_interact_fire_pistol_fail_2 with dissolve
        pause
    "BANG!"
    if cave_flags['lantern_smashed']:
        scene bg_cave_interact_fire_pistol_3
        pause
        p "I can't believe that worked."
        p "I feel like a genius."
        $ cave_flags['campfire_lit'] = True
        if 'journal' in inv:
            p "This has gotta be enough light to read that book now."
        jump cave_tent
    else:
        scene bg_cave_interact_fire_pistol_fail_3
        pause
        p "I thought for sure that would work."
        p "Maybe there's some way to make this wood more flammable..."
        jump cave_tent

label cave_act_fire_book:
    scene bg_cave_interact_fire_lit_book with fade
    if not cave_flags['journal_read']:
        p "Looks like it's a journal."
        p "Property of Captain Dwight Rortugal, of the {i}Blunt Javelin.{/i}"
        p "Do I want to read the whole thing?"
    else:
        p "Do I want to re-read the captain's journal?"    
    menu:
        "Yes":
            scene bg_cave_interact_fire_lit_book_closeup with fade
            p '"Fate truly lies beyond the grasp of men."'
            p '"Imagine purloining the infamous treasure of Lucky Richard Longwood, only to find our way down a whirlpool while making our escape."'
            p '"We had no choice. Any other route and we faced certain capture. In charting this, I spared some lives as well as all our treasure. I would do so again."'
            p '"The men are angry, but they will come to see the wisdom of this in time. The gain shall prove worth the venture."'
            p "..."
            p '"The men are gone. They all decided to swim for it. None will make it, and good riddance. They have buried the treasure against my orders, and pretend they will return for it later."'
            p '"They demanded their cut of the treasure first, but they shall not have it. The key to the hoard is within my safe, and the key to my safe was quite unfindable."'
            p '"I told them, of course, that it was lost to the sea when the {i}Javelin{/i} went under. They did not believe me, and they of course searched every inch of the wreck to disprove me. And they of course found nothing."'
            p '"I anticipated their greed and countered them. The key to my safe is safely within my stomach."'
            p '"Soon the legendary treasure will belong to I alone."'
            p "..."
            p '"The pain in my stomach has grown intolerable."'
            p '"The key has refused to emerge. I have managed to forage contraband rum overlooked by the now-drowned cowards."'
            p '"I shall imbibe it all and purge the key that way. I shall not be denied my treasure. I deserve this."'
            p "..."
            p "That's the last entry."
            p "What an asshole."
            p "I wonder if he managed to throw up the key. Maybe it's nearby?"
            $ cave_flags['journal_read'] = True
            $ renpy.notify('Gained [Ominous Knowledge]!')
            jump cave_tent
        "No, I'm bored.":
            $ renpy.notify('Gained [Nothing]!')
            jump cave_tent

label cave_act_fire_tar:
    scene bg_cave_interact_fire_tar with fade
    pause
    p "I'll just heat this up a little bit, and then hopefully it'll be good and sticky again."
    $ cave_flags['hot_tar'] = True
    $ tooltips['cave_tar'] = "Sticky Tar"
    $ renpy.notify('Heated the [Tar]!')
    jump cave_tent

# cave_ascent

label cave_act_ascent:
    scene bg_cave_interact_ascent_windup with fade
    pause
    p "They never taught me how to do anything like this on the Handsome Pete."
    p "Just as well. I doubt I'd have learned it anyway."
    scene bg_cave_interact_ascent_grapple_hook with dissolve
    pause
    $ renpy.notify("Lost the [Grappling Hook]...")
    $ inv.remove('cave_grappling_hook')
    $ cave_flags['ascent'] = True
    jump cave_ascent

label cave_act_ascent_false:
    scene bg_cave_interact_ascent_windup with fade
    pause
    p "They never taught me how to do anything like this on the Handsome Pete."
    p "Just as well. I doubt I'd have learned it anyway."
    scene bg_cave_interact_ascent_grapple_nohook with dissolve
    pause
    $ inv.remove('cave_chain')
    $ renpy.notify("Lost the [Chain]...")
    $ cave_flags['false_ascent'] = True
    jump cave_ascent

# cave_corner

label cave_act_lumber:
    scene bg_cave_interact_lumber_cleanup with fade
    pause
    p "All right, hopefully this'll work as a lever."
    p "Hnngg."
    scene bg_cave_interact_lumber_cleanup_2 with dissolve
    pause 0.5
    scene bg_cave_interact_lumber_cleanup_3 with dissolve
    pause
    p "Whew. One down, a few more to go."
    scene bg_black with fade
    pause .75
    $ cave_flags['pile_clear'] = True
    jump cave_corner


# cave_ship_perch

label cave_act_cannon_upper:
    $ cave_flags['cannon_inspected'] = True
    scene bg_cave_interact_cannon_upper_2 with fade
    pause .5
    p "Here goes nothing."
    p "Hnnnng!"
    scene bg_cave_interact_cannon_upper_3 with dissolve
    pause .25
    scene bg_cave_interact_cannon_upper_4 with dissolve
    pause .25
    scene bg_cave_interact_cannon_upper_5 with dissolve
    pause .25
    "{b}{i}{size=69}CRASH{/size}{/i}{/b}"
    p "Whew."
    p "Well, it's on the ground level now."
    if "cave_cannonball" in inv:
        p "Now to get down there and load it."
    else:
        p "I need to find something to load it with, though."
    $ cave_flags['cannon_pushed'] = True
    jump cave_ship_perch


# cave_ship_crack

label cave_act_crack_pick:
    scene bg_cave_interact_crack_pick with fade
    if cave_flags['crack_stick']:
        p "Hnnngngngng!"
        p "This won't work either..."
        if cave_flags['cannon_pushed']:
            p "I really should just use the cannon instead of being stubborn and weird."
    else:
        p "Hnnnng."
        p "It won't budge..."
        if cave_flags['cannon_pushed']:
            p "Why am I even trying this?"
            p "The cannon is right over there."
    $ cave_flags['crack_pick'] = True
    jump cave_ship_crack

label cave_act_crack_stick:
    scene bg_cave_interact_crack_stick with fade
    if cave_flags['crack_pick']:
        p "Hnnngngngng!"
        p "This won't work either..."
        if cave_flags['cannon_pushed']:
            p "I really should just use the cannon instead of being stubborn and weird."
    else:
        p "Hnnnng."
        p "It won't budge..."
        if cave_flags['cannon_pushed']:
            p "Why am I even trying this?"
            p "The cannon is right over there."
    $ cave_flags['crack_stick'] = True
    jump cave_ship_crack

# cave_ship_descent

label cave_act_cannon_cannonball:
    scene bg_cave_cannon_load with fade
    p "Hopefully there's no special tricks to loading these."
    scene bg_cave_cannon_load_2 with dissolve
    pause .5
    p "Guess I'll find out when I light it."
    $ inv.remove('cave_cannonball')
    $ cave_flags['cannon_loaded'] = True
    $ renpy.notify('Loaded the [Cannonball] into the cannon!')
    jump cave_ship_descent

label cave_act_cannon_flintlock:
    scene bg_cave_interact_cannon_2 with fade
    pause .5
    p "I know I already said here goes nothing..."
    p "But this is the most nothing that's ever gone."
    scene bg_cave_interact_cannon_3 with dissolve
    pause 0.5
    scene bg_cave_interact_cannon_4 with dissolve
    pause 0.5
    "HISSSSS"
    scene bg_cave_interact_cannon_5 with fade
    pause 0.5
    "{b}{i}{size=69}BOOM{/size}{/i}{/b}"
    scene bg_cave_interact_cannon_6 with dissolve
    pause 0.5
    p "Am I dead?"
    p "I don't feel dead..."
    p "I feel..."
    scene bg_cave_interact_cannon_7 with dissolve
    pause 1
    p "...like a fuckin' genius!"
    p "Never didn't have it."
    $ cave_flags['cannon_fired'] = True
    jump cave_ship_descent

# cave_ship_end

label cave_act_safe_key:
    if cave_flags['cannon_pushed']:
        scene bg_cave_interact_safe_end_2_cannon with fade
    else:
        scene bg_cave_interact_safe_end_2 with fade
    pause .5
    if cave_flags['journal_read']:
        p "Let's see if that other key the captain was talking about is still inside..."
    else:
        p "Time to see if there's anything useful in here..."
    "CLICK"
    scene bg_cave_interact_safe_end_3 with fade
    if cave_flags["journal_read"]:
        p "Looks like the other key all right..."
        if cave_flags['cannon_fired']:
            p "Now to see what's so special about that treasure he buried."
        else:
            p "Now to find a way out of here."
    else:
        p "A key to get another key?"
        p "Weird."
        p "Maybe it unlocks an even fancier safe..."
    $ inv.append('cave_safekey')
    $ inv.remove('cave_key')
    $ renpy.notify("Lost the [Skeleton's Key] in exchange for an [Ornate Key]!")
    jump cave_ship_end