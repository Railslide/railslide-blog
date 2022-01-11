railslide.io
============

This repository contains the source of my blog, [railslide.io](https://railslide.io)

The blog is powered by [Pelican](https://github.com/getpelican/pelican) and hosted on GitHub pages.

Setup
-----

`poetry install`


Local development
---------------

To render the blog, start the development server with `poetry run make devserver` and point your browser to http://localhost:8000

Use `poetry run make stopserver` to stop the development server.

Deployment
----------

Push the updated master branch and then run `poetry run make github`
