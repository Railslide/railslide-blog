# railslide.io

This repository contains the source of my blog, [railslide.io](https://railslide.io)

The blog is powered by [Pelican](https://github.com/getpelican/pelican) and hosted on GitHub pages.

## Setup

Create a virtualenv with your favourite virtualenv management tool and then install dependencies

```
pip install -r requirements-dev.txt
```

## Writing content

Create a new empty article with all the metadata scaffholding in place with

```
python newarticle.py [category_name]/[filename].md
```

**Note:** the command will fail if a directory with the given category name doesn't already exists (this is done to avoid mistakenly creating new folders due to typos). So if you are going to inrtoduce a new category, create the directory first and then run the script.

To render the blog, start the development server with `pelican -l -r` and point your browser to http://localhost:8000


## Deployment

Push the updated master branch and then run `make github`

## Local Python development

If you need to do changes to the article creation script, requirements, etc. you can use Tox for the mundane stuff.

#### Linting/formatting
```
tox -e format
```

#### Updating/compiling requirements
```
tox -e requirements
```
