Title: Setting up Sway: media playing & Pipewire
Date: 2025-08-31
Tags: sway, wayland, desktop-enviroments, setting-up-sway, pipewire
Summary: Part 3 of the series of article about setting up Sway. Media playing and Pipewire.

_This article is part 3 of [a series about setting up Sway](/tag/setting-up-sway.html)_


> **Note!** </br>
> In this article I am going to cover how to get media playing to work specifically with Pipewire. If you use something else (e.g. pulseaudio), the instructions below will likely not apply.


## Media keys

In order to set up media keys to work under Pipewire, you first need to install two dependencies:

- `wireplumber` to control volume
- `playerctl` to control playback

You might have noticed that the default Sway configuration already comes with a handy set of key bindings for volume control:

```
# Special keys to adjust volume via PulseAudio
bindsym --locked XF86AudioMute exec pactl set-sink-mute \@DEFAULT_SINK@ toggle
bindsym --locked XF86AudioLowerVolume exec pactl set-sink-volume \@DEFAULT_SINK@ -5%
bindsym --locked XF86AudioRaiseVolume exec pactl set-sink-volume \@DEFAULT_SINK@ +5%
bindsym --locked XF86AudioMicMute exec pactl set-source-mute \@DEFAULT_SOURCE@ toggle
```

However, as they comment says, they are meant for working with PulseAudio. So, in order to make it work with Pipewire, you need to change them to:

```
bindsym --locked XF86AudioMute exec wpctl set-mute @DEFAULT_SINK@ toggle
bindsym --locked XF86AudioLowerVolume exec wpctl set-volume @DEFAULT_SINK@ 5%-
bindsym --locked XF86AudioRaiseVolume exec wpctl set-volume --limit 1.0 @DEFAULT_SINK@ 5%+
byndsym --locked XF86AudioMicMute exec wpctl set-mute @DEFAULT_AUDIO_SOURCE@ toggle
```

As you can see, they look fairly similar, with the only exception of the `--limit 1.0` flag. The reason for that is to prevent Wireplumber from continuing to increase the volume after reaching 100%.

Last but not least, let's add the keybindings for playback control to the config file

```
bindsym --locked XF86AudioPlay exec playerctl play-pause
bindsym --locked XF86AudioNext exec playerctl next
bindsym --locked XF86AudioPrev exec playerctl previous
```

And now your media key are properly set up for working with Pipewire.

## Screen sharing

In order for screen sharing to work, you need a xdg-desktop-portal. The one for wlroots, which Sway relies on, is called `xdg-desktop-portal-wlr`. Once installed, screen sharing should just work - with a couple of catches:

- Only screen sharing is currently possible at the time of writing (version 0.7.1). Single window sharing should arrive with the next release, but the ETA for it is currently unknown. If you are in a hurry and feel adventurous, you can install from source and follow [these instructions](https://github.com/emersion/xdg-desktop-portal-wlr/issues/107#issuecomment-3217127025) (note that I haven't tried them myself, so I have no clue if they works).

- `xdg-desktop-portal-wlr` will try to pick the first screen selector from a list of hardcoded choosers (slurp, wmenu, wofi, rofi, bemenu). So make sure to have at least one of those installed.


## Preventing idle from triggering when playing media

The last bit of settings is to prevent you computer to go in idle mode when media is being played.

Install `wayland-pipewire-idle-inhibit` and add the following to Sway config

```
exec wayland-pipewire-idle-inhibit
```

And voilà, no more idle and lock screen triggering while watching a video or taking part in a video call!

The behavior of the inhibitor can be customized by creating a toml file at `~/.config/wayland-pipewire-idle-inhibit/config.toml`. For example, if you don't care about idle triggering while Spotify is playing, you can simply blacklist it in the config file:

```
[[node_blacklist]]
name = "spotify"
```

Check the [docs](https://github.com/rafaelrc7/wayland-pipewire-idle-inhibit/tree/master?tab=readme-ov-file#config) for a list of all supported configurations.


## References

- [Wireplumber docs](https://pipewire.pages.freedesktop.org/wireplumber/)
- [xdg-desktop-portal-wlr on GitHub](https://github.com/emersion/xdg-desktop-portal-wlr)
- [wayland-pipewire-idle-inhibit on GitHub](https://github.com/rafaelrc7/wayland-pipewire-idle-inhibit)
