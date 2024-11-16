Title: Uv gotchas
Date: 2024-11-16
Tags: python, virtualenv, virtual-environments, uv
Summary: A collection of the things that caught me offguard while using uv.

Since [uv](https://docs.astral.sh/uv/) seems to be the new cool kid on the python packaging and project management scene, I decided to trying it out. I mostly explored the virtual environment part, as I was trying to see if I could replace pyenv with it. Here are things that caught me off guard while doing so.

## Running `uv venv` again will wipe your environment

Since the list of things I want to do it's constantly growing and time is limited, it's not uncommon for me to go back to an existing project after some months of break. Consequently, I often don't remember whether I had created a virtual environment for the project already. Now, with pyenv I'd rely on the virtualenv name been prepended to my terminal prompt (at least until that feature gets removed). That won't work with uv though, unless I manually activate the environment first. So my automatic reaction was to run `uv venv`, expecting it to throw an error if the virtualenv already exists. However, what has happened instead was that my existing virtualenv was completely wiped and created anew.

There is an [ongoing discussion about this issue](https://github.com/astral-sh/uv/issues/1472), so this will hopefully change in the future.

## If you run `pip` instead of `uv pip` you might get confused

If you want to install a package in your uv-based virtualenv you'll likely do
```
uv pip install some_package
```

and if you want to list the packages installed you would do:

```
uv pip freeze
```

Now, if you by mistake forget to type `uv` at the start due to years of muscle memory, you might be accidentally installing a package in the wrong place or getting a very confusing freezing output as you might accidentally get the one system one instead.

A good workaround I found is to configure pip to require a virtualenv. That way, if I accidentally forget to type `uv`, I'll get a clear error telling me that pip cannot find a virtual environment.

To do so, I simply added a config file `~/.config/pip/pip.conf` with the following content
```
[global]
require-virtualenv = true
```

## Out-of-env `uv pip` commands won't work with non-default named envs

When creating an environment you have the possibility to specify a name/path, i.e. if you run
```
uv venv foobar
```
the virtualenv will be created in a folder called `foobar` instead of `.venv`.

However, doing so will also prevent all the `uv pip` commands from working as expected if you don't activate the environment first.

```bash
$ uv pip install some_package
error: No virtual environment found; run `uv venv` to create an environment, or pass `--system` to install into a non-virtual environment

$ source foobar/bin/activate
(foobar) $ uv pip install some_package
# package gets installed...
```

And while this is a bit annoying, it is still manageable. Though things get confusing when using `uv pip freeze`. Depending you setup, `uv pip freeze` might print the output of your system packages, i.e. it will basically do the same as you would do `uv pip freeze --system`.

This has also been reported to Astral and there are currently a bunch of ongoing discussions on how to best address it. This [github issue](https://github.com/astral-sh/uv/issues/1625) contains a good overview of the current status.

## Conclusion

While in general I really like the idea behind uv and I still hope for a tool to become THE ONE (instead of the [10+ that we currently have](https://chriswarrick.com/blog/2023/01/15/how-to-improve-python-packaging/)), I think this is a good reminder that we are talking about a tool that has yet to reach 1.0 - and hopefully this article will save someone from stumbling upon the very same quirks I encountered. That being said, I still plan to play around more with uv and I am especially curious about its project management functions, so who knows - this article might have follow up :)
