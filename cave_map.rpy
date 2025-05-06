label cave_center:
    if cave_flags['cannon_fired']:
        scene bg_cavecenter_final
    elif not cave_flags['lantern_taken'] and not 'cave_book' in inv:
        if cave_flags['ascent']:
            scene bg_cavecenter_full_ascent
        else:
            scene bg_cavecenter_full
    elif (cave_flags['lantern_taken'] or cave_flags['lantern_smashed']) and not 'cave_book' in inv:
        if cave_flags['ascent']:
            if cave_flags['campfire_lit']:
                scene bg_cavecenter_fire_book_ascent
            else:
                scene bg_cavecenter_nolantern_ascent
        else:
            if cave_flags['campfire_lit']:
                scene bg_cavecenter_fire_book
            else:
                scene bg_cavecenter_nolantern              
    elif not cave_flags['lantern_taken'] and 'cave_book' in inv:
        if cave_flags['ascent']:
            scene bg_cavecenter_nobook_ascent
        else:
            scene bg_cavecenter_nobook
    elif cave_flags['campfire_lit']:
        if cave_flags['ascent']:
            scene bg_cavecenter_fire_ascent
        else:
            scene bg_cavecenter_fire
    else:
        scene bg_cavecenter_empty

    if curr_map_screen != 'cave_center':
        show screen map_name_display("The Stone Table")
    $ curr_map_screen = 'cave_center'

    call screen cavecenter_nav

    screen cavecenter_nav():
        if not 'cave_book' in inv:
            modal True

            imagebutton auto "bg_cavecenter_book_%s":
                focus_mask True
                tooltip "Old Book"
                if active_item:
                    action [
                        SetVariable('active_item', None),
                        Notify("Looks like that item won't work here...")
                    ]
                else:
                    action Jump ("interact_with_cave_book")

        if not cave_flags['lantern_taken']:
            imagebutton auto "bg_cavecenter_lantern_%s":
                focus_mask True
                tooltip "Lantern"
                if active_item:
                    action [
                        SetVariable('active_item', None),
                        Notify("Looks like that item won't work here...")
                    ]
                else:
                    action Jump ("interact_with_cave_lantern")

        if not inventory_open:
            use arrow("to Left Fork", "cave_left", (.05, .68), 170)
            use arrow("to Beach", "cave_beach", (0.5, .95), 93)
            use arrow("to Right Fork", "cave_right", (.95, .55), 15)
            use inventory_button
        if active_item:
            use item_active
        use map_tooltip_display


label cave_left:
    if cave_flags['pile_dug']:
        if cave_flags['skeleton_hat']:
            scene bg_cave_left_final_hatoff
        else:
            scene bg_cave_left_final_hat
    elif cave_flags['cannon_fired']:
        if cave_flags['skeleton_hat']:
            scene bg_cave_left_cannonfired_hatoff
        else:
            scene bg_cave_left_cannonfired_hat
    elif cave_flags['campfire_lit']:
        if cave_flags['skeleton_hat'] and not cave_flags['shovel_taken']:
            scene bg_cave_left_firehat
        elif not cave_flags['skeleton_hat'] and cave_flags['shovel_taken']:
            scene bg_cave_left_fireshovel
        elif cave_flags['skeleton_hat'] and cave_flags['shovel_taken']:
            scene bg_cave_left_cleared
        else:
            scene bg_cave_left_fire
    else:
        if cave_flags['skeleton_hat'] and not cave_flags['shovel_taken']:
            scene bg_cave_left_hat
        elif not cave_flags['skeleton_hat'] and cave_flags['shovel_taken']:
            scene bg_cave_left_shovel
        elif cave_flags['skeleton_hat'] and cave_flags['shovel_taken']:
            scene bg_cave_left_hatshovel
        else:
            scene bg_cave_left

    if curr_map_screen != 'cave_left':
        show screen map_name_display("The Fork Left")
    $ curr_map_screen = 'cave_left'

    call screen cave_left_nav

    screen cave_left_nav():
        if not inventory_open:
            use arrow("to Stone Table", "cave_center", (.5, .95), 80)
            use arrow("to Pile of Kismet", "cave_treasure", (0.05, 0.45), -115)
            use arrow("to Captain's Rest", "cave_skeleton", (0.4, 0.32), -105)
            use arrow("(to Tent)", "cave_tent", (.85, .45), -35)
            use inventory_button
        if active_item:
            use item_active
        use map_tooltip_display

