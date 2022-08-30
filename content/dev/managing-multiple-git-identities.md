Title: Managing multiple Git identities
Date: 2022-08-30
Tags: git
Slug: managing-multiple-git-identities
Summary: How to manage multiple Git identities on the same machine

I code for work and I code for fun. When I do it for fun I use my personal email address as identity in Git, but when I do it for work I am often required to use my work email. For a long time my solution was to simply to set my working email in the `.gitconfig` of my working machine. That worked for most cases (I usually tend to only code for work on my work machine) and as the only pain point seemed to be my dotfiles, I simply accepted the pain of copy-pasting things around as a necessary evil and moved on with my life.

However, it turns out that there's a better way to handle multiple identities in Git: enter conditional configuration! Basically you can tell Git to include a different `.gitconfig` depending on a certain condition (e.g. when the `.git` directory matches a certain path). So for my specific case I simply changed my `.gitconfig ` to like something like this:

```
[user]
    name = <first name> <last name>
    email = <work email address>
[includeIf "gitdir:~/Projects/personal/"]
    path = .gitconfig-personal
```

and then in the `.gitconfig-personal` I added

```
[user]
    name = <first name> <last name>
    email = <personal email address>
```

and now every time I work on a repo in the `personal/` folder the work `[user]` block gets automagically overridden by the personal one. No more weird copy pasting around! 

### Gotchas

- This requires Git 2.13+ to work.
- The last slash of the `gitdir` path matters! If you forget it, it won't work.
- `../` gets matched literally, so don't use that if you want to refer to the parent folder.

### References
- [Conditional configuration in Git docs](https://git-scm.com/docs/git-config#_conditional_includes)
