Title: How to set up Pelican on GitHub pages
Date: 2014-05-26
Category: Pelican
Tags: pelican, publishing, github pages
Slug: pelican-github-pages
Author: Giulia Vergottini
Summary: How to set up Pelican on GitHUb pages
Status: draft

For setting up this blog I started by following [this posts](http://mathamy.com/migrating-to-github-pages-using-pelican.html) by Amy Hanlon. All went great until I decided to take a look at the code of the makefile and discovered a `make github` option. Thus I started wondering whether there was a better way to integrate Pelican with GitHub pages and landed on a [post](http://martinbrochhaus.com/pelican2.html) by Martin Brochhaus, which convinced me to use [project pages rather than personal ones](https://help.github.com/articles/user-organization-and-project-pages).

So,
The only thing that remained a bit unclear in my journey toward my Pelican powered blog was when I was supposed to push the source code. Here's the workflow I eventually came up with:

    :::bash
    # Write some content

    # check if everything works fine
    make devserver

    # pushing the source repo
    git push origin master

    # push the output folder to GitHub pages
    make github

    # stop the dev server
    ./develop_server.sh stop

    # celebrate!
