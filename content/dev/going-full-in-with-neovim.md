Title: Going full in with Neovim
Date: 2023-01-16
Tags: editor, vim, neovim, tools
Slug: going-full-in-with-neovim
Summary: Goodbye `.vimrc`, hello `lua.init`!

A while ago I decided to fully embrace Neovim and port all my config from `.vimrc` over to Lua.

## The why(s)
First thing first, why Neovim? Because you basically get the full Vim experience, but with sane defaults and lsp support. Plus the project is community driven and has faster development cycles (multiple maintainers, less legacy code, etc.). Sure there are some differences, but so far I have yet to find myself in the situation where I fall back to Vim because I cannot do something in Neovim.

Ok, and what about Lua? When I started my [Vim adventure]({filename}/dev/learning-vim-in-2022.md) I felt like I didn't know enough about Vim and Neovim to have a strong preference for one over the other, so I just placed all my config in `.vimrc` as that was compatible with both. But then time passed and two things happened: first, I realized I have never went back once to Vim after trying Neovim; second, Vim announced that from version 9.0 it will introduce a new scripting language (Vim 9 Script), which will not be completely backward-compatible with the old VimScript. For me that meant that, no matter which editor I chose, I would have to learn a new language. And if I have to put the effort, I'd rather do it for something multipurpose like Lua, than for a language that only applies to my editor.

## The structure

After a bit of back and forth, this is what the directory structure of my config currently looks like:

```
nvim
├── after
│   └── plugin
│       ├── ale.lua
│       ├── lightline.vim.lua
│       ├── onedark.lua
│       └── telescope.lua
├── init.lua
├── lua
│   └── railslide
│       ├── mappings.lua
│       ├── options.lua
│       └── plugin-manager.lua
└── plugin
    └── packer_compiled.lua
```

The `lua/railside` folder is where I keep my general configuration. The `lua` folder is included in Neovim `runtimepath` and it's where Neovim looks for Lua plugins by default. Inside that I created a directory with my own username in order to avoid namespace conflicts (the name per se doesn't actually matter, as long as it's something unlikely to be used by something else you're good to go).

All the files in the `railslide` folder are then imported in my `init.lua`

```lua
require("railslide.plugin-manager") -- This needs to be at the top
require("railslide.options")
require("railslide.mappings")
```

## Plugins
A side effect of my config migration is that I switched to a new plugin manager as I decided that I wanted to go for something written in Lua. Packer seemed to be the most popular choice, so I went for that and so far it has been good. There are a lot of good reasons to use Packer, but one of the things I really appreciate is the [bootstrapping snippet](https://github.com/wbthomason/packer.nvim#bootstrapping) which allows you to automatically install and set up Packer on a new machine.

My Packer settings and the list of installed plugins are stored in `lua/railslide/plugin-manager.lua`, while the files containing the configurations for the actual plugins are in the `after/plugin` folder, following a `<plugin_name>.lua` naming pattern. The cool thing with the `after` folder is that it gets automatically sourced (i.e. no need for me to explicitly require them in my `init.lua`) and, as the name suggests, that only happens after all the rest of my configurations have been loaded, which means no risk for plugins not picking up some other setting (e.g. the leader definition). Plus, having a file for each plugin makes it very easy for me to know where the settings for it are and to get rid of them if I were to decide to uninstall the plugin.

For Lua plugins I also decided to require them through a protected call, i.e.
```lua
status_ok, some_plugin = pcall(require, 'some_plugin')
if not status_ok then
  print('Could not find some_plugin plugin')
  return
end

some_plugin.setup(
  -- ...
)
```
That way if a plugin isn't correctly loaded, Neovim will display a message below the status line rather than printing out stack traces at start time. This has come in handy for me whenever I forgot to run `packerSync` after git pulling an updated copy of my dotfiles, as well as for when I want to temporarily disable a plugin without touching its configuration.

The `plugin/packed_compiled.lua` is where Packer stores the compiled code it uses for reducing startup time. I added it to `.gitignore` as there was no real benefit in committing it and I didn't want to [pollute my git history](https://github.com/wbthomason/packer.nvim/issues/462#issuecomment-876676720). Plus it will be generated anew anyway whenever I set up Neovim on a new machine.

## Use the source, Luke
This is an overview of how my configuration looks and the reasoning that went behind it. So far it has served me well, but of course I'm always happy to find ways to further improve my setup. So if you're curious about the nitty-gritty and/or how my config might evolve in the future, [my dotfiles repo GitHub](https://github.com/Railslide/dotfiles/tree/master/neovim/.config/nvim) is the place to go.
