Title: Subvenv!
Date: 2016-02-
Category: /dev
Tags: subvenv, announcements, virtual environments, python
Slug: subvenv-v1-0-0
Author: Giulia Vergottini
Summary: Subvenv 1.0.0 is out! What you need to know about it and why you should use it.
Status: draft

A couple of days ago I released and upload to PyPI the first stable release of `subvenv`.

The reason why I wrote it is that I am lazy and I love to have computers taking care of boring and repetitive tasks on my behalf. More specifically, I wasn't happy with my typical workflow for starting a new project. In fact, before I could start crunching some code:

* create a Virtualenvwrapper project
* open Sublime Text
* create a Sublime Text project
* add the previously created folder to the project file
* add the virtual environment interpreter path to the project file, so that linting plugins could pick that one instead of the global one

With Subvenv instead:

* create a Virtualenvwrapper project
* open Sublime Text
* open the Sublime Text project