label cave_treasure:
    if cave_flags['pile_dug']:
        scene bg_cave_treasure_final
    elif cave_flags['cannon_fired']:
        scene bg_cave_treasure_cannonfired
    else:
        scene bg_cave_treasure

    if curr_map_screen != 'cave_treasure':
        show screen map_name_display("The Pile of Kismet")
    $ curr_map_screen = 'cave_treasure'

    call screen cave_treasure_nav

    screen cave_treasure_nav():
        if 'cave_shovel' not in inv and not cave_flags['shovel_broken']:    
            imagebutton auto "bg_cave_treasure_full_shovel_%s":
                focus_mask True
                tooltip "Shovel"
                if active_item:
                    action [
                        SetVariable('active_item', None),
                        Notify("Looks like that item won't work here...")
                    ]
                else:
                    action Jump ("interact_with_cave_shovel")

        
        if cave_flags['pile_dug']:
            imagebutton auto "bg_cave_treasure_final_chest_%s":
                focus_mask True
                tooltip "Treasure Chest"
                if active_item:
                    if active_item == 'cave_safekey':
                        action [
                            SetVariable('active_item', None),
                            Jump ('cave_act_end_cave')
                        ]
                    else:
                        action [
                            SetVariable('active_item', None),
                            Notify("Looks like that item won't work here...")
                        ]

                else:
                    action Jump ("interact_with_cave_treasure_3")            
        elif cave_flags['cannon_fired']:
            imagebutton auto "bg_cave_treasure_cannonfired_pile_%s":
                focus_mask True
                tooltip "Dirt Pile"
                if active_item:
                    if active_item == 'cave_pick':
                        action [
                            SetVariable('active_item', None),
                            Jump ('cave_act_dig_pick')
                        ]
                    else:
                        action [
                            SetVariable('active_item', None),
                            Notify("Looks like that item won't work here...")
                        ]

                else:
                    action Jump ("interact_with_cave_treasure_2")
        else:
            imagebutton auto "bg_cave_treasure_pile_%s":
                focus_mask True
                tooltip "Dirt Pile"
                if active_item:
                    if active_item == 'cave_shovel':
                        action [
                            SetVariable('active_item', None),
                            Jump ('cave_act_dig')
                        ]
                    else:
                        action [
                            SetVariable('active_item', None),
                            Notify("Looks like that item won't work here...")
                        ]

                else:
                    action Jump ("interact_with_cave_treasure")

        if not inventory_open:
            use arrow("(to Left Fork)","cave_left",(0.3, .95),110)
            use arrow("(to Captain's Rest)","cave_skeleton",(0.75, .95),75)            
            use arrow("(to Beach)","cave_beach",(0.05, .6),170)
            use inventory_button
        if active_item:
            use item_active
        use map_tooltip_display


label cave_skeleton:
    if cave_flags['skeleton_hat']:
        if 'cave_key' in inv or 'cave_safekey' in inv:
            scene bg_skeleton_a1_nokey
        else:
            scene bg_skeleton_a1_hatoff
    else:
        scene bg_skeleton_a1

    if curr_map_screen != 'cave_skeleton':
        show screen map_name_display("The Captain's Rest")
    $ curr_map_screen = 'cave_skeleton'

    call screen cave_skeleton_nav

    screen cave_skeleton_nav():
        if cave_flags['skeleton_hat']:
            if 'cave_key' not in inv and 'cave_safekey' not in inv:
                imagebutton auto "bg_skeleton_a1_hatoff_key_%s":
                    focus_mask True
                    if active_item:
                        action [
                            SetVariable('active_item', None),
                            Notify("Looks like that item won't work here...")
                        ]
                    else:
                        action Jump ("interact_with_cave_skeleton_key")

            imagebutton auto "bg_skeleton_a1_hatoff_bottle_%s":
                focus_mask True
                tooltip "Rum Bottle"
                if active_item:
                    action [
                        SetVariable('active_item', None),
                        Notify("Looks like that item won't work here...")
                    ]
                else:
                    action Jump ("interact_with_cave_bottle")


        else:
            imagebutton auto "bg_skeleton_a1_bottle_%s":
                focus_mask True
                tooltip "Rum Bottle"
                if active_item:
                    action [
                        SetVariable('active_item', None),
                        Notify("Looks like that item won't work here...")
                    ]
                else:                    
                    action Jump ("interact_with_cave_bottle")

            imagebutton auto "bg_skeleton_a1_hat_%s":
                focus_mask True
                tooltip "Fancy Hat"
                if active_item:
                    action [
                        SetVariable('active_item', None),
                        Notify("Looks like that item won't work here...")
                    ]
                else:
                    action Jump ("interact_with_cave_skeleton_hat")

        if cave_flags['journal_read'] and 'cave_key' not in inv and 'cave_safekey' not in inv:
            timer 1.0 action Notify("Hmm...")
            timer 7.0 action Notify("If I were a key, where would I be?")
            timer 10.0 action [SetVariable("active_item", None), Jump('cave_skeleton_a2')]

        if not inventory_open:
            use arrow("(to Left Fork)","cave_left",(0.3, .95),110)
            use arrow("(to Tent)","cave_tent",(0.95, .7),47)
            use arrow("(to Pile of Kismet)","cave_treasure",(0.05, .5),190)
            use inventory_button
        if active_item:
            use item_active
        use map_tooltip_display

