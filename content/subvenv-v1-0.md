Title: Subvenv
Date: 2016-03-01
Category: /dev
Tags: subvenv, announcements, virtual environments, python
Slug: subvenv-v1-0
Author: Giulia Vergottini
Summary: Subvenv 1.0 is out! What it is, why I wrote it, and why you might want to use it.


A couple of days ago I released and upload to PyPI the first stable release of [Subvenv](https://github.com/Railslide/subvenv). Besides being a labor of love, Subvenv is an utility for creating virtualenv-friendly Sublime Text project files.

The reason why I wrote it is that I am lazy and I love to have computers taking care of boring and repetitive tasks on my behalf. More specifically, I wasn't super happy with my typical workflow for starting a new project, since it required me a certain number of steps before being finally able to crunch some code.

Here's what my workflow used to look like:

* create a Virtualenvwrapper project
* open Sublime Text
* create a Sublime Text project
* add the previously created folder to the project file
* add the virtual environment interpreter path to the project file, so that linting plugins could pick that instead of the global one (and stop complaining about missing imports!)
* Start coding

Now with Subvenv instead:

* create a Virtualenvwrapper project
* open Sublime Text
* open the Sublime Text project
* Start coding

Way faster and less error prone! So, why not sharing it? I cleaned up the code a bit, made it more virtual environment management agnostic, and uploaded it on PyPI. Now it's out there. If you use Sublime Text you might want to have a look it - it may speed up your workflow too :)
