# railslide.io

This repository contains the source of my blog, [railslide.io](https://railslide.io)

The blog is powered by [Pelican](https://github.com/getpelican/pelican) and hosted on GitHub pages.

## Setup

Create a virtual environment and install dependencies
```
uv venv
uv sync
```

## Writing content

Create a new empty article with all the metadata scaffholding in place with

```
uv run newarticle.py [category_name]/[filename].md
```

**Note:** the command will fail if a directory with the given category name doesn't already exists (this is done to avoid mistakenly creating new folders due to typos). So if you are going to introduce a new category, create the directory first and then run the script.

To render the blog
```
uv run make devserver
```
and point your browser to http://localhost:8000


## Deployment

Push the updated master branch and then run `uv run make github`
