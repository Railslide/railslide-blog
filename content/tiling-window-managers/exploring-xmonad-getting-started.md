Title: Exploring xmonad: Getting started
Date: 2024-02-05
Tags: xmonad
Summary: The first of a series of articles about exploring xmonad and trying to wrap my head around Haskell.

This is the first article of a series about my experience with setting up xmonad. The idea is to keep track of my journey and to write some handy guides for either someone who might be curious about xmonad as well and/or my future self.


## Installing all the things

What a better place for starting than installing xmonad?

Ideally you want to install the following

- `xmonad` (duh!)
- `xmonad-contrib`, xmonad extensions (you can't do much without it!)
- `dmenu`, launcher/menu for applications
- `xterm`, xmonad default terminal emulator. You can switch to your favourite emulator later, but it's good to have xterm available as a fallback.

For Arch, I installed all the above via Yay/Pacman and then added a [Pacman hook](https://wiki.archlinux.org/title/Xmonad#Problems_with_finding_shared_libraries_after_update) to avoid future headaches when updating.

## Basic configuration

Next I created a basic config file. You don't necessarily need one, but I wanted to customize a couple of things already from the start.

```haskell
import XMonad

myModMask  = mod4Mask -- Use Super as the mod key
myTerminal = "alacritty"

-- Actions to perform whenever xmonad starts or is restarted
myStartupHook = do
  spawn "setxkbmap -layout us"

myConfig = def
  {
    terminal    = myTerminal,
    modMask     = myModMask,
    startupHook = myStartupHook
  }

-- Run xmonad with the settings specified above
main :: IO ()
main = xmonad $ myConfig
```

and saved it into `~/.xmonad/xmonad.hs`.

Note that the above configuration will not work with xmonad<0.17.

It's also worth nothing that the location of the config might vary. According to xmonad doc it should go into `~/.config/xmonad/xmonad.hs`, which however didn't work for me (thankfully I had xterm installed, otherwise I wouldn't have been able to do anything once I logged into xmonad!). Arch wiki tells you instead to place it into `~/.xmonad/xmonad.hs`, which in my case resulted in the config being picked up correctly.

## Getting around in xmonad

Next is to log into xmonad and test if the config is loaded correctly.

If `Super+Shift+Enter` launches Alacritty, you're good to go. If not, try moving the config to a different location (see above).

Here are a list of useful keybindings to start with

| Keybinding                                        | Action                      |
|---------------------------------------------------|-----------------------------|
| <kbd>mod</kbd> <kbd>shift</kbd> <kbd>return</kbd> | Launch terminal             |
| <kbd>mod</kbd> <kbd>p</kbd>                       | Launch dmenu                |
| <kbd>mod</kbd> <kbd>shift</kbd> <kbd>c</kbd>      | Close the focused window    |
| <kbd>mod</kbd> <kbd>shift</kbd> <kbd>q</kbd>      | Quit xmonad                 |
| <kbd>mod</kbd> <kbd>q</kbd>                       | Restart xmonad              |

## References

- [Xmonad docs](https://xmonad.org/documentation.html)
- [Xmonad - Arch linux wiki](https://wiki.archlinux.org/title/xmonad)