label cave_skeleton_a2:
    if cave_flags['skeleton_hat']:
        scene bg_skeleton_a2
    else:
        scene bg_skeleton_a2_hat
    call screen cave_skeleton_a2_nav

    screen cave_skeleton_a2_nav():
        imagebutton auto "bg_skeleton_a2_key_%s":
            focus_mask True
            tooltip "Skeleton's Key"
            action Jump('interact_with_cave_skeleton_key')

        use map_tooltip_display

label cave_tent:
    if cave_flags['campfire_lit']:
        scene bg_cavetent_fire
    elif cave_flags['lantern_smashed']:
        scene bg_cavetent_ready
    else:
        scene bg_cavetent

    if curr_map_screen != 'cave_tent':
        show screen map_name_display("The Abandoned Tent")
    $ curr_map_screen = 'cave_tent'

    call screen cave_tent_nav

    screen cave_tent_nav():
        if cave_flags['campfire_lit']:
            imagebutton auto "bg_cavetent_fire_pit_%s":
                focus_mask True
                tooltip "Campfire"
                if active_item:
                    if active_item == "cave_book":
                        action [
                            SetVariable('active_item', None),
                            Jump("cave_act_fire_book")
                        ]
                    elif active_item == 'cave_tar':
                        if cave_flags['hot_tar']:
                            action [
                                SetVariable('active_item', None),
                                Notify('The tar is already hot...')
                            ]
                        else:
                            action [
                                SetVariable('active_item', None),
                                Jump('cave_act_fire_tar')
                            ]
                    else:
                        action [
                            SetVariable('active_item', None),
                            Notify("Looks like that item won't work here...")
                        ]
                else:
                    action Jump ("interact_with_cave_lit_fire")

        elif cave_flags['lantern_smashed']:
            imagebutton auto "bg_cavetent_ready_pit_%s":
                focus_mask True
                tooltip "Campfire"
                if active_item:
                    if active_item == "cave_flintlock":
                        action [
                            SetVariable('active_item', None),
                            Jump("cave_act_fire_flintlock")
                        ]   
                    else:
                        action [
                            SetVariable('active_item', None),
                            Notify("Looks like that item won't work here...")
                        ]
                else:
                    action Jump ("interact_with_cave_ready_fire")
        else:
            imagebutton auto "bg_cavetent_pit_%s":
                focus_mask True
                tooltip "Campfire"
                if active_item:
                    if active_item == "cave_lantern":
                        action [
                            SetVariable('active_item', None),
                            Jump ('cave_act_fire_lantern')
                        ]                        
                    elif active_item == "cave_flintlock":
                        action [
                            SetVariable('active_item', None),
                            Jump("cave_act_fire_flintlock")
                        ]                        
                    else:
                        action [
                            SetVariable('active_item', None),
                            Notify("Looks like that item won't work here...")
                        ]
                else:
                    action Jump ("interact_with_cave_unlit_fire")                    
        if not inventory_open:
            use arrow("(to Left Fork)","cave_left",(0.45, .95),100)
            use arrow("(to Captain's Rest)","cave_skeleton",(0.05, .5),170)
            use inventory_button
        if active_item:
            use item_active
        use map_tooltip_display

label cave_right:
    if cave_flags['cannon_fired']:
        scene bg_cave_right_final
    elif cave_flags['ascent'] or cave_flags['false_ascent']:
        if 'cave_book' in inv:
            scene bg_cave_right_ascent
        else:
            scene bg_cave_right_ascent_book
    elif cave_flags['pile_clear']:
        if cave_flags['chain_taken']:
            if 'cave_book' in inv:
                scene bg_cave_right_clear
            else:
                scene bg_cave_right_clear_book
        else:
            if 'cave_book' in inv:
                scene bg_cave_right_pile
            else:
                scene bg_cave_right_pile_book
    elif cave_flags['chain_taken']:
        if 'cave_book' in inv:
            scene bg_cave_right_chain
        else:
            scene bg_cave_right_chain_book
    else:
        scene bg_cave_right

    if curr_map_screen != 'cave_right':
        show screen map_name_display("The Fork Right")
    $ curr_map_screen = 'cave_right'

    call screen cave_right_nav

    screen cave_right_nav():
        if not inventory_open:
            use arrow("(to Stone Table)","cave_center",(0.55, .95),100)
            use arrow("(to Ascent)","cave_ascent",(0.25, 0.75),220)
            use arrow("(to Ingress)","cave_broadside",(0.65, 0.55),-80)
            use arrow("(to Water's Edge)","cave_corner",(0.85, 0.8),-55)
            use inventory_button
        if active_item:
            use item_active
        use map_tooltip_display


