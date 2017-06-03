Title: How to sign PGP keys with an offline master key
Date: 2017-06-03
Tags: GPG, cryptography, howto
Slug: how-to-sign-pgp-keys-with-offline-master-key
Author: Giulia Vergottini
Summary: Signing other people keys with an offline master key is not super straightforward. Here's how to do it in an almost pain-free way.

Lately I wanted to sign a coworker's key, so after having gone through the all in-real-life verification shebang together, all that was left was me performing the actual signing. However, since I [use subkeys on my laptop]({filename}./create-gpg-key-with-subkeys.md), I first needed to get out my master key from its secret dungeon and tell GPG to use that one instead of the usual subkey. For doing that I used the handy `--homedir` option.

    $ gpg --homedir=/path/to/my/master/gnupg/folder --sign-key mycoworker@myjob.com
    gpg: key "mycoworker@myjob.com" not found: public key not found

How's that possible? I am positive that I've imported my coworker's key - we have even exchanged encrypted email with each other!

Well, the fact is that I imported the key, yes, but I did it in my local keyring which is the one located at `~/.gnupg` and thus not the one my master key refers to. Pretty much as when using GPG on multiple computers: you have to re-import all the public keys from scratch.

Ok, so what are the options? Export the key I want to sign, import it into the master keyring, sign it, export it from the master keyiring, and finally import it into the local keyring? Sure, you could do that, but it's quite cumbersome. Fortunately, gpg has a better solution for that: the `--keyring` option!

    $ gpg --homedir=/path/to/my/master/gnupg/folder --keyring ~/.gnupg/pubring.gpg --sign-key mycoworker@myjob.com

And voilà! Now you can proceed signing the key.
