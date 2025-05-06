# center screen

label interact_with_cave_book:
    scene bg_cave_interact_book with fade
    $ in_menu = True
    while in_menu:
        menu (x = 0.2, y = 0.2):
            "Inspect":
                p "It's an old book."
                p "The binding is sturdier than you'd think. The paper's held up too."
                p "This must've belong to someone with money."
            "Read":
                scene bg_cave_book_read_fail with fade
                pause
                p "This handwriting is worse than mine. It's too dark to actually understand any of this."
                p "Maybe if I had some light..."
                scene bg_cave_interact_book with fade
            "Take":
                $ inv.append('cave_book')
                $ renpy.notify("Acquired a [Journal]!")
                $ in_menu = False
                jump cave_center
            "Leave":
                $ in_menu = False
                jump cave_center


label interact_with_cave_lantern:
    scene bg_cave_interact_lantern with fade
    $ in_menu = True
    while in_menu:
        menu (x = 0.85, y=.75):
            "Inspect":
                p "It's a lantern."
                p "It looks like there's still oil inside, but the hinges are rusted shut."
            "Light":
                p "I don't have anything to light it with, for starters."
                p "And I'm not sure I could get it open even if I could."
            "Take":
                $ inv.append('cave_lantern')
                $ renpy.notify("Acquired a [Lantern]!")
                $ cave_flags['lantern_taken'] = True
                $ in_menu = False
                jump cave_center
            "Leave":
                $ in_menu = False
                jump cave_center

# cave_treasure

label interact_with_cave_shovel:
    scene bg_cave_interact_shovel with fade
    $ in_menu = True
    while in_menu:
        menu(x=.9, y=.2):
            "Inspect":
                p "It's a shovel. It's seen better days."
                p "In its youth, I bet it probably buried whatever's under that pile."
                p "I hope it's got one more dig in it."
            "Take":
                $ inv.append('cave_shovel')
                $ cave_flags['shovel_taken'] = True
                $ renpy.notify ("Acquired a [Shovel]!")
                $ in_menu = False
                jump cave_treasure
            "Leave":
                $ in_menu = False
                jump cave_treasure

label interact_with_cave_treasure:
    scene bg_cave_interact_treasure with fade
    $ in_menu = True
    while in_menu:
        menu(x=.25, y=.2):
            "Inspect":
                p "It's a big pile. Whatever's under it must be pretty big, too."
            "Dig":
                p "There's no way I can dig this up by hand."
                p "Maybe if I tried a shovel..."
                if cave_flags['shovel_broken']:
                    p "But it better be sturdier than the first one I tried."
            "Leave":
                $ in_menu = False
                jump cave_treasure

label interact_with_cave_treasure_2:
    if cave_flags['skeleton_hat']:
        scene bg_cave_interact_treasure_cannonfired_hatoff with fade
    else:
        scene bg_cave_interact_treasure_cannonfired_haton with fade
    $ in_menu = True
    while in_menu:
        menu(x=.45, y=.25):
            "Inspect":
                p "Looks like the cannonball did a lot of the digging for me."
                p "Lucky duck."
                if cave_flags['journal_read']:
                    p "Must be the treasure the captain thought was worth dying for."
                    p "I wonder if it'll even be useful."
                else:
                    if 'cave_safekey' in inv:
                        p "I'm going to go out on a limb and guess this what the fancy key I found unlocks."
                    else:
                        p "Unsurprisingly, there's a treasure chest under the big dirt pile."
                    p "Must be something valuable in it to go through all the trouble of burying it."
            "Dig":
                p "I'm still not going to dig this up with my bare hands."
                if 'cave_pick' in inv:
                    p "I should try using that pick I found in the ship."
            "Leave":
                $ in_menu = False
                jump cave_treasure