label cave_ascent:
    if cave_flags['cannon_fired']:
        scene bg_cave_ascent_final
    elif cave_flags['ascent'] or cave_flags['false_ascent']:
        scene bg_cave_ascent_mast_clear
    else:
        scene bg_cave_ascent

    if curr_map_screen != 'cave_ascent':
        show screen map_name_display("The Wreck - Ascent")
    $ curr_map_screen = 'cave_ascent'

    call screen cave_ascent_nav

    screen cave_ascent_nav():
        if not cave_flags['cannon_fired']:
            if cave_flags['ascent'] or cave_flags['false_ascent']:
                imagebutton auto "bg_cave_ascent_mast_clear_chain_%s":
                    focus_mask True
                    tooltip "Chain Upwards"
                    if active_item:
                        action [
                            SetVariable('active_item', None),
                            Notify("Looks like that item won't work here...")
                        ]
                    else:
                        action Jump ("interact_with_cave_ascent")
            else:
                imagebutton auto "bg_cave_ascent_mast_%s":
                    focus_mask True
                    tooltip "Mast"
                    if active_item:
                        if active_item == 'cave_chain':
                            if not cave_flags['false_ascent_attempted']:
                                action [
                                    SetVariable('active_item', None),
                                    Jump('cave_act_ascent_false')
                                ]
                            else:
                                action [
                                    SetVariable('active_item', None),
                                    Notify("I need to find some way to secure the [Chain]...")
                                ]
                        elif active_item == 'cave_grappling_hook':
                            action [
                                SetVariable('active_item', None),
                                Jump('cave_act_ascent')
                            ]
                        else:
                            action [
                                SetVariable('active_item', None),
                                Notify("Looks like that item won't work here...")
                            ]
                    else:
                        action Jump ("interact_with_cave_mast")

        if not inventory_open:
            use arrow("(to Stone Table)","cave_center",(0.3, .95),110)
            use arrow("(to Ingress)","cave_broadside",(0.9, .75),20)
            use inventory_button
        if active_item:
            use item_active
        use map_tooltip_display

label cave_broadside:
    if cave_flags['cannon_fired']:
        scene bg_cave_broadside_final
    else:
        scene bg_cave_broadside

    if curr_map_screen != 'cave_broadside':
        show screen map_name_display("The Wreck - Ingress")
    $ curr_map_screen = 'cave_broadside'

    call screen cave_broadside_nav

    screen cave_broadside_nav():
        if not cave_flags['chain_taken']:
            imagebutton auto "bg_cave_broadside_chain_%s":
                focus_mask True
                tooltip "Chain"
                if active_item:
                    action [
                        SetVariable('active_item', None),
                        Notify("Looks like that item won't work here...")
                    ]
                else:                
                    action Jump ("interact_with_cave_chain")

        if not cave_flags["crack_stick_outside"] and not cave_flags['cannon_fired']:
            imagebutton auto "bg_cave_broadside_boards_%s":
                focus_mask True
                tooltip "Crack in the Hull"
                if active_item:
                    if active_item == "cave_shaft":
                        action [
                            SetVariable('active_item', None),
                            Jump("cave_act_crack_outside_stick")
                        ]
                    else:
                        action [
                            SetVariable('active_item', None),
                            Notify("Looks like that item won't work here...")
                        ]
                else:                
                    action Jump ("interact_with_cave_crack_outside")

        if not inventory_open:
            use arrow("(to Right Fork)","cave_right",(0.5, .95),110)
            use arrow("(to Water's Edge)","cave_corner",(0.9, .74),40)
            use arrow("(to Ascent)","cave_ascent",(0.05, .65),160)
            if cave_flags['cannon_fired']:
                use arrow("(to Egress)","cave_ship_crack",(0.3, .85),-60)
            use inventory_button
        if active_item:
            use item_active
        use map_tooltip_display


