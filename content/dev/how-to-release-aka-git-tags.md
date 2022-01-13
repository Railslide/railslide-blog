Title: How to release your code (aka Git tags)
Date: 2016-04-02
Tags: git, github, release
Slug: how-to-release-aka-git-tags
Summary: After spending quite some time working on your side project, you feel that it is finally good enough for going public. Releasing sounds like a super neat idea, but how do you do it?


After spending quite some time working on your side project, you feel that it is finally good enough for going public. Releasing sounds like a super neat idea, but how do you do it?

Releasing through Github
-------------------------

Github provides a very straightforward release interface. All you need to do is to click on the releases counter, press the _"Create a new release"_ button, fill the form, submit, and you're done. Github also offer the possibility to draft releases - which comes in handy if you want to start preparing the release while still working on the code for it - or pre-releases, in case your code is not really stable yet.

Github also provides you with a fancy link in the form of github.com/Username/repo/releases/latest, which will allow people to get directly to the latest release, no matter its number.


Releasing from the command line (with Git tags)
-----------------------------------------------

Github interface it is certainly nice, but it comes to the price of making your release workflow dependent on Github. What if a certain point you decide that you want to move your code away from Github? Also wouldn't be awesome if you could take care of your releases directly from your trusted terminal? Well, it turns out that you can, since what Github does behind the scene is to create and set a Git tag on the repository.

Tags in Git are a way to set a reference to a specific point in history. You can think of them as a way to _bookmark_ a specific commit. So when you download the source code for your-awesome-project.v1.1.0 you're basically saying "Hey Git, fetch me the code up to the point that correspond to the commit tagged with the name your-awesome-project.v1.1.0".

You can set a tag with the `git tag` command. However, before you go git-tagging all the things, you should probably be aware that there are two kinds of tags in Git: annotated and lightweight. As the man page for `git-tag` explains:

    Tag objects (created with -a, -s, or -u) are called "annotated" tags;
    they contain a creation date, the tagger name and e-mail, a tagging
    message, and an optional GnuPG signature. Whereas a "lightweight" tag
    is simply a name for an object (usually a commit object).

    Annotated tags are meant for release while lightweight tags are meant
    for private or temporary object labels. For this reason, some git
    commands for naming objects (like git describe) will ignore lightweight
    tags by default.

To be honest, I still haven't yet figured out a good case for lightweight tags - if you have, give me a shout 'cause I'd love to know! Anyways, the bottom line is: **do not forget the `-a` flag when you're trying to make a release**.

Ok, back to our release!

    ::bash
    $ git tag -a v1.0.0 -m "My awesome message for v1.0.0"
    $ git push --tags  # tags need to be pushed explicitly

Done!


Happy ending? Almost...
-----------------------

OK, so after pushing your latest release via command line, you go an check Github to see if everything worked as expected. The counter increased - which is good - but if you had done any previous release via GUI the releases page might not look exactly how you would have expected it. In fact, even though Github correctly displays your tags, it doesn't mark it as the latest relase.

The reason for that is that at the time of writing Github doesn't fully support releases made via command line. That's a bummer and unfortunately there's nothing we can do other than hoping that the folk at Github will implement it soon.

However, leaving it as it is doesn't really qualify as an option since having a flag and a direct link pointing to the wrong release is worse than not having them at all. So what our workaround options? We could use the Github interface to mark a tag as the latest release, though it would add extra manual work to the release process and - again - making it dependent on Github. Alternatively it possible is to remove the Github sugarcoat from previous releases, so that the _latest release_ flag disappears. The downside of doing so is that the direct link to the latest release won't work anymore.

Unfortunately, every workaround has its flaws, so which one would work best depends on what your needs are and what compromises you're ready to make. Other than that, happy releasing!