label interact_with_cave_treasure_3:
    if cave_flags['skeleton_hat']:
        scene bg_cave_interact_treasure_final_hatoff with fade
    else:
        scene bg_cave_interact_treasure_final_haton with fade
    $ in_menu = True
    while in_menu:
        menu(x=.45, y=.25):
            "Inspect":
                if cave_flags['journal_read']:
                    p "That's the treasure from the journal all right."
                    if 'cave_safekey' in inv:
                        p "Nothing left to do but unlock it."
                    else:
                        p "I need to retrieve the key from the captain's safe if I want to unlock it."
                else:
                    p "It's an even bigger chest than I expected."
                    if 'cave_safekey' in inv:
                        p "I should try using that key I found to unlock it."
                    else:
                        p "I wonder if there's a key for it around here somewhere."
            "Leave":
                $ in_menu = False
                jump cave_treasure


# cave_skeleton

label interact_with_cave_bottle:
    scene bg_cave_interact_bottle_1 with fade
    $ in_menu = True
    while in_menu:
        menu(x=.15,y=.3):
            "Inspect":
                p "It's an empty bottle. This guy must've drunk the last of it before he died."
                p "Some of the crew on the {i}Handsome Pete{/i} would hide bottles just like this from the officers."
            "Smell" if not cave_flags['smelled_booze']:
                scene bg_cave_interact_bottle_2 with dissolve
                p "I guess I can try to see what kind of..."
                p "Oh."
                p "Can you get drunk from smelling something? That's really strong."
                p "Maybe this guy died of alcohol poisoning."
                if cave_flags['journal_read']:
                    p "If he drank the whole bottle and still couldn't throw the key back up..."
                $ cave_flags['smelled_booze'] = True
                scene bg_cave_interact_bottle_1 with dissolve
            "Drink" if cave_flags['smelled_booze'] and not cave_flags['tried_booze']:
                p "Really?"
                menu(x=.15,y=.3):
                    "No, just kidding":
                        p "Whew. I was starting to worry myself there for a second."
                        $ renpy.notify('Did not acquire [Crippling Cirrhosis]!')
                    "YES, DRINK IT":
                        scene bg_cave_interact_bottle_3 with dissolve
                        p "I am not going to try to drink out of this."
                        p "There's a few drops at most and even that much would probably kill me."
                        p "I'm getting a little alarmed about some of these intrusive thoughts."
                        $ cave_flags['tried_booze'] = True
                        $ renpy.notify('Acquired some [Doubt Regarding Your Own Sanity]!')
                        scene bg_cave_interact_bottle_1 with dissolve
            "Leave":
                $ in_menu = False
                jump cave_skeleton
            


label interact_with_cave_skeleton_hat:
    scene bg_cave_interact_skeleton_hat_1 with fade
    $ in_menu = True
    while in_menu:
        menu(x=.15,y=.2):
            "Inspect":
                scene bg_cave_interact_skeleton_hat_2 with dissolve
                p "Some ostentatious haberdashery here."
                if cave_flags['journal_read']:
                    p "This has gotta be Captain Rortugal."
                    p "I wonder if that means the key he wrote about is nearby."
                else:
                    p "Either he was the captain, or he died wearing the captain's hat."
                menu(x=.15,y=.2):
                    "Set it aside":
                        p "Hope I have better luck than you did."
                        $ cave_flags['skeleton_hat'] = True
                        $ in_menu = False
                        jump cave_skeleton
                    "Try it on":
                        p "Why would I try this on? I already have a hat."
                        menu(x=.15,y=.2):
                            "Good point.":
                                p "I'll just leave this here."
                                p "Hope I have better luck than you did."
                                $ cave_flags['skeleton_hat'] = True
                                $ in_menu = False
                                jump cave_skeleton
                            "PUT ON THE HAT!":
                                scene bg_cave_interact_skeleton_hat_3 with dissolve
                                pause
                                $ renpy.say(p, "...", x=1.0, y=.5) 
                                p "I'm not sure what I was trying to accomplish with this."
                                p "I need to control these intrusive thoughts better."
                                $ cave_flags['skeleton_hat'] = True
                                $ renpy.notify("Did not acquire a [Captain's Hat]! Don't be weird.")
                                $ in_menu = False
                                jump cave_skeleton
                    "Leave":
                        $ in_menu = False
                        jump cave_skeleton
            "Leave":
                $ in_menu = False
                jump cave_skeleton


