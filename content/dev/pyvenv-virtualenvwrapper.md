Title: Using pyvenv with virtualenvwrapper
Date: 2016-06-07
Category: /dev
Tags: virtualenvwrapper, virtualenv, python3, pyvenv
Slug: pyvenv-virtualenvwrapper
Author: Giulia Vergottini
Summary: After reading that it might be possible to use virtualenvwrapper with pyvenv, I decided to fire up a couple of virtual machines and to find it out.

Python 3 ships with pyvenv, a built-in virtualenv manager. Although I welcomed the news as a definitely good one, the absence of a virtualenvwrapper-like tool for pyvenv has always stopped me from giving it a try. I consider virtualenvwrapper to be a super neat tool (I even wrote a plugin for it!) and I don't see why I would want to type the path to my virtual environment activation script every time I want to activate it, when I can just use a way more pythonic `workon my_venv`.

I happened, however, to stumble into [a conversation](https://groups.google.com/forum/#!msg/virtualenvwrapper/bkpwkfyIppM/9M9mz3pB0RQJ) in the virtualenvwrapper google group, where Doug Hellman (aka the guy behind virtualenvwrapper) wrote that _in theory_ it should be possible to use virtualenvwrapper with pyvenv. So I immediately fired up a couple of virtual machines and started playing around in order to see whether it was possible to turn that _in theory_ into an _in practice_.

The Ubuntu mess
---------------

According to Python documentation I should be able to invoke pyvenv by simply calling `pyvenv [args]`. However, that is not the case for Ubuntu. Thus, my first attempt to set my `VIRTUALENVWRAPPER_VIRTUALENV` variable equal to `pyvenv` resulted in my vagrant machine complaining because it could not find it in my path. Setting it to `pyvenv-3.4` solved it (I was initially testing on Ubuntu 14.04, which ships with Python 3.4). Though having to manually change it whenever I decide to update my Python version is far from optimal.

So I set `pyvenv-3.4` as `VIRTUALENVWRAPPER_VIRTUALENV`, created a new virtualenv and...

    :::bash
    Error: Command '['/home/vagrant/.virtualenvs/test/bin/python3.4', '-Im', 'ensurepip', '--upgrade', '--default-pip']' returned non-zero exit status 1

Ok, not exactly what I was hoping for.

After a bit of digging, it came out that it is due [to a bug with ensurepip](https://bugs.launchpad.net/ubuntu/+source/python3.4/+bug/1290847) in the first release of Ubuntu 14.04. However, it is possible to bypass the problem by first creating the virtualenv without pip and then manually installing it once inside it.

    :::bash
    $ mkvirtualenv --without-pip my_venv
    (my_venv)$ curl https://bootstrap.pypa.io/get-pip.py | python

Quite a lot to type, plus you have to wait for Pip to install. Definitely not optimal.

Fortunately the issue has been solved in Ubuntu 14.04.2 (which allowed me to perform my tests), but for some reason the whole pyvenv package has been [removed in Ubuntu 14.04.03](http://askubuntu.com/questions/682612/pyvenv-3-4-disappeared-in-ubuntu-14-04-3).

Ok, not exactly an encouraging scenario... but hey! Ubuntu 16.04 has been released in the meanwhile and it ships with Python 3.5! Maybe things have changed in the new LTS? Well, apparently not, since getting an image with a working pyvenv package looks pretty much like a lottery: you pick one and hope for the best.

The vagrant box `20160521.0.0` shipped with a working pyvenv, but then it disappeared from the catalog. The `20160528.0.0` one brings back to the good old ensurepip bug, while in the `20160606.1.0` pyvenv seems to work again. For the sake honesty, it might be a problem related to the vagrant boxes only, since this wasn't the [only](https://github.com/mitchellh/vagrant/issues/7288) [issue](https://groups.google.com/d/msg/vagrant-up/cUXVwSDi4vc/OhyXR-G7CAAJ) I encountered. But at this point I already started to wonder whether the pyvenv package will be ever stable enough to be used in everyday development.

The only good news is that in 16.04 the package can also be installed and invoked through a more generic alias (`python3-venv` for installing and `pyvenv` for invoking), so that - if it will ever become stable - you will have no longer to worry about manually updating your pyvenv version in your shell start file.


What doesn't work when it works
-------------------------------

Leaving Ubuntu peculiarities apart, the initial question remains: assuming a working pyvenv package, is it possible to use it as a replacement for virtualenv in virtualenwrapper?

The answer is yes, but with some gotchas.

All the site packages related commands, i.e

* `lssitepackages`
* `toogleglobalsitepackages`
* `cdsitepackages`
* `add2virtualenv`

don't work and they all raise

    :::python
    AttributeError: 'module' object has no attribute 'sysconfig'

`cpvirtualenv` is instead a bit weird, since it does copy the virtualenv, but it displays the name of the original one in front of the prompt of all its copies. Even making copies of a copy doesn't change the result: it still shows the name of the first original. The `$VIRTUAL_ENV` variable and the interpreter point to the correct folder tho...

Last but not least, is probably worthy mentioning that - by design - pyvenv doesn't offer the possibility to specify a Python interpreter for virtual environments, so

    :::bash
    $ mkvirtualenv -p /path/to/python/interpreter my_venv

no longer works, which means no way to get a Python 2.7 virtualenv out of it.

All the rest work as expected.

Summing up
----------

Before I started experiment with it, I was seriously tinkering with the idea of dropping virtualenv altogether and use pyvenv instead. However, after seeing the results, it looks like it's not going to be the case. Not much for the site packages commands - I think this was the first time I ever used them - but rather for the impossibility to switch to Python 2.7 when needed.

Also, the whole Ubuntu situation is quite a show-stopper for me, since I don't really want to rely on hoping that everything still works every time I run an `apt update`.

So, at the current status, replacing virtualenv with pyvenv is definitely a no-op for me. However, if you want to give it a try, I uploaded the Vagrantfiles for the virtual machines in a [GitHub repo](https://github.com/Railslide/pyvenvwrapper). They're provisioned with a shell script, so that there's no need to install any fancy tool for running them. Feel free to play with them and don't forget to give me a shout if you find a way to fix those issues!
