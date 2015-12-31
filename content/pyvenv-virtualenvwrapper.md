Title: Using pyvenv with virtualenvwrapper
Date: 2015-05-15
Category: /dev
Tags: virtualenvwrapper, virtualenv, python3, pyvenv
Slug: pyvenv-virtualenvwrapper
Author: Giulia Vergottini
Summary: Short version for index and feeds
Status: draft

Python 3 ships with pyvenv, a built-in virtualenv management. Although I welcomed the news as a definitely good one, the absence of a virtualenvwrapper-like tool for pyvenv has always stopped me from giving it a try. I find virtualenvwrapper a super neat tool (I even wrote a plugin for it!) and I don't see why I would want to type the path to my python interpreter every time I want to create a new virtualenv, when I can just use a way more pythonic `mkvirtualenv my_venv`.

I happened, however, to run into [this conversation](https://groups.google.com/forum/#!msg/virtualenvwrapper/bkpwkfyIppM/9M9mz3pB0RQJ) in virtualenvwrapper google group, where Dough Hellman aka the guy behind virtualenvwrapper says that **in theory** it should be possible to use virtualenvwrapper with pyvenv. So I immediately fired up a couple of virtual machines and started playing around in order to see whether it was possible to turn that _in theory_ into an _in practice_.

TL;DR: yes, it is possible by setting `VIRTUALENVWRAPPER_VIRTUALENV='pyvenv'` in your bash profile. There are some caveats though, which are described below.

1. Which pyvenv?
----------------

According to Python documentation (for Python 3.4.2 at the time of writing) I should be able to invoke pyvenv by simply calling `pyvenv [options]`. However, that is not the case for Python 3.4.0 which is the version of Python 3 shipped with Ubuntu 14.04. Thus, my first attempt to set my `VIRTUALENVWRAPPER_VIRTUALENV` variable equal to `pyvenv` resulted in my vagrant machine complaining because it could not find it in my path. Setting it to `pyvenv-3.4` solved it, even though having to manually change it whenever I decide to update my Python version is far from optimal.


2. Trusty bug
-------------

So I set `pyvenv-3.4` as `VIRTUALENVWRAPPER_VIRTUALENV`, created a new virtualenv and...

    Error: Command '['/home/vagrant/.virtualenvs/test/bin/python3.4', '-Im', 'ensurepip', '--upgrade', '--default-pip']' returned non-zero exit status 1

Ok, not exactly what I was hoping for.

After a bit of digging, it came out that it is due [to a bug](https://bugs.launchpad.net/ubuntu/+source/python3.4/+bug/1290847) in Ubuntu 14.04 (Trusty Tahr). At the time of writing a fixed was released, but not yet distributed through apt-get. However, it is possible to bypass the problem by first creating the virtualenv without pip and then manually installing it once inside the virtualenv.

    mkvirtualenv --without-pip my_venv
    curl https://bootstrap.pypa.io/get-pip.py | python
