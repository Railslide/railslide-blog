Title: Learning vim in 2022
Date: 2023-01-04
Tags: editor, vim, tools
Slug: learning-vim-in-2022
Summary: I decided that in 2022 I would learn Vim, here's how it went.
Status: draft

At a certain point I decided that it was time for me to learn how to use Vim. There were mainly two reasons for it. Number one, while playing the Sans Holiday Hack Challenge I have had a taste of how powerful could Vim be, as I discovered that I could open a binary file, pipe it through `xxd`, and modify its source code. Maybe this was obvious to everyone but me, but it definitely blew my mind and grew my curiosity about what else could Vim do. Second, I recently found myself orphaned of an editor of choice, so I needed to find a new one.

## Why I needed a new editor

For a long time I have used Sublime Text as my go-to editor. I set it up with a bunch of plugins, so that I could have linting and autocompletion, bought a license (at the time the business model of Sublime was an one-off lifelong license) and happily coded with it for a bunch of years. The problem with that setup was that the more languages I started coding in the more plugins I had to add, and those plugins didn't always play along with each other. On top of that Sublime has now switched to a monthly subscription license model, and - while I still use Sublime for occasional note-taking and writing this blog - I don't feel it gives me enough value for committing to a subscription.

Then came Kotlin and with it came IntelliJ. I loved IntelliJ and for me it's the best IDE out there: fantastic language support, everything can be done through keyboard, fuzzy search for anything you might need (files, actions, etc.), and so on. So why don't I stick to it? Well, mostly because its free version doesn't have multilanguage support. In other words, if you don't use the paid version, you have to use a different editor for each language (e.g. IntelliJ for Kotlin, PyCharm for Python, GoLand for Go, and good luck with JS/Typescript as there's no free version of Webstorm). That is usually not a problem at work, as my employer is happy to cover the cost of the license, but when it comes to the amount of code I do in my free time I found hard to motivate such an expense.

Last but not least I also gave VSCode a shot, but I found it way too mouse oriented from my liking and its shortcuts didn't feel super intuitive to me.

## Learning Vim

Being Vim a free keyboard-based open source cross-platform editor, it sounded like the perfect answer to all my needs. But of course all that goodness didn't come for free as it involves a steep learning curve. Thankfully there are some amazing resources out there and if you happen to be using Neovim I strongly recommend to go through the tutorial (just launch Neovim and type `:Tutor`).

My approach to Vim was to go cold turkey, which in practice meant that I switched to it (or actually to Neovim) as my day-to-day editor. I initially tried to use the Vim Plugin in VSCode, but that didn't really worked for me - maybe it was because I never felt at home with VSCode in the first place, but it mostly felt like a headache without any progress in actually learning Vim. So I went back to Vim and started with a very vanilla configuration with the idea that I would build it up on it whenever I felt the need for extra functionality. Did I get frustrated from lack of functionality from time to time? Absolutely! But shaping my `.vimrc` on my own needs and pain points is a great way to reduce the risk of bloating my setup with stuff I don't really need, as well as to make sure that I understand what every single line of my config file does.

As there's only a certain amount of frustration a person can cope with, I also made some compromises. For example I decided to ignore `hjkl` and stick to the arrows - I know this will probably offend Vim purists, but I needed a balance between learning things the Vim way and productivity. I tend to mob and pair programming a lot and I like my colleagues too much for forcing them to watch me trying to navigate around - they still had to put up with me being lost in Vim from time to time, but being unable to move around a file felt like a bit too much to endure. I don't exclude I might try to learn to use `jhkl` in the future, but for now it felt like an ok tradeoff to just skip it.

Am I fluent at Vim now? Well, while I probably wouldn't use the word _fluent_ to define myself, I definitely have gained some speed around it and I started to feel more and more at ease using it. Copy and pasting is probably the part I struggle the most with at the moment. Vim doesn't use the system clipboard as default, so copy pasting things from and to Vim is anything but straightforward. Also whenever you delete something in Vim it ends in the copy-paste registry, so I often end up overwriting whatever I was meant to copy simply because I removed some stuff before pasting. On the bright side there are some motions I really enjoy and see a lot of value in. For example, the ability to delete a whole line by simply typing `dd` is a bliss and I often find myself longing for it when using other text-editing programs.

## Wrapping up

So, was it worthy learning Vim in 2022? To me yes. Sure, it might have been frustrating at times and there were definitely occasions where editing some files took me what it felt like an eternity, but all in all it has been growing on me and nowadays I rarely feel the need to resort to other editors. So if you are willing to put the time, I'd say it's worth a shot. And if learning Vim sounds daunting, just be aware that there are plenty of resources out there and that it's really up to you how much hardcore you wanna go with it. Last but not least, Vim is highly configurable and has an extensive plugin ecosystem, so no matter what your workflow is, you're likely to be able to replicate it in Vim - if you don't believe me, just google "Vim like [editor_name_here]" and see it for yourself!



## Resources

- [Transcript of the builtin Neovim tutorial](https://github.com/neovim/neovim/blob/master/runtime/tutor/en/vim-01-beginner.tutor). I highly recommend to do the interactive version of it by typing `:Tutor` after launching Neovim, but it's good to have a reference for when you just want to quickly review something.
- [Vim as your editor YouTube Playlist by ThePrimeagean](https://www.youtube.com/playlist?list=PLm323Lc7iSW_wuxqmKx_xxNtJC_hJbQ7R)
