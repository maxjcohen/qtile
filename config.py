# Copyright (c) 2010 Aldo Cortesi
# Copyright (c) 2010, 2014 dequis
# Copyright (c) 2012 Randall Ma
# Copyright (c) 2012-2014 Tycho Andersen
# Copyright (c) 2012 Craig Barnes
# Copyright (c) 2013 horsik
# Copyright (c) 2013 Tao Sauvage
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

import os
from typing import List  # noqa: F401

from libqtile import bar, layout, widget
from libqtile.config import Click, Drag, Group, Key, Match, Screen, ScratchPad, DropDown
from libqtile.lazy import lazy

_WM = {
    "COLOR_BG_BAR": "#2e3440",
    "COLOR_FOCUS": "#81a1c1",
    "COLOR_URGENT": "#bf616a",
}

for key in _WM:
    try:
        _WM[key] = os.environ[f"WM_{key}"]
    except KeyError:
        pass


_widget_defaults = {
    "padding": 10,
    "background": None,
    "fontsize": 15,
    "font": "Open Sans Bold",
}

mod = "mod1"  # See "xmodmap" for a list a modifiers available
terminal = "st"

keys = [
    # Switch between windows
    Key([mod], "h", lazy.layout.left(), desc="Move focus to left"),
    Key([mod], "l", lazy.layout.right(), desc="Move focus to right"),
    Key([mod], "j", lazy.layout.down(), desc="Move focus down"),
    Key([mod], "k", lazy.layout.up(), desc="Move focus up"),
    # Move windows between left/right columns or move up/down in current stack.
    # Moving out of range in Columns layout will create new column.
    Key(
        [mod, "shift"], "h", lazy.layout.shuffle_left(), desc="Move window to the left"
    ),
    Key(
        [mod, "shift"],
        "l",
        lazy.layout.shuffle_right(),
        desc="Move window to the right",
    ),
    Key([mod, "shift"], "j", lazy.layout.shuffle_down(), desc="Move window down"),
    Key([mod, "shift"], "k", lazy.layout.shuffle_up(), desc="Move window up"),
    # Grow windows. If current window is on the edge of screen and direction
    # will be to screen edge - window would shrink.
    Key([mod, "control"], "h", lazy.layout.grow_left(), desc="Grow window to the left"),
    Key(
        [mod, "control"], "l", lazy.layout.grow_right(), desc="Grow window to the right"
    ),
    Key([mod, "control"], "j", lazy.layout.grow_down(), desc="Grow window down"),
    Key([mod, "control"], "k", lazy.layout.grow_up(), desc="Grow window up"),
    Key([mod], "n", lazy.layout.normalize(), desc="Reset all window sizes"),
    # Toggle between split and unsplit sides of stack.
    # Split = all windows displayed
    # Unsplit = 1 window displayed, like Max layout, but still with
    # multiple stack panes
    Key(
        [mod, "shift"],
        "Return",
        lazy.layout.toggle_split(),
        desc="Toggle between split and unsplit sides of stack",
    ),
    # Toggle between different layouts as defined below
    Key([mod], "space", lazy.next_layout(), desc="Toggle between layouts"),
    Key([mod], "w", lazy.window.kill(), desc="Kill focused window"),
    Key([mod, "control"], "r", lazy.restart(), desc="Restart Qtile"),
    Key([mod, "control"], "q", lazy.shutdown(), desc="Shutdown Qtile"),
    # Spawn commands
    Key(
        [mod, "control"],
        "p",
        lazy.spawncmd(),
        desc="Spawn a command using a prompt widget",
    ),
    Key([mod], "Return", lazy.spawn(terminal), desc="Launch terminal"),
    Key([mod], "r", lazy.spawn("st -e ranger")),
    Key([mod], "f", lazy.spawn("st -e sh -c '$(fzfmenu)'")),
    # Toogle between groups
    Key([mod], "Tab", lazy.screen.toggle_group()),
    Key(["shift", "control"], "k", lazy.screen.next_group()),
    Key(["shift", "control"], "j", lazy.screen.prev_group()),
]


# ============================
# Groups
# ============================
groups_def = [
    {
        "name": "term",
        "label": "",
    },
    {
        "name": "firefox",
        "label": "",
        "matches": [Match(wm_class=["firefox", "vimb", "Tor Browser"])],
    },
    {
        "name": "files",
        "label": "",
        "matches": [Match(wm_class=["ranger"])],
    },
    {
        "name": "code",
        "label": "",
    },
    {
        "name": "video",
        "label": "",
    },
    {
        "name": "slack",
        "label": "",
        "matches": [Match(wm_class=["Slack"])],
    },
]
groups = [Group(**group_def) for group_def in groups_def]

for group_idx, group in enumerate(groups):
    keys.extend(
        [
            # mod1 + letter of group = switch to group
            Key(
                [mod],
                str(group_idx + 1),
                lazy.group[group.name].toscreen(),
                desc="Switch to group {}".format(group.name),
            ),
            # mod1 + shift + letter of group = switch to & move focused window to group
            Key(
                [mod, "shift"],
                str(group_idx + 1),
                lazy.window.togroup(group.name, switch_group=True),
                desc="Switch to & move focused window to group {}".format(group.name),
            ),
        ]
    )