label interact_with_cave_skeleton_key:
    if cave_flags['skeleton_hat']:
        scene bg_cave_interact_skeleton_key_nohat with fade
    else:
        scene bg_cave_interact_skeleton_key_hat with fade
    p 'What do we have here?'
    $ inv.append('cave_key')
    $ renpy.notify("Acquired a [Skeleton's Key]!")
    jump cave_skeleton

# cave_tent

label interact_with_cave_unlit_fire:
    scene bg_cave_interact_fire_unlit with fade
    $ in_menu = True
    while in_menu:
        menu(x=.9,y=.3):
            "Inspect":
                p "It's a campfire."
                p "There's wood here already, but it's not particularly dry."
            "Leave":
                $ in_menu = False
                jump cave_tent

label interact_with_cave_ready_fire:
    scene bg_cave_interact_fire_unlit_ready with fade
    $ in_menu = True
    while in_menu:
        menu(x=.9,y=.3):
            "Inspect":
                p "The lantern oil is all over the wood now."
                p "I just need to think of a way to light it..."
            "Leave":
                $ in_menu = False
                jump cave_tent

label interact_with_cave_lit_fire:
    scene bg_cave_interact_fire_lit with fade
    $ in_menu = True
    while in_menu:
        menu(x=.9,y=.3):
            "Inspect":
                p "It's burning pretty well now."
                if 'cave_book' in inv and not cave_flags['journal_read']:
                    p "Bright enough to read by, even."
            "Leave":
                $ in_menu = False
                jump cave_tent

# cave_ascent

label interact_with_cave_ascent:
    scene bg_cave_interact_ascent_chain_climb_1 with fade
    pause
    $ in_menu = True
    while in_menu:
        menu:
            "Climb":
                if cave_flags['ascent']:
                    scene bg_cave_interact_ascent_chain_climb_2 with dissolve
                    pause .5
                    scene bg_cave_interact_ascent_chain_climb_3 with dissolve
                    pause .5
                    scene bg_cave_interact_ascent_chain_climb_4 with dissolve
                    pause .5
                    scene bg_cave_interact_ascent_chain_climb_5 with dissolve
                    p "Huff... urgh..."
                    p "Almost - "
                    scene bg_black
                    "{b}{i}{size=69}CRACK{/size}{/i}{/b}"
                    p "Ahhh!!!"
                    scene bg_cave_interact_ascent_chain_climb_6 with dissolve
                    p "That was close..."
                    scene bg_cave_interact_ascent_chain_climb_7 with dissolve
                    if cave_flags['fell_down'] == 3:
                        p "Thought gravity was going to get me again for sure."
                    p "The tar must have given out."
                    scene bg_cave_interact_hook_break with dissolve
                    p "Guess I'm lucky it held as long as it did, though."
                    scene bg_cave_interact_ascent_chain_climb_8 with dissolve
                    p "It's a long way down..."
                    scene bg_cave_interact_ascent_chain_climb_9 with dissolve
                    p "I'll have to find another way back to the ground."
                    p "No way forward now but... uh, forward."
                    $ cave_mast_walked = False
                    menu:
                        "How should I cross the mast?"
                        "Walk. I'm no coward!":
                            scene bg_cave_mast_walk_0 with fade
                            pause 1.0
                            scene bg_cave_mast_walk_1 with fade
                            p "Why did I think this was a good idea? I should've been a coward!"
                            if cave_flags['fell_down'] == 3:
                                p "Why do I keep challenging gravity?!"
                            scene bg_cave_mast_walk_2 with dissolve
                            p "Breathe and walk. Breathe and walk."
                            p "Don't look down... even if you already know what's there."
                            $ cave_mast_walked = True
                        "Crawl! I'm no idiot.":
                            scene bg_cave_mast_crawl_1 with fade
                            p "Slow and steady. Right."
                            p "Right?"
                            if cave_flags['fell_down'] == 3:
                                p "I know better than to challenge gravity again."
                                p "I've learned my lesson."
                            scene bg_cave_mast_crawl_2 with dissolve
                            p "At least I can't see the ground from here."
                            p "If I ever get to tell this story, I'll say I walked across this."
                    scene bg_cave_mast_walk_3 with fade
                    p "I'm never doing that again."
                    if cave_flags['journal_read']:
                        p "Time to look for this safe."
                    else:
                        p "Why did I even climb up here in the first place?"
                    $ in_menu = False
                    $ renpy.notify('The [Grappling Hook] broke! Find another way back.')
                    jump cave_ship_top
                    

                else:
                    scene bg_cave_interact_ascent_chain_climb_2 with dissolve
                    pause 0.5
                    p "Uh oh..."
                    pause 0.5
                    scene bg_cave_interact_ascent_chain_climb_fail_1 with dissolve
                    pause .25
                    p "Aw hell."
                    pause 0.5
                    scene bg_cave_interact_ascent_chain_climb_fail_2 with dissolve
                    pause .5
                    scene bg_cave_interact_ascent_chain_climb_fail_3 with dissolve
                    pause 0.5
                    "{b}{i}{size=69}CRASH{/size}{/i}{/b}"
                    p "Ow..."
                    if cave_flags['fell_down'] == 1:
                        p "I can't believe I did that again."
                    elif cave_flags['fell_down'] > 1:
                        p "How do I keep doing this?"
                    $ cave_flags['fell_down'] += 1
                    $ inv.append('cave_chain')
                    $ cave_flags['false_ascent'] = False
                    $ cave_flags['false_ascent_attempted'] = True
                    $ renpy.notify("Acquired a [Chain]! ...again.")
                    $ in_menu = False
                    if cave_flags['fell_down'] == 1:
                        $ renpy.notify('Acquired [Shame] and a [Small Bruise]!')
                    elif cave_flags['fell_down'] == 2:
                        $ renpy.notify('Your [Shame] and your [Bruise] both increased in size!')
                    elif cave_flags['fell_down'] == 3:
                        $ renpy.notify('You are now more [Bruise] than man!')
                        jump cave_ascent
            "Leave":
                $ in_menu = False
                jump cave_ascent