label cave_corner:
    if cave_flags['pile_clear']:
        scene bg_cave_corner_clear
    else:
        scene bg_cave_corner_pile

    if curr_map_screen != 'cave_corner':
        show screen map_name_display("The Water's Edge")
    $ curr_map_screen = 'cave_corner'

    call screen cave_corner_nav

    screen cave_corner_nav():
        if cave_flags['pile_clear']:
            if not cave_flags['tar_taken']:
                imagebutton auto "bg_cave_corner_clear_barrel_%s":
                    focus_mask True
                    tooltip "Barrel"
                    if active_item:
                        action [
                            SetVariable('active_item', None),
                            Notify("Looks like that item won't work here...")
                        ]
                    else:
                        action Jump ("interact_with_cave_barrel")
            
            if 'cave_flintlock' not in inv:
                imagebutton auto "bg_cave_corner_clear_box_%s":
                    focus_mask True
                    tooltip "Crate"
                    if active_item:
                        action [
                            SetVariable('active_item', None),
                            Notify("Looks like that item won't work here...")
                        ]
                    else:
                        action Jump ("interact_with_cave_box")

        else:
            if not cave_flags['tar_taken']:
                imagebutton auto "bg_cave_corner_pile_barrel_%s":
                    focus_mask True
                    tooltip "Barrel"
                    if active_item:
                        action [
                            SetVariable('active_item', None),
                            Notify("Looks like that item won't work here...")
                        ]
                    else:
                        action Jump ("interact_with_cave_barrel")
            imagebutton auto "bg_cave_corner_pile_lumber_%s":
                focus_mask True
                tooltip "Debris"
                if active_item:
                    if active_item == "cave_shaft":
                        action [
                            SetVariable('active_item', None),
                            Jump('cave_act_lumber')
                        ]
                    else:    
                        action [
                            SetVariable('active_item', None),
                            Notify("Looks like that item won't work here...")
                        ]
                else:
                    action Jump ("interact_with_cave_lumber")
            
            imagebutton auto "bg_cave_corner_pile_box_%s":
                focus_mask True
                tooltip "Crate"
                if active_item:
                    action [
                        SetVariable('active_item', None),
                        Notify("Looks like that item won't work here...")
                    ]
                else:
                    action [
                        SetVariable('active_item', None),
                        Notify("I can't reach that without clearing the debris...")
                    ]

        if not inventory_open:
            use arrow("(to Right Fork)","cave_right",(0.25, .95),95)
            use arrow("(to Ingress)","cave_broadside",(0.05, .7),145)
            use arrow("(to Beach)","cave_beach",(0.75, .95),60)
            use inventory_button
        if active_item:
            use item_active
        use map_tooltip_display

label cave_beach:
    scene bg_cave_beach

    if curr_map_screen != 'cave_beach':
        show screen map_name_display("The Empty Beach")
    $ curr_map_screen = 'cave_beach'

    call screen cave_beach_nav

    screen cave_beach_nav():
        if not inventory_open:
            use arrow("(to Stone Table)","cave_center",(0.5, .85),90)
            use arrow("(to Water's Edge)","cave_corner",(.05, .75),-140)
            use arrow("(to Pile of Kismet)","cave_treasure",(.85, .555),-40)
            use inventory_button
        if active_item:
            use item_active
        use map_tooltip_display

label cave_ship_top:
    scene bg_cave_ship_top

    if curr_map_screen != 'cave_ship_top':
        show screen map_name_display("The Wreck - Aft")
    $ curr_map_screen = 'cave_ship_top'

    call screen cave_ship_top_nav

    screen cave_ship_top_nav():
        if not inventory_open:
            use arrow("(to Grate)","cave_ship_grate_view",(0.05, .5),160)
            use arrow("(to Port)","cave_ship_deck_2",(0.25, .15),-35)
            use inventory_button
        if active_item:
            use item_active
        use map_tooltip_display

label cave_ship_grate_view:
    scene bg_cave_ship_grate_view

    if curr_map_screen != 'cave_ship_grate_view':
        show screen map_name_display("The Wreck - Grate")
    $ curr_map_screen = 'cave_ship_grate_view'

    call screen cave_ship_grate_view_nav

    screen cave_ship_grate_view_nav():
        if not cave_flags['safe_fallen']:
            imagebutton auto 'bg_cave_ship_grate_view_grate_%s':
                focus_mask True
                tooltip "Grate"
                if active_item:
                    action [
                        SetVariable('active_item', None),
                        Notify("Looks like that item won't work here...")
                    ]
                else:                    
                    action Jump ("interact_with_cave_grate")

        if not inventory_open:
            use arrow("(to Aft)","cave_ship_top",(0.65, .95),105)
            use inventory_button
        if active_item:
            use item_active
        use map_tooltip_display


label cave_ship_deck_2:
    scene bg_cave_ship_deck_2

    if curr_map_screen != 'cave_ship_deck_2':
        show screen map_name_display("The Wreck - Port")
    $ curr_map_screen = 'cave_ship_deck_2'

    call screen bg_cave_ship_deck_2_nav

    screen bg_cave_ship_deck_2_nav():  
        if not inventory_open:          
            use arrow("(to Aft)","cave_ship_top",(0.5, .95),90)
            use arrow("(to Starboard)","cave_ship_deck_2_other",(0.85, .45),20)
            use arrow("(to Middecks)","cave_ship_deck_3",(0.2, .15),-100)
            use inventory_button
        if active_item:
            use item_active
        use map_tooltip_display

