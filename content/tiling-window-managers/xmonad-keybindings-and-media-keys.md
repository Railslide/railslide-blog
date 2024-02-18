Title: Xmonad keybindings and media keys
Date: 2024-02-18
Tags: xmonad
Summary: How to set up keybindings and make media keys work in Xmonad
Status: draft

One of the first things I wanted to get to work once I installed Xmonad were the media keys. I use music as a way to concentrate when coding and having to go through the hassle of finding the player window, reaching for my mouse, and clicking on the control buttons is a waste of time and focus. So controlling playback from my keyboard is a must.

However Xmonad doesn't support media keys out of the box, so in order to have them working I had to define some keybindings.

## How keybindings work

First I had to import the `XMonad.Util.EZConfig` module at the top of my config.

```haskell
import XMonad.Util.EZConfig
```

The `XMonad.Util.EZConfig` includes `additionalKeys` which can be used to define keybindings. The syntax is the following

```haskell
myKeyBindings =
  [ ((mod1Mask, xK_f), spawn "firefox") -- mod+f launches Firefox
  , ((noModMask, xK_Print), spawn "scrot -s") -- PrtScr takes a screenshot
  ]

myConfig = def
  {
    terminal    = myTerminal,
    modMask     = myModMask,
    startupHook = myStartupHook
  } `additionalKeys` myKeyBindings
```

where `noModMask` is used for when you don't need a modifier, like in the example above where <kdb>PrtScr</kbd> is all you need to press in order to take a screenshot.

While that certainly works, it's not exactly the most straightforward syntax. Thankfully the very same module also includes `additionalKeysP`, which helps solving exactly that. According to the docs, it uses _"Emacs-style keybinding specifications"_, which I would have rather called human-friendly specifications but I guess that wasn't equally catchy.

So with the new syntax, the config becomes

```
myKeyBindings =
  [ ("M-f", spawn "firefox")
  , ("<Print>", spawn "scrot -s")
  ]

myConfig = def
  {
    terminal    = myTerminal,
    modMask     = myModMask,
    startupHook = myStartupHook
  } `additionalKeysP` myKeyBindings
```

Much better! A full list of the supported special keys can be found in [Xmonad docs](https://hackage.haskell.org/package/xmonad-contrib-0.18.0/docs/XMonad-Util-EZConfig.html#g:3).

## Setting media keys up

Next was to set up media keys. In order for them to work, besides a keybinding, I also needed something to control the currently active player. For that I installed `playerctl` which worked great both from my keyboard and from my headphones.

```haskell
myKeyBindings =
  [ ("M-f", spawn "firefox")
  , ("<Print>", spawn "scrot -s")
  -- Media keys
  , ("<XF86AudioPlay>", spawn "playerctl play-pause")
  , ("<XF86AudioNext>", spawn "playerctl next")
  , ("<XF86AudioPrev>", spawn "playerctl previous")
  ]
```

Note that if you are using `additionalKeys`, you will have to import `Graphics.X11.ExtraTypes.XF86` in order to use `xF86XK_AudioPlay` and co.

## Resources

- [Xmonad configuration tutorial](https://xmonad.org/TUTORIAL.html)
- [XMonad.Util.EZConfig docs](https://hackage.haskell.org/package/xmonad-contrib-0.18.0/docs/XMonad-Util-EZConfig.html)