label interact_with_cave_mast:
    scene bg_cave_interact_ascent with fade

    $ in_menu = True
    while in_menu:
        menu(x=.2, y=.35):
            "Inspect":
                p "That looks pretty sturdy... for a broken piece of ship, anyway."
                p "I wonder if it could support my weight."
            "Climb" if not cave_flags['climbed_flag']:
                scene bg_cave_interact_ascent_flag_climb_1 with dissolve
                pause 0.5
                p "Hoik!"
                scene bg_cave_interact_ascent_flag_climb_2 with dissolve
                pause
                p "Maybe I can get up here if I just..."
                p "Uh..."
                pause .25
                scene bg_cave_interact_ascent_flag_climb_3 with dissolve
                pause .25
                scene bg_cave_interact_ascent_flag_climb_4 with dissolve
                pause .5
                p "Owww."
                if cave_flags['fell_down'] == 1:
                    p "I can't believe I did that again."
                elif cave_flags['fell_down'] > 1:
                    p "How do I keep doing this?"
                $ cave_flags['fell_down'] += 1
                $ cave_flags['climbed_flag'] = True
                $ in_menu = False
                if cave_flags['fell_down'] == 1:
                    $ renpy.notify('Acquired [Shame] and a [Small Bruise]!')
                elif cave_flags['fell_down'] == 2:
                    $ renpy.notify('Your [Shame] and your [Bruise] both increased in size!')
                elif cave_flags['fell_down'] == 3:
                    $ renpy.notify('You are now more [Bruise] than man!')
                jump cave_ascent
            "Leave":
                $ in_menu = False
                jump cave_ascent

# cave_broadside

