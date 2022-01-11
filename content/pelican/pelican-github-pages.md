Title: How to set up Pelican on GitHub pages
Date: 2014-06-09
Tags: pelican, publishing, github pages
Slug: pelican-github-pages
Summary: How to set up Pelican on GitHUb pages and a custom domain


Although the web is plenty of blog posts about how to set up a Pelican powered blog on GitHub pages, I still had to glean information from several sources and mix it with a bit of experimentation before being able to have my blog up and running. So hopefully this post will make someone's life easier, other than being a future reference for myself.

Before starting I need to give credit where credit is due, since [this post](http://mathamy.com/migrating-to-github-pages-using-pelican.html) by Amy Hanlon and [this one](http://martinbrochhaus.com/pelican2.html) by Martin Brochhaus have been a tremendous starting point for my trial-and-error journey. Once said that, we can start.


1. Setting up GitHub project pages
==================================

GitHub offers the possibility to host your site in the cloud through either [personal or project pages](https://help.github.com/articles/user-organization-and-project-pages). Although it is possible to use both for hosting a Pelican powered blog, project pages make your life so much easier when it comes both to publish your blog content and to put blog source under revision control.

For creating project pages, all we need to do is to create a repository as usual and put the content we wish to publish (i.e. the HTML static files) into a branch named `gh-pages`. Once done that, your page will show up at username.github.io/repository.

Although it could sounds overly complicated - especially the `gh-pages` branch part - you don't have to worry since an awesome program called [ghp-import](https://github.com/davisp/ghp-import) will take care of it for us. For now, simply create a new repository as you would do for any other project and set up a `.gitignore` file with the following content:

    *.pid
    *.pyc
    output/


2. Installing the needed packages
=================================

Before installing Pelican, I would recommend to create a new virtualenv. It is not mandatory, but it is definitely a good practice and would prevent the risk of conflicts between installed packages.

NOTE: Pelican documentation recommends to use Pelican with Python 2.7. I am keeping up with [my pledge of using Python 3 whenever possible]({filename}/dev/virtualenwrapper-ubuntu-python3.md), as well as giving a try with Python 3.4 (Ubuntu 14.04 default version). Everything works fine so far and anyways these instructions are version agnostic - just be aware of it and choose your Python version accordingly.

Install pelican and ghp-import

    :::bash
    pip install pelican
    pip install -e git+git://github.com/davisp/ghp-import.git#egg=ghp-import


Next run `pelican-quickstart` and get ready to answer to a bunch of questions. Most of them are pretty straightforward and anyway you'll be able to change them later in your settings files. These are the only ones you need to care about for the moment:

    ::bash
    Where do you want to create your new web site? [.] # Press enter
    Do you want to specify a URL prefix? e.g., http://example.com (Y/n) # y
    What is your URL prefix? (see above example; no trailing slash) # http://username.github.io/repository
    Do you want to generate a Fabfile/Makefile to automate generation and publishing? (Y/n) # y

Answer `n` to all the questions about uploading your website and you are ready to go.


3. Writing content
==================

Fire up your favorite text editor and write your blog content in either Markdown or reStructuredText. Once you have done, save it in the content folder. For previewing it:

    :::bash
    make devserver
    # go to http://localhost:8000 and check if everything looks good
    ^C # note that CTRL+C won't stop dev server
    ./develop_server.sh stop # manually stop the dev server


4. Publishing and pushing
=========================

Ok this is the easy part.

    :::bash
    # pushing the source repo
    git push origin master

    # push the output folder to GitHub pages
    make github

    # celebrate!

Congrats! Your blog is now up and running!


5. Setting up your custom domain
================================

Create a CNAME file containing your bare domain:

    mydomain.com

Add the following lines to your pelicanconf.py, in order to make Pelican copying it to your output folder on every publish.

    :::python
    STATIC_PATHS = [
    'CNAME'
    ]

Then, assuming that you want both mydomain.com and www.mydomain.com to point at your blog, you need to set **both the CNAME and the A-records** of your domain to point at github.

Since this has been the most problematic step for me, here's a couple of extra thoughts regarding my domain registrar (Gandi):

1. Make sure to not have any other A-record
2. Using Gandi's web forwarding instead of setting both the CNAME and the A-records resulted in a redirect loop error
3. You can take the rest of the zone file data from Gandi's default one
4. Testing from different browsers and refreshing several times can help spotting some very sneaky bugs
5. [This answer](http://stackoverflow.com/a/22374542/2926113) from Stack Overflow provides great step-by-step instructions for using GitHub project pages with a custom domain

Here are the lines taking care of the magic in my case:

    www 10800 IN CNAME railslide.github.io.
    @ 10800 IN A 192.30.252.153
    @ 10800 IN A 192.30.252.154

After that, wait some hours for the DNS to propagate and you should be done.