label cave_ship_deck_2_other:
    if cave_flags['cannon_loaded'] or 'cave_cannonball' in inv:
        scene bg_cave_deck_2_other_noball
    else:
        scene bg_cave_deck_2_other

    if curr_map_screen != 'cave_ship_deck_2_other':
        show screen map_name_display("The Wreck - Starboard")
    $ curr_map_screen = 'cave_ship_deck_2_other'

    call screen bg_cave_ship_deck_2_other_nav

    screen bg_cave_ship_deck_2_other_nav():
        if not cave_flags['cannon_loaded'] and not 'cave_cannonball' in inv:
            imagebutton auto 'bg_cave_deck_2_other_cannonballs_%s':
                focus_mask True
                tooltip "Cannonballs"
                if active_item:
                    action [
                        SetVariable('active_item', None),
                        Notify("Looks like that item won't work here...")
                    ]
                else:                    
                    action Jump ("interact_with_cave_cannonball")

        if not inventory_open:            
            use arrow("(to Port)","cave_ship_deck_2",(0.9, .5),25)
            use inventory_button
        if active_item:
            use item_active
        use map_tooltip_display


label cave_ship_deck_3:
    if not cave_flags['door_open']:
        scene bg_cave_ship_deck_3
    else:
        scene bg_cave_ship_deck_3_dooropen
    if curr_map_screen != 'cave_ship_deck_3':
        show screen map_name_display("The Wreck - Middecks")
    $ curr_map_screen = 'cave_ship_deck_3'
    call screen bg_cave_ship_deck_3_nav

    screen bg_cave_ship_deck_3_nav():
        if not inventory_open:            
            if not cave_flags["door_open"]:
                imagebutton auto 'bg_cave_ship_deck_3_door_%s':
                    focus_mask True
                    tooltip "Cabin Doors"
                    if active_item:
                        action [
                            SetVariable('active_item', None),
                            Notify("Looks like that item won't work here...")
                        ]
                    else:                    
                        action Jump ("interact_with_cave_ship_door")
            else:
                use arrow("(to Outer Cabin)","cave_ship_cabin_1",(0.85, .7),-5)
            use arrow("(to Port)","cave_ship_deck_2",(0.75, .95),-10)
            use arrow("(to Fore)","cave_ship_deck_4",(0.45, .25),215)
            use inventory_button
        if active_item:
            use item_active
        use map_tooltip_display



label cave_ship_deck_4:
    if cave_flags["door_open"]:
        scene bg_cave_ship_deck_4_dooropen
    else:
        scene bg_cave_ship_deck_4
    if curr_map_screen != 'cave_ship_deck_4':
        show screen map_name_display("The Wreck - Fore")
    $ curr_map_screen = 'cave_ship_deck_4'
    call screen bg_cave_ship_deck_4_nav

    screen bg_cave_ship_deck_4_nav():
        if not inventory_open:            
            use arrow("(to Middecks)","cave_ship_deck_3",(0.4, .15),-60)
            use arrow("(to Perch)","cave_ship_perch",(0.95, .5),0)
            use arrow("(to Descent)","cave_ship_descent",(0.75, .85),75)
            use inventory_button
        if active_item:
            use item_active
        use map_tooltip_display

label cave_ship_perch:
    if cave_flags["cannon_pushed"]:
        if not cave_flags["safe_fallen"]:
            scene bg_cave_ship_perch_nocannon
        elif "cave_safekey" not in inv:
            scene bg_cave_ship_perch_safe_nocannon
        else:
            scene bg_cave_ship_perch_safe_opened_nocannon
    else:
        if not cave_flags["safe_fallen"]:
            scene bg_cave_ship_perch
        elif "cave_safekey" not in inv:
            scene bg_cave_ship_perch_safe
        else:
            scene bg_cave_ship_perch_safe_opened

    if curr_map_screen != 'cave_ship_perch':
        show screen map_name_display("The Wreck - Perch")
    $ curr_map_screen = 'cave_ship_perch'

    call screen bg_cave_ship_perch_nav

    screen bg_cave_ship_perch_nav():
        if not cave_flags["cannon_pushed"]:
            imagebutton auto 'bg_cave_ship_perch_cannon_%s':
                focus_mask True
                tooltip "Cannon"
                if active_item:
                    if active_item == "cave_shaft":
                        action [
                            SetVariable('active_item', None),
                            Jump('cave_act_cannon_upper')
                        ]
                    else:
                        action [
                            SetVariable('active_item', None),
                            Notify("Looks like that item won't work here...")
                        ]
                else:                    
                    action Jump ("interact_with_cave_cannon_top")

        if not inventory_open:
            use arrow("(to Fore)","cave_ship_deck_4",(0.4, .95),108)
            use inventory_button
        if active_item:
            use item_active
        use map_tooltip_display