label interact_with_cave_chain:
    scene bg_cave_interact_broadside_chain with fade
    $ in_menu = True
    while in_menu:
        menu(x=.2,y=.3):
            "Inspect":
                p "A chain's hanging down from the deck."
                p "Maybe I could climb up there with it?"
            "Climb":
                scene bg_cave_chain_climb_1 with fade
                pause .5
                p "Well, I'll just--"
                pause .25
                scene bg_cave_chain_climb_2 with dissolve
                pause .25
                "Uh?"
                pause .5
                scene bg_cave_chain_climb_3 with dissolve
                pause .25
                scene bg_black with dissolve
                pause 0.5
                p "Ow."
                p "That didn't work quite how I hoped it would."
                if cave_flags['fell_down'] == 1:
                    p "I can't believe I did that again."
                elif cave_flags['fell_down'] > 1:
                    p "How do I keep doing this?"
                $ cave_flags['fell_down'] += 1
                p "I guess I'll hang on to this."
                if cave_flags['fell_down'] == 1:
                    $ renpy.notify('Acquired a [Chain] in exchange for a [Bruise]!')
                elif cave_flags['fell_down'] == 2:
                    $ renpy.notify('Acquired a [Chain] in exchange for enlarging your [Bruise]!')
                $ inv.append('cave_chain')
                $ cave_flags['chain_taken'] = True
                $ in_menu = False
                jump cave_broadside
            "Pull":
                scene bg_cave_chain_careful_1 with fade
                pause
                p "Just to be safe..."
                scene bg_cave_chain_careful_2 with dissolve
                pause .5
                scene bg_cave_chain_careful_3 with dissolve
                pause
                p "Yikes."
                p "Glad I didn't try to climb it."
                p "I guess I'll hang on to this."
                $ renpy.notify("Acquired a [Chain]!")
                $ inv.append('cave_chain')
                $ cave_flags['chain_taken'] = True
                $ in_menu = False
                jump cave_broadside
            "Leave":
                $ in_menu = False
                jump cave_broadside

label interact_with_cave_crack_outside:
    scene bg_cave_interact_crack_outside with fade
    $ in_menu = True
    while in_menu:
        menu(x=.2, y=.25):
            "Inspect":
                p "Looks like a big crack in the hull of the ship."
                p "Maybe I can find something useful in there."
                p "No idea how I'd even get through, though."
            "Break":
                scene bg_cave_interact_crack_outside_really with dissolve
                p "Break it?"
                p "With what, my bare fists?"
                p "Even a really strong guy couldn't pry apart planks this thick. Much less me."
                scene bg_cave_interact_crack_outside with dissolve
            "Leave":
                $ in_menu = False
                jump cave_broadside


# cave_corner

label interact_with_cave_lumber:
    scene bg_cave_interact_lumber with fade
    $ in_menu = True
    while in_menu:
        menu(x=.9, y=.7):
            "Inspect":
                p "It's a pile of debris."
                p "I don't think I'll be able get at anything underneath unless I move it."
            "Move" if not cave_flags['attempted_move']:
                scene bg_cave_interact_lumber_cleanup_fail with fade
                p "Urghhhh..."
                p "This wood is heavy..."
                p "And splintery."
                p "I don't think I'll be able to do this with my bare hands."
                p "I bet I could clear it if I had something to use for leverage..."
                $ cave_flags['attempted_move'] = True
                scene bg_cave_interact_lumber with fade
            "Leave":
                $ in_menu = False
                jump cave_corner

label interact_with_cave_barrel:
    if cave_flags['pile_clear']:
        scene bg_cave_interact_lumber_clear_barrel with fade
    else:
        scene bg_cave_interact_lumber_barrel with fade
    p 'Hmm, maybe I can find something useful here...'
    scene bg_black with fade
    if cave_flags['pile_clear']:
        scene bg_cave_interact_lumber_clear_barrel_2 with fade
    else:
        scene bg_cave_interact_lumber_barrel_2 with fade
    p "Looks like a jar of tar is still intact."
    p "Who knows how long it's been here, though. It's probably all firmed up."
    $ renpy.notify("Acquired some [Tar]!")
    $ inv.append('cave_tar')
    $ cave_flags['tar_taken'] = True
    jump cave_corner


