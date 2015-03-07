Title: Setting up a dotfiles repo and easily port configurations around
Date: 2014-07-10
Category: Utilities
Tags: dotfiles, utilities, git
Slug: dotfiles
Author: Giulia Vergottini
Summary: How I set up a repository containing my setting and configuration files and delegated the task of creating symlinks to the computer.


After having spent quite some time in finding the right set up for my developing environment, it came natural to look for a way for porting my configuration. Enter a dotfiles repo, aka having all my configurations only one `git clone` away and making my life so much easier.

Michael Smalley wrote an [amazing tutorial](http://blog.smalleycreative.com/tutorials/using-git-and-github-to-manage-your-dotfiles/) for managing dotfiles and creating a script for automagically installing them (go and check it out!), which provided me with a great starting point. However, his script handles only dotfiles housed in the home directory and that didn't really get together with my goal of adding Sublime Text settings to my dotfiles repo. So I fired up Nano and extended the script in order to make it do exactly what I needed.

First of all, I needed to to move Sublime configuration files to my dotfiles folder. Thankfully [Mark Nichols' post](http://zanshin.net/2013/01/21/sublime-text-2-dotfiles-simplified/) tipped me that I the only folder I needed to care about was the User one. So, after cleaning it up from some experiments leftovers, I moved to my dotfiles folder and placed a symlink in its previous location.

Then I added a variable holding the path to the User directory:

    :::bash
    sublimedir=~/.config/sublime-text-3/Packages/User

and at the end of the file the lines taking care of the magic:

    :::bash
    # move any existing dotfiles in homedir to dotfiles_old directory, then create symlinks
    for file in $files; do
        if [ -a ~/.$file ]; then    # check if a dotfile already exists
            echo "Moving any existing dotfiles from ~ to $olddir"
            mv ~/.$file $olddir
        fi
        echo "Creating symlink to $file in home directory."
        ln -s $dir/$file ~/.$file
    done

    echo "...done"

    # Create symlink for Sublime Text User directory
    if [ -d $sublimedir ]; then # check whether the directory already exists

        if [ -L $sublimedir ]; then
            echo "Removing old symlink"
            rm $sublimedir
            echo "...done"
        else
            echo "Moving the existing Sublime Text Users directory from $sublimedir to $olddir"
            mv $sublimedir $olddir
            echo "...done"
        fi
    fi
    echo "Creating symlink to User in $sublimedir"
    ln -s $dir/sublime/User $sublimedir
    echo "...done"

The full script can be found on [github](https://github.com/Railslide/dotfiles/blob/master/installdotfiles.sh).

Finally, since Package Control updates regularly some of the files in the User folder, I added them to a `.gitignore` file in order to avoid to much noise in my version control. A list of those files can be found in the [docs](https://sublime.wbond.net/docs/syncing) of Package Control.
