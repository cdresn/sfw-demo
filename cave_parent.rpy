label cave_parent:
    $ cave_flags = dict(
    campfire_lit = False,
    ascent = False,
    false_ascent = False,
    skeleton_hat = False,
    journal_read = False,
    pile_clear = False,
    shovel_broken = False,
    fell_down = 0,
    attempted_move = False,
    lantern_taken = False,
    lantern_smashed = False,
    crack_stick_outside = False,
    climbed_flag = False,
    shovel_taken = False,
    smelled_booze = False,
    tried_booze = False,
    false_ascent_attempted = False,
    hot_tar = False,
    sticky_hook = False,
    chain_taken = False,
    tar_taken = False,
    safe_fallen = False,
    fell_with_safe = False,
    door_open = False,
    cannon_inspected = False,
    cannon_pushed = False,
    cannon_loaded = False,
    cannon_fired = False,
    ascent_climbed = False,
    crack_inspected = False,
    pick_taken = False,
    crack_pick = False,
    crack_stick = False,
    pile_dug = False
        )

    $ tooltips = dict(
    cave_book = "[Weathered Journal]",
    cave_cannonball = "[Cannonball]",
    cave_chain = "[Length of Chain]",
    cave_flintlock = "[Defective Flintlock]",
    cave_grappling_hook = "[Improvised Grappling Hook]",
    cave_hook = "[Broken Shovel Blade]",
    cave_key = "[Skeleton's Key]",
    cave_lantern = "[Rusty Lantern]",
    cave_pick = "[Sturdy Pick]",
    cave_safekey = "[Ornate Key]",
    cave_shaft = "[Broken Shovel Haft]",
    cave_shovel = "[Rickety Shovel]",
    cave_tar = "[Congealed Tar]"
    )
    
    $ inv = []
    $ inventory_open = False
    $ active_item = None
    $ prev_map_screen = None
    $ curr_map_screen = None

    scene cave_cs_1 with fade
    pause
    scene cave_cs_2 with dissolve
    pause
    scene cave_cs_3 with fade
    show screen map_name_display(map_name="The Deep Cove", text_size=200)
    pause

    $ renpy.notify('Dig up your destiny!')

    jump cave_center