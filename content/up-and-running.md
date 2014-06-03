Title: Up and running!
Date: 2014-06-03
Category: Pelican
Tags: pelican, publishing, github pages
Slug: up-and-running
Author: Giulia Vergottini
Summary: Celebrating the first post of the blog, giving credits where credits are due, what to do next.

Ok, my Pelican and GitHub pages powered blog seems to be up and running! Yay!

For setting it up I started by following [this posts](http://mathamy.com/migrating-to-github-pages-using-pelican.html) by Amy Hanlon. All went great until I decided to take a look at the code of the makefile and discovered a `make github` option. Thus I started wondering whether there was a better way to integrate Pelican with GitHub pages and landed on a [post](http://martinbrochhaus.com/pelican2.html) by Martin Brochhaus, which convinced me to use [project pages rather than personal ones](https://help.github.com/articles/user-organization-and-project-pages).

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



TO DO (not necessarily in this order)
-------------------------------------

* Change theme - ideally developing my own
* Fix links, social buttons, etc.
* Fix an about page
* Setting up a comment system
* Write stuff