label cave_ship_descent:
    if cave_flags['cannon_fired']:
        if 'cave_safekey' in inv:
            scene bg_cave_ship_descent_clear_safe_opened
        elif cave_flags['safe_fallen']:
            scene bg_cave_ship_descent_clear_safe
        else:
            scene bg_cave_ship_descent_clear
    else:
        if 'cave_safekey' in inv:
            if cave_flags['cannon_pushed']:
                scene bg_cave_ship_descent_safe_opened_cannon
            else:
                scene bg_cave_ship_descent_safe_opened
        elif cave_flags['safe_fallen']:
            if cave_flags['cannon_pushed']:
                scene bg_cave_ship_descent_safe_cannon
            else:
                scene bg_cave_ship_descent_safe
        else:
            if cave_flags['cannon_pushed']:
                scene bg_cave_ship_descent_cannon
            else:
                scene bg_cave_ship_descent

    if not cave_flags['pick_taken']:
        show bg_cave_ship_descent_pick

    if curr_map_screen != 'cave_ship_descent':
        show screen map_name_display("The Wreck - Descent")
    $ curr_map_screen = 'cave_ship_descent'

    call screen bg_cave_ship_descent_nav

    screen bg_cave_ship_descent_nav():
        if cave_flags["cannon_pushed"] and not cave_flags["cannon_fired"]:
            imagebutton auto 'bg_cave_ship_descent_cannon_%s':
                focus_mask True
                if active_item:
                    if active_item == 'cave_cannonball':
                        action [
                            SetVariable('active_item', None),
                            Jump("cave_act_cannon_cannonball")
                        ]
                    elif active_item == 'cave_flintlock':
                        if cave_flags['cannon_loaded']:
                            action [
                                SetVariable('active_item', None),
                                Jump("cave_act_cannon_flintlock")
                            ]
                        else:
                            action [
                                SetVariable('active_item', None),
                                Notify("I need to load it before I try to fire it...")
                            ]
                    else:
                        action [
                            SetVariable('active_item', None),
                            Notify("Looks like that item won't work here...")
                        ]
                else:                    
                    action Jump ("interact_with_cave_cannon_bottom")

        if not inventory_open:
            use arrow("(to Fore)","cave_ship_deck_4",(0.3, .9),120)
            use arrow("(to Egress)","cave_ship_crack",(0.2, .2),205)
            use arrow("(to Terminus)","cave_ship_end",(0.75, .25),-75)
            use inventory_button
        if active_item:
            use item_active
        use map_tooltip_display

label cave_ship_end:
    if 'cave_safekey' in inv:
        scene bg_cave_ship_end_safe_opened   
    elif cave_flags['safe_fallen']:
        scene bg_cave_ship_end
    else:
        scene bg_cave_ship_end_nosafe

    if curr_map_screen != 'cave_ship_end':
        show screen map_name_display("The Wreck - Terminus")
    $ curr_map_screen = 'cave_ship_end'

    call screen bg_cave_ship_end_nav

    screen bg_cave_ship_end_nav():
        if cave_flags["safe_fallen"] and not 'cave_safekey' in inv:
            imagebutton auto 'bg_cave_ship_end_safe_%s':
                focus_mask True
                tooltip "Captain's Safe"
                if active_item:
                    if active_item == 'cave_key':
                        action [
                            SetVariable('active_item', None),
                            Jump("cave_act_safe_key")
                        ]
                    else:
                        action [
                            SetVariable('active_item', None),
                            Notify("Looks like that item won't work here...")
                        ]
                else:                    
                    action Jump ("interact_with_cave_safe_end")
        if not inventory_open:
            use arrow("(to Descent)","cave_ship_descent",(0.5, .95),90)
            use arrow("(to Egress)","cave_ship_crack",(0.05, .95),135)
            use inventory_button
        if active_item:
            use item_active
        use map_tooltip_display

