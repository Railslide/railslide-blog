Title: Make pyenv and pyright play nice together
Date: 2023-03-12
Tags: python, neovim
Slug: make-pyenv-and-pyright-play-nice-together
Summary: If you use `pyenv local`, Pyright will not automatically pick up the correct virtualenv. Here's an explanation of why it happens and how to work around it.  

Some time ago I started looking into setting up the built-in LSPs in Neovim, and being Python my main programming language, I set up [Pyright](https://github.com/microsoft/pyright/) as my first language server and gave it a spin. While all the basics things worked out of the box, I kept getting a bunch of `Import "some_module" could not be resolved`. After having ruled out the classic mistakes (i.e. forgetting to install dependencies, or running Neovim from the wrong folder), and ran some test ([Ale](https://github.com/dense-analysis/ale) recognized my virtualenv as expected), all that was left was that somehow Pyright did not play along with my virtualenv.

## Why it happens

By default Pyright tries to be smart and to automatically pick up existing virtualenvs. When it comes to Pyenv, Pyright checks whether `$PYENV_VERSION` is set and determines which Python interpreter to use from its value. So far so good.

  The problems however start when using `pyenv local`. Basically [pyenv-virtualenv](https://github.com/pyenv/pyenv-virtualenv) has this super nifty function that couples the specified virtualenv with the current folder, so that it gets automatically activated whenever you `cd` into the directory (and deactivate once you move away from it). However, whenever the virtualenv gets automagically activated, the `$PYENV_VERSION` variable doesn't get set (and apparently that's [by design](https://github.com/pyenv/pyenv/issues/1760), and hence unlikely to change anytime soon).

## How to solve(ish)

If you need to fix something on the fly, forcing Pyenv to set the environment variable by using `pyenv shell <env_name>` is a quick way to work around the issue. It's worth mentioning, however, that it's only temporary and that you will have type it again every time you start a new shell. So great for debugging, but not ideal as a long term solution.

A more long term solution is to leverage Pyright configuration options. For doing so, you need to create a `pyrightconfig.json` file in the root of your project with the following content

```json
{
  "venvPath": "<PYENV_ROOT>/versions",
  "venv": "<ENV_NAME>"
}
```

where `PYENV_ROOT` is the output of `echo $PYENV_ROOT` and `ENV_NAME` is the name of your virtualenv.

Keep in mind though that `pyrightconfig.json` <u>does not support shell variables</u>, so stuff like `~/.pyenv/versions` won't work.

While this is a way better method, it still requires a lot of typing. Wouldn't be great if it was possible to automate this somehow? Enter [pyenv-pyright](https://github.com/alefpereira/pyenv-pyright), a Pyenv plugin that takes care of handling `pyrightconfig.json` on your behalf. So now all you have to do is to type `pyenv pyright` once and you're ready to go!

Happy coding!

## Resources

- [pyenv-pyright](https://github.com/alefpereira/pyenv-pyright)
- [Pyright configuration options](https://github.com/microsoft/pyright/blob/main/docs/configuration.md)
