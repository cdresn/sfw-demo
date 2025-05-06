# disable mousewheel rollback
init:
    $ config.keymap['rollback'].remove('mousedown_4')
    # $ config.keymap['rollback'].append('mousedown_4')       

# disable default arrow-key UI highlighting
define config.keymap = dict(
    focus_left=None,
    focus_right=None,
    focus_up=None,
    focus_down=None,

    **dict(
        (k, v) for k, v in config.keymap.items() 
        if k not in ['focus_left', 'focus_right', 'focus_up', 'focus_down']
    )
)

# map fade-in
screen map_name_display(map_name, display_time=2.0, text_size=99):
    zorder 100
    timer display_time action Hide("map_name_display")  # Auto-hide after time elapses
    
    # The actual text with fade effects
    text map_name:
        xalign 0.05
        yalign 0.95
        size text_size
        color "#fff"
        outlines [(2, "#000", 0, 0)]
        at transform:
            alpha 0.0
            on show:
                linear 0.5 alpha 1.0  # Fade in
            on hide:
                linear 0.5 alpha 0.0  # Fade out
            on replace:
                linear 0.5 alpha 1.0  # Smooth if shown again quickly

# common arrow button for map navigation

screen arrow(tooltip_text, target_map, align_pos, rotation=0):
    imagebutton:
        if prev_map_screen == target_map:
            auto "arrow_gray_%s"
        else:
            auto "arrow_white_%s"
        focus_mask True
        tooltip tooltip_text
        action [
            SetVariable("active_item", None),
            SetVariable("prev_map_screen", curr_map_screen), 
            Jump(target_map)
        ]
        align align_pos
        at transform:
            rotate rotation

# common inventory button

screen inventory_button:
    imagebutton auto "inventory_%s":
        focus_mask True
        tooltip "(Open Inventory)"
        action [SetVariable("active_item", None), SetVariable("inventory_open", True), Show ("open_inventory")]
        align(.9, 1.0)

screen item_active:
    $ mouse_x, mouse_y = renpy.get_mouse_pos()
    timer 0.05 repeat True action [
        SetScreenVariable("mouse_x", renpy.get_mouse_pos()[0]),
        SetScreenVariable("mouse_y", renpy.get_mouse_pos()[1])
    ]
    key "mouseup_3" action SetVariable("active_item", None)
    add active_item pos (mouse_x-64, mouse_y-64) xysize (128, 128)

screen map_tooltip_display:
    $ tooltip = GetTooltip()
    if tooltip and not inventory_open:
        $ mouse_x, mouse_y = renpy.get_mouse_pos()
        timer 0.05 repeat True action [
            SetScreenVariable("mouse_x", renpy.get_mouse_pos()[0]),
            SetScreenVariable("mouse_y", renpy.get_mouse_pos()[1])
        ]
        text "{color=#FFFFFF}[tooltip]" pos (mouse_x-10, mouse_y+25):
            outlines [(2, "#000", 0, 0)]


screen open_inventory:
    modal True

    if inv:
        frame:
            xalign 0.5
            yalign 0.2
            xpadding 30
            ypadding 30
            background Solid("#00000099")
            grid 4 2:
                for item in inv:
                    imagebutton:
                        auto "{}_%s".format(item)
                        tooltip tooltips[item]
                        action [
                            Hide('open_inventory'),
                            SetVariable('active_item', item),
                            SetVariable('inventory_open', False)
                        ]

        textbutton "COMBINE ITEMS?":
            text_style 'combine_button'
            xalign 0.5
            yalign 0.9
            action [
                Hide('open_inventory'),
                Show('combine_items')
            ]

    imagebutton auto "red_x_%s":
        focus_mask True
        tooltip "Close Inventory"
        action [SetVariable("active_item", None), SetVariable("inventory_open", False), Hide ("open_inventory")]
        align(.9, 1.0)

    $ tooltip = GetTooltip()
    if tooltip:
        text "[tooltip]":
            color "#FFFFFF"
            outlines [(2, "#000", 0, 0)]
            xalign .5
            yalign .7
            size 72