label interact_with_cave_box:
    scene bg_black with fade
    pause .5
    p "Let's see if there's anything useful in here..."
    p "Whoa!"
    scene bg_cave_pistol_1 with fade
    p "I can't believe someone left something like this lying around."
    p "I'd better be extra careful when I -"
    scene bg_cave_pistol_2 with dissolve
    pause 0.5
    scene bg_cave_pistol_3 with dissolve
    p "Ahhh!"
    p "Huh."
    p "That was quieter than expected."
    scene bg_cave_pistol_4 with fade
    p "No bullets, huh."
    p "I wonder if all those sparks mean this is just defective."
    p "I'll hang onto it anyway. Maybe I can come up with a use for it."
    $ renpy.notify("Acquired a [Pistol]!")
    $ inv.append('cave_flintlock')
    jump cave_corner

# cave_ship_grate_view

label interact_with_cave_grate:
    # if not cave_flags['safe_fallen']:
    scene bg_cave_interact_grate with fade
    $ in_menu = True
    while in_menu:
        menu(x=.2, y=.35):
            "Inspect":
                if cave_flags['journal_read']:
                    p 'That must be the safe the captain wrote about...'
                    p 'I need to find a way to get to it.'
                else:
                    p 'Huh, a safe...'
                    p "Maybe there's something valuable inside."
                    p "I should find a way to get to it."
            "Leave":
                $ in_menu = False
                jump cave_ship_grate_view

# cave_deck_2_other

label interact_with_cave_cannonball:
    scene bg_cave_interact_cannonball_1 with fade
    $ in_menu = True
    while in_menu:
        menu(x=.9, y=.35):
            "Inspect":
                p "Some cannonballs. We never had {i}these{/i} on the {i}Handsome Pete{/i}."
            "Take":
                if not cave_flags['cannon_inspected']:
                    p "What am I gonna do with a cannonball? Drag it around for fun?"
                    p "It's not like I even have a cannon."
                else:
                    scene bg_cave_interact_cannonball_2 with dissolve
                    p "Well, now that I've found a cannon, I can deal with dragging one of these around."
                    scene bg_cave_interact_cannonball_3 with dissolve
                    p "It'll be dragging for purpose."
                    scene bg_cave_interact_cannonball_4 with dissolve        
                    pause 0.5
                    scene bg_cave_interact_cannonball_5 with dissolve
                    "{b}{i}{size=69}CRASH{/size}{/i}{/b}"
                    p "Oops."
                    p "At least it didn't crush anything?"
                    p "I'll have to be careful handling this thing."
                    $ inv.append('cave_cannonball')
                    $ in_menu = False
                    $ renpy.notify('Acquired a [Cannonball]!')
                    jump cave_ship_deck_2_other
            "Leave":
                $ in_menu = False
                if not cave_flags['cannon_inspected']:
                    $ renpy.notify('Did not take a [Cannonball] for no reason!')
                jump cave_ship_deck_2_other

# cave_ship_deck_3

label interact_with_cave_ship_door:
    scene bg_cave_interact_ship_door with fade
    $ in_menu = True
    while in_menu:
        menu(x=.7, y=.65):
            "Open":
                scene bg_cave_interact_ship_door_1 with dissolve
                pause 0.5
                scene bg_cave_interact_ship_door_2 with dissolve
                pause 0.5
                $ in_menu = False
                $ cave_flags['door_open'] = True
                jump cave_ship_cabin_1
            "Leave":
                $ in_menu = False
                jump cave_ship_deck_3

# cave_ship_perch

