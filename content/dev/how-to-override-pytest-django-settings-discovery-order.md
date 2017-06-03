Title: How to override pytest-django settings discovery order
Date: 2016-09-29
Category: /dev
Tags: django, pytest, pytest-django, environment variables
Slug: how-to-override-pytest-django-settings-discovery-order
Author: Giulia Vergottini
Summary: The order pytest-django uses for determining which settings file should be used for running tests might not be the most optimal when using environment variables. However, it is still possible to override it so that it picks up the correct file without recurring to extra typing.


If you want to use Pytest for running the test suite in your Django project, all you need to do is to install pytest-django, tell it where to look for the Django settings file - usually by placing a `pytest.ini` file in the project root folder - and you're ready to go. However, even though the `pytest.ini` file is probably the most common way to point pytest-django to the settings file, it also the last place in which pytest-django will look for it. In fact, every time you run `pytest`, pytest-django will check for the `DJANGO_SETTINGS_MODULE` variable in the following order:

* command line option with `--ds`
* environment variables
* `pytest.ini` file

While this order would work perfectly fine for many projects, if you happen to have an enviroment variable pointing to a different settings file (e.g. if you're running your project in a Docker container), it might reveals itself as a bit of a bummer. So, what are the available options for preventing django-pytest from picking up the wrong variable?


Using the `--ds` option
-----------------------

This is probably a no-brainer, but the most obvious way to make sure pytest-django picks up the right settings file is to pass the `--ds` option when invoking `pytest` from the command line.

While it certainly works, it adds quite a lot of typing - especially if you use a [settings module instead of a single setting file](https://www.rdegges.com/2011/the-perfect-django-settings-file/), since it could easily translate into

    :::bash
    $ pytest --ds=project_folder.settings_folder.settings_file


Certainly not something I'd like to do every time I want to run the test suite.


Setting the environment variable
--------------------------------

Another way around the issue is to set the environment variable to the test settings file before every test run and the setting it back to its original value once you're finished.

However, besides still requiring quite a lot of typing, this method is also extremely error prone. What if you forget to set the environment variable back after test running? So, unless you're willing to take the risk of frustrating debugging time trying to figure out why your app is not working as it should, this option is pretty much a no-op.


Using `addopts` in the `pytest.ini` file
----------------------------------------

Wouldn't be awesome if you could just use the `pytest.ini` file, set all the necessary settings in there, and not have to worry ever again? Actually you can, thanks to [`addopts`](http://doc.pytest.org/en/3.0.2/customize.html#confval-addopts).

What `addopts` does is to add options (hence the double d!) to your test run as if they were specified via command line. So, for example, if you want to update and export coverage every time you run the suite, you would write this in the `pytest.ini` file

    :::ini
    [pytest]
    addopts =
        --cov=.
        --cov-report=html


and every time you run `pytest` it will, behind the scene, be interpreted as if you have run

    :::bash
    $ pytest --cov=. --cov-report=html

Thus, by adding `--ds=project_folder.settings_folder.settings_file` to `addopts` it is possible to override pytest-django discovery order and make sure that the value in the `pytest.ini` file gets read instead of environment variable.

Ok, but what if you want to point pytest to a different settings file for one run only? No problem! One of the perks of this method is that you can esplicitly pass the `--ds` option from the command line to override the one in the `pytest.ini` file. So running

    :::bash
    $ pytest --ds=other_settings_file

will just work as usual. Neat!

