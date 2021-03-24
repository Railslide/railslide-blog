railslide.io
============

This repository contains the source of my blog, [railslide.io](https://railslide.io)

The blog is powered by [Pelican](https://github.com/getpelican/pelican) and hosted on GitHub pages. More info about how I set it up can be found in [this blog post](http://railslide.github.io/railslide-blog/pelican-github-pages.html)

Setup
-----

`pipenv install`


Local development
---------------

To render the blog, start the development server with `pipenv run make devserver` and point your browser to http://localhost:8000

Use `pipenv run ./develop_server.sh stop` to stop the development server.

Deployment
----------

Push the updated master branch and then run `pipenv run make github`