label interact_with_cave_cannon_top:
    scene bg_cave_interact_cannon_upper_1 with fade
    $ in_menu = True
    $ cave_flags['cannon_inspected'] = True
    while in_menu:
        menu(x=.7, y=.4):
            "Inspect":
                p "It's a cannon."
                if cave_flags['crack_stick'] or cave_flags['crack_pick']:
                    if 'cave_pick' in inv:
                        scene bg_cave_ship_crack_nopick with fade
                        pause .5
                    else:
                        scene bg_cave_ship_crack with fade
                        pause .5
                    p "Y'know, I bet this would be more than strong enough to open that crack in the hull..."
                    scene bg_cave_interact_cannon_upper_1 with fade
            "Take":
                scene bg_cave_interact_cannon_upper_really with dissolve
                pause 1
                p "..."
                p "I can't carry this thing around."
                p "Look at the size of it."
                if cave_flags['crack_stick'] or cave_flags['crack_pick']:
                    if cave_flags['pick_taken'] in inv:
                        scene bg_cave_ship_crack_nopick with fade
                        pause .5
                    else:
                        scene bg_cave_ship_crack with fade
                        pause .5
                    p "But if I found a way to get it down to the ground..."
                    p "Maybe I could use it to get out of here?"
                    scene bg_cave_interact_cannon_upper_1 with fade
                else:
                    scene bg_cave_interact_cannon_upper_1 with dissolve
            "Leave":
                $ in_menu = False
                jump cave_ship_perch

    jump cave_ship_perch

# cave_ship_cabin_1

label interact_with_cave_desk:
    scene bg_cave_interact_desk with fade
    $ in_menu = True
    while in_menu:
        menu(x=.25, y=.7):
            "Inspect":
                p "Looks like something's scratched into the underside of this desk..."
                "{b}{i}{size=69}DON'T BELIEVE HIS LIES{/size}{/i}{/b}"
                p "Huh."
                if cave_flags['safe_fallen']:
                    p "You think maybe that was a warning about the safe?"
                    if cave_flags['fell_with_safe']:
                        p "Maybe I should have been more careful."
                else:
                    if cave_flags['journal_read']:
                        p "You figure the crew wrote this about the captain?"
                    else:
                        p "I wonder who wrote this."
                        p "I don't even know what lies I'm supposed to disbelieve."
            
            "Leave":
                $ in_menu = False
                jump cave_ship_cabin_1


# cave_ship_cabin_2

label interact_with_cave_safe:
    scene bg_cave_interact_safe_1 with fade
    $ in_menu = True
    while in_menu:
        menu(x=.25, y=.7):
            "Inspect":
                scene bg_cave_interact_safe_2 with dissolve
                p "I'll just go give it a -"
                scene bg_cave_interact_safe_3 with dissolve
                "CRACK"
                p "-fuck."
                scene bg_cave_interact_safe_4 with dissolve
                pause 0.5
                scene bg_cave_interact_safe_5 with dissolve
                pause 0.5
                scene bg_cave_interact_safe_6 with dissolve
                pause 2.0
                scene bg_black with fade
                pause .5
                if cave_flags['cannon_pushed']:
                    scene bg_cave_interact_safe_7_cannon with fade
                else:
                    scene bg_cave_interact_safe_7 with fade
                pause 1.5
                p "Unnnghhh."
                if cave_flags['cannon_pushed']:
                    scene bg_cave_interact_safe_8_cannon with dissolve
                else:
                    scene bg_cave_interact_safe_8 with dissolve
                p "I'm alive..."
                p "Can't decide if I'm just that lucky or just that cursed."
                if 'cave_cannonball' in inv:
                    p "{i}Definitely{/i} lucky the cannonball I'm carrying around didn't crush anything."
                if cave_flags['fell_down'] == 3:
                    p "How do I keep falling off everything?"
                    p "Am I... stupid?"
                    if not cave_mast_walked:
                        p "I didn't learn my lesson at all."
                $ cave_flags['safe_fallen'] = True
                $ cave_flags['fell_with_safe'] = True
                $ cave_flags['fell_down'] += 1
                $ in_menu = False
                if cave_flags['fell_down'] > 3:
                    $ renpy.notify('Your [Bruise] has consumed your [Soul]!')
                else:
                    $ renpy.notify('Somehow avoided breaking your [Neck]!')
                jump cave_ship_falldown
            "Hey, wait...":
                p "This floor looks really unsafe, I better be-"
                scene bg_cave_interact_safe_cautious_1 with dissolve
                "CRACK"
                p "-cautious."
                scene bg_cave_interact_safe_cautious_2 with dissolve
                pause 0.5
                scene bg_cave_interact_safe_cautious_3 with dissolve
                pause 0.5
                scene bg_cave_interact_safe_cautious_4 with dissolve
                pause 0.5
                scene bg_cave_interact_safe_cautious_5 with fade
                pause 0.5
                p "Yikeseroo!"
                p "Glad I didn't just go try to inspect it like an idiot."
                p "I'd have broken my neck for sure."
                p "I'll find another way down."
                $ cave_flags['safe_fallen'] = True
                $ in_menu = False
                $ renpy.notify('Acquired some [Earned Smugness]!')
                jump cave_ship_cabin_2
            "Leave":
                $ in_menu = False
                jump cave_ship_cabin_2