launch_app_cmd = "st -e sh -c 'nohup $(fzfmenu)'"
groups.append(
    ScratchPad(
        "scratchpad",
        [
            DropDown(
                "launcher",
                launch_app_cmd,
                y=0.3,
                height=0.4,
                x=0.2,
                width=0.60,
            ),
        ],
    )
)

# define keys to toggle the dropdown terminals
keys.extend(
    [
        Key([mod], "p", lazy.group["scratchpad"].dropdown_toggle("launcher")),
    ]
)

# ============================
# Layouts
# ============================
layouts = [
    layout.Max(),
    layout.TileSingle(
        margin=10,
        border_focus=_WM["COLOR_FOCUS"],
        border_normal=_WM["COLOR_BG_BAR"],
        border_width=3,
    ),
    # layout.Columns(border_focus_stack='#d75f5f'),
    # Try more layouts by unleashing below layouts.
    # layout.Stack(num_stacks=2),
    # layout.Bsp(),
    # layout.Matrix(),
    # layout.MonadTall(),
    # layout.MonadWide(),
    # layout.RatioTile(),
    # layout.Tile(),
    # layout.TreeTab(),
    # layout.VerticalTile(),
    # layout.Zoomy(),
]
layouts_icons = {
    "tilesingle": "",
    "max": "",
    "float": "",
}

# ============================
# Widgets
# ============================
widget_defaults = dict(
    font="sans",
    fontsize=12,
    padding=3,
)
extension_defaults = widget_defaults.copy()

screens = [
    Screen(
        wallpaper="~/.local/share/backgrounds/the-midnight-gospel-wallpaper.jpeg",
        wallpaper_mode="fill",
        top=bar.Bar(
            [
                widget.GroupBox(
                    fontsize=15,
                    font="Font Awesome 5 Free Solid",
                    highlight_method="line",
                    urgent_alert_method="line",
                    highlight_color=_WM["COLOR_BG_BAR"],
                    this_current_screen_border=_WM["COLOR_FOCUS"],
                    block_highlight_text_color=_WM["COLOR_FOCUS"],
                    urgen_text=_WM["COLOR_URGENT"],
                    urgen_border=_WM["COLOR_URGENT"],
                ),
                widget.CurrentLayout(
                    layouts_icons=layouts_icons,
                    foreground=_WM["COLOR_FOCUS"],
                    **_widget_defaults
                ),
                widget.Prompt(**_widget_defaults),
                widget.WindowName(**_widget_defaults),
                widget.Spacer(),
                widget.Systray(),
                widget.Net(
                    format="{down}{up}",
                    update_interval=3.0,
                    foreground="#b48ead",
                    **_widget_defaults
                ),
                widget.Backlight(
                    backlight_name="intel_backlight",
                    format=" {percent:2.0%}",
                    foreground="#d08770",
                    **_widget_defaults
                ),
                widget.CPU(
                    format=" {load_percent:.0f}%",
                    update_interval=3.0,
                    foreground="#a3be8c",
                    **_widget_defaults
                ),
                widget.Memory(
                    format=" {MemPercent:.0f}%",
                    update_interval=3.0,
                    foreground="#b48ead",
                    **_widget_defaults
                ),
                widget.Wifi(fmt=" {}", foreground="#d08770", **_widget_defaults),
                widget.BatteryHybrid(foreground="#88c0d0", **_widget_defaults),
                widget.VolumePulse(foreground="#d08770", **_widget_defaults),
                widget.KeyboardLayout(
                    fmt=" {}", foreground="#5e81ac", **_widget_defaults
                ),
                widget.Clock(
                    format="%a, %d %b",
                    fmt=" {}",
                    foreground="#a3be8c",
                    **_widget_defaults
                ),
                widget.Clock(
                    format="%H:%M", fmt=" {}", foreground="#88c0d0", **_widget_defaults
                ),
            ],
            28,
            background=_WM["COLOR_BG_BAR"],
        ),
    ),
]

# Drag floating layouts.
mouse = [
    Drag(
        [mod],
        "Button1",
        lazy.window.set_position_floating(),
        start=lazy.window.get_position(),
    ),
    Drag(
        [mod], "Button3", lazy.window.set_size_floating(), start=lazy.window.get_size()
    ),
    Click([mod], "Button2", lazy.window.bring_to_front()),
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: List
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False
floating_layout = layout.Floating(
    float_rules=[
        # Run the utility of `xprop` to see the wm class and name of an X client.
        *layout.Floating.default_float_rules,
        Match(wm_class="confirmreset"),  # gitk
        Match(wm_class="makebranch"),  # gitk
        Match(wm_class="maketag"),  # gitk
        Match(wm_class="ssh-askpass"),  # ssh-askpass
        Match(title="branchdialog"),  # gitk
        Match(title="pinentry"),  # GPG key password entry
    ],
    border_focus=_WM["COLOR_FOCUS"],
    border_normal=_WM["COLOR_BG_BAR"],
    border_width=3,
)
auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True

# If things like steam games want to auto-minimize themselves when losing
# focus, should we respect this or not?
auto_minimize = True

# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = "LG3D"