label cave_ship_crack:
    if cave_flags['cannon_fired']:
        if cave_flags['pick_taken']:
            scene bg_cave_ship_crack_open_nopick
        else:
            scene bg_cave_ship_crack_open
    else:
        if cave_flags['pick_taken']:
            scene bg_cave_ship_crack_nopick
        else:
            scene bg_cave_ship_crack

    if curr_map_screen != 'cave_ship_crack':
        show screen map_name_display("The Wreck - Egress")
    $ curr_map_screen = 'cave_ship_crack'
    call screen bg_cave_ship_crack_nav

    screen bg_cave_ship_crack_nav():
        if not cave_flags["cannon_fired"]:
            imagebutton auto 'bg_cave_ship_crack_boards_%s':
                focus_mask True
                tooltip "Crack in the Hull"
                if active_item:
                    if active_item == 'cave_pick':
                        if cave_flags['crack_pick']:
                            action [
                                SetVariable('active_item', None),
                                Notify("I already tried that...")
                            ]
                        else:
                            action [
                                SetVariable('active_item', None),
                                Jump("cave_act_crack_pick")
                            ]
                    elif active_item == "cave_shaft":
                        if cave_flags['crack_stick']:
                            action [
                                SetVariable('active_item', None),
                                Notify("I already tried that...")
                            ]
                        else:
                            action [
                                SetVariable('active_item', None),
                                Jump("cave_act_crack_stick")
                            ]                      
                    else:
                        action [
                            SetVariable('active_item', None),
                            Notify("Looks like that item won't work here...")
                        ]
                else:                    
                    action Jump ("interact_with_cave_crack")
        else:
            if not inventory_open:
                use arrow("(to Ingress)","cave_broadside",(0.5, .05),-90)    
        if not cave_flags['pick_taken']:
            imagebutton auto 'bg_cave_ship_crack_pick_%s':
                focus_mask True
                tooltip "Pick"
                if active_item:
                    action [
                        SetVariable('active_item', None),
                        Notify("Looks like that item won't work here...")
                    ]
                else:                    
                    action Jump ("interact_with_cave_pick")

        if not inventory_open:
            use arrow("(to Descent)","cave_ship_descent",(0.4, .9),108)
            use arrow("(to Terminus)","cave_ship_end",(0.9, .7),20)
            use inventory_button
        if active_item:
            use item_active
        use map_tooltip_display

label cave_ship_cabin_1:
    scene bg_cave_ship_cabin_1

    if curr_map_screen != 'cave_ship_cabin_1':
        show screen map_name_display("The Wreck - Outer Cabin")
    $ curr_map_screen = 'cave_ship_cabin_1'

    call screen bg_cave_ship_cabin_1_nav

    screen bg_cave_ship_cabin_1_nav():
        imagebutton auto 'bg_cave_ship_cabin_1_desk_%s':
            focus_mask True
            tooltip "Overturned Desk"
            if active_item:
                action [
                    SetVariable('active_item', None),
                    Notify("Looks like that item won't work here...")
                ]
            else:                    
                action Jump ("interact_with_cave_desk")

        if not inventory_open:
            use arrow("(to Middecks)","cave_ship_deck_3",(0.55, .95),70)
            use arrow("(to Inner Cabin)","cave_ship_cabin_2",(0.45, .35),-108)
            use inventory_button
        if active_item:
            use item_active
        use map_tooltip_display

label cave_ship_cabin_2:
    if cave_flags["safe_fallen"]:
        scene bg_cave_ship_cabin_2_nofloor
    else:
        scene bg_cave_ship_cabin_2

    if curr_map_screen != 'cave_ship_cabin_2':
        show screen map_name_display("The Wreck - Inner Cabin")
    $ curr_map_screen = 'cave_ship_cabin_2'

    call screen bg_cave_ship_cabin_2_nav

    screen bg_cave_ship_cabin_2_nav():
        if not cave_flags['safe_fallen']:
            imagebutton auto 'bg_cave_ship_cabin_2_safe_%s':
                focus_mask True
                tooltip "Captain's Safe"
                if active_item:
                    action [
                        SetVariable('active_item', None),
                        Notify("Looks like that item won't work here...")
                    ]
                else:                    
                    action Jump ("interact_with_cave_safe")
            
        if not inventory_open:
            use arrow("(to Outer Cabin)","cave_ship_cabin_1",(0.5, .95),90)
            use inventory_button
        if active_item:
            use item_active
        use map_tooltip_display



label cave_ship_falldown:
    if not cave_flags['cannon_pushed']:
        scene bg_cave_ship_falldown
    else:
        scene bg_cave_ship_falldown_cannon

    show screen map_name_display("The Wreck - Terminus")
    $ curr_map_screen = 'cave_ship_end'
    call screen bg_cave_ship_falldown_nav

    screen bg_cave_ship_falldown_nav():
        imagebutton auto 'bg_cave_ship_falldown_safe_%s':
            focus_mask True
            tooltip "Captain's Safe"
            if active_item:
                if active_item == 'cave_key':
                    action [
                        SetVariable('active_item', None),
                        Jump("cave_act_safe_key")
                    ]
                else:
                    action [
                        SetVariable('active_item', None),
                        Notify("Looks like that item won't work here...")
                    ]
            else:                    
                action Jump ("interact_with_cave_safe_end")

        if not inventory_open:
            use arrow("(to Descent)","cave_ship_descent",(0.3, .35),-108)
            use arrow("(to Egress)","cave_ship_crack",(0.8, .35),-55)
            use inventory_button
        if active_item:
            use item_active
        use map_tooltip_display