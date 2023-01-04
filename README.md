railslide.io
============

This repository contains the source of my blog, [railslide.io](https://railslide.io)

The blog is powered by [Pelican](https://github.com/getpelican/pelican) and hosted on GitHub pages.

Setup
-----

`poetry install`


Local development
-----------------

Create a new empty article with all the metadata scaffholding in place with

```
python newarticle.py [category_name]/[filename].md
```

**Note:** the command will fail if a directory with the given category name doesn't already exists (this is done to avoid mistakenly creating new folders due to typos). So if you are going to inrtoduce a new category, create the directory first and then run the script.

To render the blog, start the development server with `poetry run make devserver` and point your browser to http://localhost:8000

Use `poetry run make stopserver` to stop the development server.

Deployment
----------

Push the updated master branch and then run `poetry run make github`