screen combine_items:
    default selected_items = set()
    modal True

    frame:
        xalign 0.25
        yalign 0.2
        xpadding 30
        ypadding 30
        background Solid("#00000099")
        grid 4 2:
            for item in inv:
                imagebutton:
                    auto "{}_%s".format(item)
                    tooltip tooltips[item]
                    action [
                        If(
                            len(selected_items) < 2 or item in selected_items,
                            ToggleSetMembership(selected_items, item)
                        )
                    ]
    frame:
        if selected_items:
            xalign .85
            yalign .2
            xpadding 30
            ypadding 30
            background Solid("#00000099")
            grid 1 2:
                for item in selected_items:
                    image item

    if len(selected_items) == 2:
        textbutton "Combine!":
            text_style 'combine_button'
            xalign .85
            yalign .7
            action [
                If(
                    'cave_chain' in selected_items and 'cave_hook' in selected_items,
                    true=[
                        If(
                            cave_flags['sticky_hook'],
                            true=[
                                Function(make_grappling_hook),
                                Notify("Combined the [Broken Shovel] with the [Chain] and created a [Grappling Hook]!"),
                                SetScreenVariable('selected_items', set())
                            ],
                            false=[
                                Hide('combine_items'),
                                SetScreenVariable('selected_items', set()),
                                Function(renpy.call_in_new_context, 'cave_hook_combine_fail'),
                                Show('combine_items')
                            ]
                        )
                    ],
                    false=[
                        If(
                            'cave_hook' in selected_items and 'cave_tar' in selected_items,
                            true=[
                                If(
                                    cave_flags['hot_tar'],
                                    true=[
                                        SetScreenVariable('selected_items', set()),
                                        Function(remove_tar),
                                        Notify("Applied the [Tar] to the [Shovel Blade]! It's sticky now...")
                                    ],
                                    false=[
                                        Hide('combine_items'),
                                        SetScreenVariable('selected_items', set()),
                                        Function(renpy.call_in_new_context, 'cave_tar_combine_fail'),
                                        Show('combine_items')
                                    ]
                                )
                            ],
                            false=[
                                SetScreenVariable('selected_items', set()),
                                Notify("These two items don't seem to work together like that...")
                            ]
                        )
                    ]
                )
            ]

    textbutton "CANCEL":
        text_style 'combine_button'
        xalign 0.5
        yalign 0.7
        action [
            Hide('combine_items'),
            Show('open_inventory')
        ]

    $ tooltip = GetTooltip()
    if tooltip:
        text "[tooltip]":
            color "#FFFFFF"
            outlines [(2, "#000", 0, 0)]
            xalign .5
            yalign .8
            size 72

    imagebutton auto "red_x_%s":
        focus_mask True
        tooltip "Close Inventory"
        action [SetVariable("active_item", None), SetVariable("inventory_open", False), Hide ("combine_items")]
        align(.9, 1.0)

# misc helper functions

init python:
    def make_grappling_hook():
        inv.remove('cave_chain')
        inv.remove('cave_hook')
        inv.append('cave_grappling_hook')


init python:
    def remove_tar():
        inv.remove('cave_tar')
        tooltips['cave_hook'] = '[Sticky Shovel Blade]'
        cave_flags['sticky_hook'] = True

label cave_hook_combine_fail:
    show guy_whaler_thinking:
        zoom .5
    p "Hmm, the idea is sound, but I can't get the chain to stay put. Maybe if I had something that would get it to stick..." 
    hide guy_whaler_thinking
    $ renpy.hide_screen("say")
    window hide
    return

label cave_tar_combine_fail:
    show guy_whaler_thinking:
        zoom .5
    p "This might work, but the tar is too thick right now. Maybe if I could find a way to heat it..."
    hide guy_whaler_thinking
    $ renpy.hide_screen("say")
    window hide
    return


