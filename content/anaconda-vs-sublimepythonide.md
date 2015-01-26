Title: Anaconda VS SublimePythonIDE
Date: 2015-01-27
Category: Python, Utilities
Tags: sublime text, code linting, tools
Slug: anaconda-vs-sublime-python-ide
Author: Giulia Vergottini
Summary: When I was looking for a python code linting plugin for Sublime Text 3, I stumbled upon several blog posts mentioning either SublimePythonIDE or Anaconda. The problem was, however, that a comparison between the two was nowhere to be found, so I ended up trying both.


When I was looking for a python code linting plugin for Sublime Text 3, I stumbled upon several blog posts mentioning either [SublimePythonIDE](https://github.com/JulianEberius/SublimePythonIDE) or [Anaconda](http://damnwidget.github.io/anaconda/). The problem was, however, that a comparison between the two was nowhere to be found, so I ended up trying both.

The first thing that I have to acknowledge is that they are both very good when it comes to code linting and auto completion. So, no matter which one you choose, you can't really go wrong.

When it comes to the extras SublimePythonIDE is the one that lacks most. Although this certainly comes with with the price of less flexibility, it isn't necessary a negative thing. Indeed, the strength of SublimePythonIDE is that it works out of the box: just make sure that your project settings point to correct interpreter (I delegate that to [Subvenv](http://github.com/Railslide/subvenv)) and you're ready to go. Without any further effort from your side, SublimePythonIDE will provide you with fancy linting icons on the gutter and colored linting marks. While the same things can be obtained with Anaconda as well, they still require you to read the docs and tinker with the settings.

Although they require some initial tuning, the extensive amount of customizable settings are not necessarily a negative things, since they offer you the possibility to adjust the way it looks and feel to suite your taste. On top of that Anaconda provides a bunch of handy IDE-like features, such as `Go to definition`, `Show documentation`, and `Find usage` - all reachable via shortcuts or via command palette. It also comes with [AutoPEP8](https://github.com/hhatto/autopep8), McCabe complexity checker, and Vagrant integration (via command palette). Recently also a test runner and an import validator has been added to the already reach set of features.

So which one is the best? It depends. I have settled on Anaconda, since I really enjoy the `Go to definition`, `Show documentation`, and `Find usage` features and use them quite often - especially when dealing with large projects and/or large files. However, if you need a linter that just works and don't want to spend time in playing around with its configuration, SublimePythonIDE is probably the right choice. On the contrary, you don't mind tinkering a bit with settings files and you are looking for a wider set of IDE-like functions, Anaconda is definitely worthy a shot.
