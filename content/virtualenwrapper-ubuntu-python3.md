Title: Installing virtualenvwrapper for Python 3.4 on Ubuntu
Date: 2014-06-04
Category: Python
Tags: virtualenvwrapper, virtualenv, python3.4
Slug: virtualenvwrapper-python3
Author: Giulia Vergottini
Summary: Virtualenvwrapper is a great virtualenv management tool. Here is how I set it up for Python 3.4 on Ubuntu.


After listening to an inspiring talk by [Kenneth Reitz](http://www.kennethreitz.org/) about transitioning from Python 2 to Python 3 at PyCon Sweden (I'll write a blog post about it sooner or later), I've decided that I should try to stick to Python 3 as much as possible.

So the first step in that direction was to set up my working environment in a Python 3 friendly way, hence to install Virtualenwrapper for Python 3. Here's how I did it.

Virtualenwrapper documentation specifies that Virtualenvwrapper has been tested under Python 2.6-3.3, but no mention of Python 3.4. Being lazy and not really willing to install a third version of Python on my computer (Ubuntu 14.04 comes with Python 2.7.6 and Python 3.4 by default), I decided to give it try with what I had. Everything seems to work flawlessly so far, just keep it in mind in case you want to try to follow these instructions.

Setting up Virtualenvwrapper
----------------------------

Install pip for Python 3:

    :::bash
    sudo apt-get install python3-pip


Install Virtualenvwrapper for Python 3:

    :::bash
    sudo pip3 install virtualenvwrapper

So far so good. Now it is time to configure Virtualenvwrapper.

Create a folder for your virtualenvs (I use ~/.virtualenvs) and set it as WORKON_HOME:

    :::bash
    mkdir ~/.virtualenvs
    export WORKON_HOME=~/.virtualenvs

Add the following lines to ~/.bashrc:

    VIRTUALENVWRAPPER_PYTHON='/usr/bin/python3' # This needs to be placed before the virtualenvwrapper command
    source /usr/local/bin/virtualenvwrapper.sh

Close and re-open your shell and you're ready to go. Here are the basic commands for using virtualenvwrapper:

    :::bash
    mkvirtualenv virtualenv_name # Create virtualenv
    workon virtualenv_name # Activate/switch to a virtualenv
    deactivate virtualenv_name # Deactivate virtualenv

Congratulations! Your Virtualenvwrapper for Python 3 is now ready to use. However, being I lazy and a strong supporter of the idea that [tedious and repetitive tasks should be automated](http://xkcd.com/1319/), I added a couple of extra behaviors to Virtualenvwrapper settings.

Projects and Postactivate
-------------------------

My typical workflow is to create a virtualenv and then create a project folder with the same name. So why not setting up Virtualenvwrapper to automatically do it for me every time I create a new virtualenv? Specify PROJECT_HOME in ~/.bashrc will do the trick:

    VIRTUALENVWRAPPER_PYTHON='/usr/bin/python3'
    PROJECT_HOME='/path/to/where/you/want/your/project/folder/to/be/created' # This needs to be placed before the virtualenvwrapper command as well
    source /usr/local/bin/virtualenvwrapper.sh

Now, when typing

    :::bash
    mkproject my_project

Virtualenvwrapper will automatically create a virtualenv and a folder called *my_project*.

Finally I set up virtualenvwrapper to automatically navigate to the project folder on virtualenv activation, by adding the following lines to my postactivate script:

    project_name=$(basename $VIRTUAL_ENV)
    cd ~/Projects/$project_name

So when typing

    :::bash
    workon my_project

Virtualenvwrapper activates the virtualenv and teleports me to ~/Projects/my_project. Neat!