# cave_ship_end

label interact_with_cave_safe_end:
    if cave_flags['cannon_pushed']:
        scene bg_cave_interact_safe_end_1_cannon with fade
    else:
        scene bg_cave_interact_safe_end_1 with fade

    $ in_menu = True
    while in_menu:
        menu(x=.35, y=.7):
            "Inspect":
                if cave_flags['journal_read']:
                    p "So here's the famous safe. Locked, as expected."
                    if "cave_key" in inv:
                        p "The key I found should unlock it..."
                    else:
                        p "I need to find what happened to the key after he swallowed it."
                else:
                    p "This is a tough safe."
                    p "It's still locked, even after falling."
                    if "cave_key" in inv:
                        p "I wonder if the key I found in the skeleton will unlock this?"
                    else:
                        p "Maybe there's a key around here somewhere."
            "Leave":
                $ in_menu = False
                jump cave_ship_end

# cave_ship_crack

label interact_with_cave_pick:
    scene bg_cave_interact_pick with fade
    $ in_menu = True
    while in_menu:
        menu(x=.75, y=.3):
            "Inspect":
                p "It's a handheld pick."
                p "It seems a lot sturdier than that shovel, if nothing else."
            "Take":
                p "I can definitely find a use for this."
                $ in_menu = False
                $ inv.append('cave_pick')
                $ renpy.notify('Found a [Pick]!')
                $ cave_flags['pick_taken'] = True
                jump cave_ship_crack
            "Leave":
                $ in_menu = False
                jump cave_ship_crack

label interact_with_cave_crack:
    scene bg_cave_interact_crack with fade
    $ in_menu=True
    while in_menu:
        menu(x=.7, y=.2):
            "Inspect":
                p "The same crack in the hull that I saw on the outside."
                p "I thought I would need it to get in, but maybe it's the best way I have to get out..."
                if cave_flags['cannon_pushed']:
                    p "That cannon I pushed down ought to do the trick if I manage to fire it."
            "Think" if cave_flags['crack_stick'] and cave_flags['crack_pick'] and not cave_flags['cannon_pushed']:
                scene bg_cave_interact_crack_thinking with fade
                p "Well, I've tried small measures."
                p "I need to think of something with more firepower..."
                $ cave_flags['crack_hint'] = True
                scene bg_cave_interact_crack with fade
            "Leave":
                $ in_menu = False
                jump cave_ship_crack

# cave_ship_descent

label interact_with_cave_cannon_bottom:
    scene bg_cave_interact_cannon_1 with fade
    $ in_menu = True
    while in_menu:
        menu(x=.35, y=.25):
            "Inspect":
                p "Luckily it landed pointing at the weak spot so I don't have to move it."
                p "I'm not sure I could if I had to."
                if cave_flags['cannon_loaded']:
                    p "I just need to light the fuse."
                    p "Maybe that pistol I picked up would do the trick here?"
                elif 'cave_cannonball' in inv:
                    p "I need to load it with that cannonball I took from the upper decks."
                else:
                    p "It's still unloaded..."
                    p "Maybe there's something I can find to load it in the upper decks?"
            "Leave":
                $ in_menu = False
                jump cave_ship_descent