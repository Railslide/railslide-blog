Title: Travis, Mock, different Python versions and an afternoon of frustration
Date: 2016-05-08
Category: /dev
Tags: travis-ci, python, python3, mock
Slug: travis-mock-afternoon-of-frustration
Author: Giulia Vergottini
Summary: My plan was to quickly set up Travis CI for Subvenv and then move on to other projects. Instead, it came out that I couldn't have been more wrong and I ended up instead in an afternoon of frustration.
Status: draft

I have been tinkering for a while with the idea of setting up Travis CI for Subvenv. I mean, automatically running tests on pull requests sounded like a great idea and the getting started guide seemed pretty straightforward, so why not use a bit of my today free-for-coding time for setting Travis up?

Armed with enthusiasm, I set up the `.travis.yml` configuration file, granted the necessary GitHub permissions, enabled Travis for Subvenv, pushed, and... build failure!

There's always a first time (for a failure)
-------------------------------------------
Ok, you know the old adage: _if it compiles the first time, there must be something wrong_. And in a similar fashion, this first failure didn't come at all as a surprise. Not a big deal. Also, the build for Python 3.4 succeeded, which is good.

I checked out the error messages and - of course - it complains since it couldn't find the `unittest.mock` in Python 2. Since I'd rather not add dependencies that are not strictly necessary for setting up the development environment, I was quite happy to read that Travis CI automatically installs mock in its testing environments. So, I wrapped my import statement in a try-except block as such:

    :::python
    try:
        from unittest.mock import patch, mock_open
    except ImportError:
        from mock import patch, mock_open

To be honest, I am not super glad about an import that relies on a non-mandatory dependency, but let's play along for now and let's get Travis up and running - I can always come up with something better on a later moment.

Ok so, commit my hack, push, and hold my breath for a handful of seconds. Does it work? Nope.

Builtins, __builtins__, and better mocking decisions
----------------------------------------------------
Since Subvenv relies on I/O operations for doing its job, I made sure to mock them away when writing my tests. However, since I use Python 3 as my default, I had initially mocked the `open` function like this:

    :::python
    patch('builtins.open', m, create=True)

That of course didn't work in Python 2, since the module is called `__builtin__`. So, after a hacky and unsuccessful attempt, I ended up in rewriting my mock in a more specific and robust way. In fact, instead of patching the function within the Builtins module, I patched directly the function call made inside my module:

    :::python
    patch('subvenv.core.open', m, create=True)

In this way, there's no need to worry about where the function comes from, since all it matters is that it gets called within my module's namespace.

Python 2.6 and Unittest
-----------------------

In the meanwhile, Python 2.6 was throwing its own kind of errors. That wasn't a big problem either, since I had added it to list of interpreters mostly out of curiosity. Nevertheless, I did a check on the errors and investigated its causes a bit and it came out that before 2.7 it wasn't possible to use `self.AssertRaises` as a context manager (see [here](https://docs.python.org/2/library/unittest.html#unittest.TestCase.assertRaises) and [here](https://bugs.python.org/issue4444)).

Supporting Python 2.6 has never been on my roadmap and adapting my tests to it didn't seem worth the effort, so I didn't think twice about ditching it from the interpreters list.

Which mock?
-----------
Ok, so back to my mocks! Now they get imported and patch what they need to patch, but still don't seem to work as expected. Or rather, it looks like there's something off with the `mock_open` helper, since for some reason it returns a `MagicMock` instance instead of the specified `read_data`.

After a bit of head scratching and googling, I found a [feature request](https://github.com/travis-ci/travis-ci/issues/5849) to Travis that shaded light over my own problem. Thanks to it I got to discover that Travis runs an old version of Mock (I haven't figure out which one exactly, but for sure older than 1.3.0) which does not implement `mock_open` as later versions do. Thankfully the same issue suggested also a workaround for it, i.e. to add an explicit install command for the desired version to the configuration file:

    :::yaml
    install:
      - pip install .
      - pip install mock==2.0
      - pip install -r requirements.txt


Mock and Python 3.3
-------------------
Ok, after the last changes, I managed to add Python 2.7 to the successful builds list. However, Python 3.3 shows up still in red and the error message is basically the same one I got when I add the Mock version issue in Python 2.7. That's weird!

Just to be sure, I double checked: yes, Mock is already part of the Unittest module in Python 3.3 and yes, its implementation of the `mock_open` does take `read_data` as an argument. However, as the documentation specifies, the `readline` and `readlines` method have been added in version 3.4, hence my error.



On top of that, I didn't even got to test with Python 3.2, since it has been throwing a not better specified error while installing a dependency (pypandoc).

