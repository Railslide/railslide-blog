Title: Setting up Sway: inputs & outputs
Date: 2025-08-19
Tags: sway, wayland, desktop-enviroments, setting-up-sway
Summary: Part 2 of the series of articles about setting up Sway. Keyboard, mouse, and multiple screens.


_This article is part 2 of [a series about setting up Sway](/tag/setting-up-sway.html)_

## Inputs (aka keyboard, mouse, etc)

One of the first things I used to do after installing a desktop environment was to adjust keyboard and mouse behavior. Thankfully Sway lets you define those in the config, so now I only need to make sure my config is in place and everything just works out of the box.

So how do you go for customizing them? Once again, the friendly config provides an example as well as some helpful text

```
### Input configuration
#
# Example configuration:
#
#   input "2:14:SynPS/2_Synaptics_TouchPad" {
#       dwt enabled
#       tap enabled
#       natural_scroll enabled
#       middle_emulation enabled
#   }
#
# You can get the names of your inputs by running: swaymsg -t get_inputs
# Read `man 5 sway-input` for more information about this section.
```

So if you want to edit the config for a specific input device, you'd just run `swaymsg -t get_inputs`, find it in the list, and adjust its behavior accordingly.

This is great, but what if I wanted to have certain behaviors for ALL my keyboards or all my mice? Well, you simply have to define the behaviors on the input type, rather than on the input identifier. For example

```
input type:keyboard {
  xkb_layout "us,it,se"
# Map alt+shift to keyboard layout switcher and caps-lock to ctrl
  xkb_options "grp:alt_shift_toggle, ctrl:nocaps"
}
```

The snippet above would make the `us`, `it`, and `se` layouts available, set <kbd>alt</kbd> <kbd>shift</kbd> as layout switcher, and remap <kbd>caps-lock</kbd> to <kbd>ctrl</kbd>, for ALL keyboards.

For a list of layouts and options for `xkb`, [the man page for it](https://man.archlinux.org/man/xkeyboard-config-2.7.en) is a great resource.


## Outputs (aka screens)

Outputs in Sway work similarly to inputs. You can get a list of the available ones with `swaymsg -t get_outputs` and define their setup, as suggested in the config itself

```
# Example configuration:
#
#   output HDMI-A-1 resolution 1920x1080 position 1920,0
#
# You can get the names of your outputs by running: swaymsg -t get_outputs
```

And this would probably work great if you have a very static setup, like a single screen that you only need to set up once. However, if you happen to have a laptop and one or more external screens or setups (e.g. home and office), you'll likely want to use [Kanshi](https://gitlab.freedesktop.org/emersion/kanshi) instead.

Kanshi allows you to define output profiles that are automatically enabled and disabled when screens are plugged in or out. If you are familiar with Autorandr, Kanshi is the Wayland equivalent of it.

To setup Kanshi, you first need to install the `kanshi` package with your favourite package manager. Next, create a config file at `~/.config/kanshi/config` (I personally don't git commit this file to my dotfiles, since it's very machine specific) and fill it with your desired setup. For example

```
profile {
	output LVDS-1 position 0,0 scale 1.5
	output "Some Company ASDF 4242" mode 1600x900 position 1920,0
}

profile {
	output LVDS-1 enable scale 2
}
```

The snippet above defines two different profiles, one for the laptop built-in monitor only and the other for when a specific external screen is plugged in. Kanshi will then take care of enabling the correct profile whenever all the listed devices are connected.

One thing worth paying attention to is the position parameter, especially if you want multiple outputs to be displayed next to each other. The way you achieve that, is to set the position of the screen you want on the left to `0,0` and the one you want to the right to `<left_screen_width>,0`. You can get the width of the screen by running `swaymsg -t get_outputs`.

Last but not least, let's tell Sway to use Kanshi by adding the following to your config
```
exec_always "pkill kanshi; kanshi &"
```

The `exec_always` parts guarantees that the command is run even when the Sway config is reloaded (differently from `exec`, which will only run at session start). And the rest of the command is just to make sure to stop any running instances of Kanshi, before starting a new one.

## Conclusion

That's it! You should now be able to config your inputs an outputs as per your liking!

## References

- [Man page for xkeyboard-config](https://man.archlinux.org/man/xkeyboard-config-2.7.en)
- [Kanshi source code and docs](https://gitlab.freedesktop.org/emersion/kanshi)
- `man -k sway`, for a list of all the available Sway man pages
- [Sway - Arch linux wiki](https://wiki.archlinux.org/title/Sway)
