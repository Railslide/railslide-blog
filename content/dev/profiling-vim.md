Title: Profiling Vim
Date: 2025-03-09
Tags: vim, neovim
Summary: How to figure out what's slowing your Neovim down

Is your Neovim slow and you want to understand why? Here's what you can do.

## Profiling start time

If the problem occurs during the startup, you can use the `--startuptime` to get an insight of what's going on

```
nvim --startuptime [OUTPUT_FILE]
```

## Profiling after startup

If your problem doesn't occur when starting up Neovim (e.g. in my case it would occur when opening the first Python file), the `:profile` is likely a better option. You can use it from inside Vim like so:

```
:profile start [OUTPUT_FILE]
:profile func *
:profile file *
[Do slow actions here...]
:profile stop
```

Note that the `*` pattern will make Vim profile all the functions and scripts indiscriminately. So if you already know that you want to look into specific ones, you can use a more specific pattern to reduce the noise. See `:h profile` for more info on how to do that.
