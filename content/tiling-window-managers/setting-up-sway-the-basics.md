Title: Setting up Sway: the basics
Date: 2025-08-08
Tags: sway, wayland, desktop-enviroments
Summary: The first of a series of article about setting up Sway. How to install Sway, creating a config file, and setting the lock screen up.
Status: draft


A while ago I decided to give window managers a try. After a bit of experimentation I landed on Sway and never go back. So after roughly 1.5 years of using as my daily driver, I decided that it was finally time to dedicate a series of article to how to set it up.

## Why Sway

- It is super customizable while still being human-friendly
- It has great docs, an easily understandable config, and a sane defaults set
- It uses Wayland instead of Xorg, which is deprecated and no longer actively maintained


So if you are after a minimal tiling window managers that can be completely adapted to you needs, without having to go through to a super steep learning curve (hello xmonad), you should definitely give Sway a try.

## Installing Sway

The first step to get started with Sway, is unsurprisingly to install it.

So pull up your favorite package manager and install the following:

- `sway`
- `foot` (default terminal emulator)
- `wmenu` (default application menu)
- `swaybg` (default wallpaper tool)

You can of course change the terminal emulator and application menu later on, but for now let's stick to the default and get Sway up and running.

After that, if you are using a display a display manager, it's a just a matter of logging out from your current desktop environment and logging in into Sway. If not, running `sway` in your terminal will do the trick.

Here's a list of useful keybindings to start with. The full list can be found in the config file (see below).

| Keybinding                                        | Action                      |
|---------------------------------------------------|-----------------------------|
| <kbd>mod</kbd> <kbd>enter</kbd>                   | Launch terminal             |
| <kbd>mod</kbd> <kbd>d</kbd>                       | Launch wmenu                |
| <kbd>mod</kbd> <kbd>shift</kbd> <kbd>q</kbd>      | Close the focused window    |
| <kbd>mod</kbd> <kbd>shift</kbd> <kbd>e</kbd>      | Quit Sway                   |
| <kbd>mod</kbd> <kbd>shift</kbd> <kbd>c</kbd>      | Reload config               |

## Getting yourself a config file

The first thing you need in order to configure and customize Sway is a config file. The easiest way to get one is to copy the example configuration file located at `/etc/sway/config` to `~/.config/sway/config`.

The file in itself is fairly easy to read and includes plenty of examples. For any other question not covered in the comments or in these articles, `man 5 sway` is your friend.

## Idle and lock screen

In order to configure idle and lock screen, you first need to install the packages taking care of them, i.e. `swaylock` and `swayidle`.

Then uncomment the dedicated section in the config file and adjust it to your liking

```
# exec swayidle -w \
#          timeout 300 'swaylock -f -c 000000' \
#          timeout 600 'swaymsg "output * power off"' resume 'swaymsg "output * power on"' \
#          before-sleep 'swaylock -f -c 000000'
#
# This will lock your screen after 300 seconds of inactivity, then turn off
# your displays after another 300 seconds, and turn your screens back on when
# resumed. It will also lock your screen before your computer goes to sleep.
```

Great, now your screen will lock itself and power off after the specified time of inactivity. Though you probably also want to be able to lock it also when stepping away from keyboard. So let's add a key binding for it.

Add to your config

```
bindsym $mod+Escape exec killall -SIGUSR1 swayidle
```

That might look like a bit of black magic, so let's break it down. What that line basically does is to set a key binding for `$mod+Escape` (mod by default is the logo key) to execute a command.

Ok, now for the `killall -SIGUSR1 swayidle` part. The man page for `killall` tells us that

```
killall sends a signal to all processes running any of the specified commands. If no signal name is specified, SIGTERM is sent.
```

In other words, if no signal is specified, then `killall` will terminate the process, otherwise it will just send the provided signal. Then in the man page of `swayidle`, we can see that when receiving `SIGUSR1` `swayidle` will immediately enter idle state (i.e. it will skip it the timeout).

So basically what that line does is to bind a key combination to sending a signal to `swaydle`, so that it immediately enters idle state (aka locking the screen).

Note though, that the command as is will only skip the first timeout (i.e. the one for the screen locking). If you want your command to lock AND power off the screen, you'll have to send the signal a second time (basically one signal for every timeout you want to skip), i.e.

```
bindsym $mod+escape exec killall -s SIGUSR1 swayidle && killall -s SIGUSR1 swayidle
```

Great! Now you should have a working Sway and a working lock screen.


## References

- `man -k sway`, for a list of all the available Sway man pages
- [Sway - Arch linux wiki](https://wiki.archlinux.org/title/Sway)


