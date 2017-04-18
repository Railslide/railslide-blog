Title: How to create a GPG key with subkeys
Date: 2017-04-19
Category: Cryptography
Tags: GPG, cryptography, howto
Slug: create-gpg-key-with-subkeys
Author: Giulia Vergottini
Summary: A step to step guide for creating a GPG key with subkeys.
Status: draft

I wanted to create a GPG key - so far so good. The problem is that I also wanted to use GPG on multiple devices, ideally even on my phone. I could have - _in theory_ - copied the key over to all the needed machines, but that would have been a terrible ide. What if I lose my phone/laptop? My key would be compromised and I'd be left with no other choice than revoking it and losing all the previous signatures.

That's when subkeys come in.

Subkeys are almost identical to normal key pairs, except they can't be used for signing other people's keys, they're bound to a master key pair, and - here comes the interesting part! - they can be revoked independently from the master key.

So, in practical terms, they allow me to do the following: create a master key pair, create a subkey pair, remove the master key from my laptop, store it in a safe place, move on with my encrypting/decrypting life as usual. If catastrophe strikes, I retrieve my master key from its safe place, revoke the subkey, create a new subkey pair and I'm ready to go - and since each link of the Web of Trust is connected to the UID of the master key, my reputation stays untouched.

The only problem with all this workflow is that it requires a bunch of steps and I have the tendency to forget them pretty quickly. So, for the sake of my future self (or anyone else who might found them useful) here it is the whole process.

Set GPG to prefer SHA2
----------------------

GPG defaults to SHA1 as preferred hash, so let's set it to prefer SHA2 instead.
Check if the following lines are present in `~/.gnupg/gpg.conf`:

    personal-digest-preferences SHA512 SHA384 SHA256 SHA224
    default-preference-list SHA512 SHA384 SHA256 SHA224 AES256 AES192 AES CAST5 BZIP2 ZLIB ZIP Uncompressed
    cert-digest-algo SHA512

If not, add them.

Create a master key
-------------------

Create the master key - I'm going to mark user inputs with `# [input value] <--`.

    :::bash
    $ gpg --gen-key
    gpg (GnuPG) 1.4.11; Copyright (C) 2010 Free Software Foundation, Inc.
    This is free software: you are free to change and  redistribute it.
    There is NO WARRANTY, to the extent permitted by law.

    Please select what kind of key you want:
        (1) RSA and RSA (default)
        (2) DSA and Elgamal
        (3) DSA (sign only)
        (4) RSA (sign only)
        Your selection? # 1 <--

When it comes to choosing the length make sure to choose the longest available option (4096 at the time of writing).

    :::bash
    RSA keys may be between 1024 and 4096 bits long.
    What keysize do you want? (2048)  # 4096 <-- (the longer the better!)

    Requested keysize is 4096 bits
    Please specify how long the key should be valid.
        0 = key does not expire
        <n>  = key expires in n days
        <n>w = key expires in n weeks
        <n>m = key expires in n months
        <n>y = key expires in n years
    Key is valid for? (0) # 0 <--

    Key does not expire at all
    Is this correct? (y/N) # y <--

    You need a user ID to identify your key; the software constructs the user ID
    from the Real Name, Comment and E-mail Address in this form:
        "Heinrich Heine (Der Dichter) <heinrichh@duesseldorf.de>"

    Real name: # [Your name] <--

    E-mail address: # [Your email address] <--

    Comment:
    You selected this USER-ID:
        "[Your name] <[your email address]>"

    Change (N)ame, (C)omment, (E)-mail or (O)kay/(Q)uit? # o <--

When prompted for a passphrase, make sure to choose a strong one - ideally long and hard to guess. If someone gets access to the secret key, the passphrase would be the only thing left to prevent them from using it.

    :::bash
    You need a Passphrase to protect your secret key.
    # Enter passphrase <--

    We need to generate a lot of random bytes. It is a good idea to perform
    some other action (type on the keyboard, move the mouse, utilize the
    disks) during the prime generation; this gives the random number
    generator a better chance to gain enough entropy.
    .............+++++
    ..+++++

    gpg: key [your key ID] marked as ultimately trusted
    public and secret key created and signed.

    gpg: checking the trustdb
    gpg: 3 marginal(s) needed, 1 complete(s) needed, PGP trust model
    gpg: depth: 0  valid:   1  signed:   0  trust: 0-, 0q, 0n, 0m, 0f, 1u
    pub   4096R/[your key ID] 2017-04-17
          Key fingerprint = [Key fingerprint]
    uid                  [Your name] <[your email address]>
    sub   4096R/[Sub ID] 2017-04-17

Congratulations! The master key has been created!


Set your key to prefer strong hashes
------------------------------------

In theory, if hash preferences were set in the `gpg.conf` file before creating the key, this step should not be necessary. But better safe than sorry.

    :::bash
    $ gpg --edit-key [your email address]
    gpg (GnuPG) 1.4.11; Copyright (C) 2010 Free Software Foundation, Inc.
    This is free software: you are free to change and redistribute it.
    There is NO WARRANTY, to the extent permitted by law.

    Secret key is available.

    gpg: checking the trustdb
    gpg: 3 marginal(s) needed, 1 complete(s) needed, PGP trust model
    gpg: depth: 0  valid:   1  signed:   0  trust: 0-, 0q, 0n, 0m, 0f, 1u
    pub  4096R/[Your key ID]  created: 2017-04-17  expires: never       usage: SC
                         trust: ultimate      validity: ultimate
    sub  4096R/[Sub ID]  created: 2017-04-17  expires: never       usage: E

    gpg> # setpref SHA512 SHA384 SHA256 SHA224 AES256 AES192 AES CAST5 ZLIB BZIP2 ZIP Uncompressed <--

    Set preference list to:
         Cypher: AES256, AES192, AES, CAST5, 3DES
         Digest: SHA512, SHA384, SHA256, SHA224, SHA1
         Compression: ZLIB, BZIP2, ZIP, Uncompressed
         Features: MDC, Keyserver no-modify
    Really update the preferences? (y/N) # y <--


    You need a passphrase to unlock the secret key for
    user: [Your name] <[your email address]>
    4096-bit RSA key, ID [You key ID], created 2017-04-17

    # Enter passphrase <--

    pub  4096R/[Your key ID]  created: 2017-04-17  expires: never       usage: SC
                         trust: ultimate      validity: ultimate
    sub  4096R/[Sub ID]  created: 2017-04-17  expires: never       usage: E   ]

    gpg> # save


Create a signing subkey
-----------------------

When creating a key GPG automatically creates an encryption subkey as well, which means that only the signing subkey needs manual creation.

    :::bash
    $ gpg --edit-key [Your email address]
    gpg (GnuPG) 1.4.11; Copyright (C) 2010 Free Software Foundation, Inc.
    This is free software: you are free to change and redistribute it.
    There is NO WARRANTY, to the extent permitted by law.

    Secret key is available.

    gpg: checking the trustdb
    gpg: 3 marginal(s) needed, 1 complete(s) needed, PGP trust model
    gpg: depth: 0  valid:   1  signed:   0  trust: 0-, 0q, 0n, 0m, 0f, 1u
    pub  4096R/[Your key ID]  created: 2017-04-17  expires: never       usage: SC
                             trust: ultimate      validity: ultimate
    sub  4096R/[Sub ID]  created: 2017-04-17  expires: never       usage: E   ]

    gpg> # addkey <--

    Key is protected.

    You need a passphrase to unlock the secret key for
    user: [Your name] <[your email address]>
    4096-bit RSA key, ID [Your key ID], created 2017-04-17
    # Enter passphrase <--

    Please select what kind of key you want:
        (3) DSA (sign only)
        (4) RSA (sign only)
        (5) Elgamal (encrypt only)
        (6) RSA (encrypt only)
    Your selection? # 4 <--

    RSA keys may be between 1024 and 4096 bits long.
    What keysize do you want? (2048) # 4096 <-- (the longer the better!)

    Requested keysize is 4096 bits
    Please specify how long the key should be valid.
        0 = key does not expire
        <n>  = key expires in n days
        <n>w = key expires in n weeks
        <n>m = key expires in n months
        <n>y = key expires in n years
    Key is valid for? (0) # 0 <--

    Key does not expire at all
    Is this correct? (y/N) # y <--

    Really create? (y/N) # y <--


    pub  4096R/[Your key ID]  created: 2017-04-17  expires: never       usage: SC
                             trust: ultimate      validity: ultimate
    sub  4096R/[Sub ID]  created: 2017-04-17  expires: never       usage: E   ]
    sub  4096R/[Sub ID]  created: 2017-04-17  expires: never       usage: S

    gpg> # save <--


Create a revocation certificate
-------------------------------

If the master key gets lost or compromised, the revocation certificate is going to be your emergency brake.

    :::bash
    $ gpg --output revoke.asc --gen-revoke [your email address]
    Create a revocation certificate for this key? (y/N) # y <--
    Please select the reason for the revocation:
      0 = No reason specified
      1 = Key has been compromised
      2 = Key is superseded
      3 = Key is no longer used
      Q = Cancel
    (Probably you want to select 1 here)
    Your decision? # 1 <--
    Enter an optional description; end it with an empty line:
    > # Empty line will do fine here <--
    Reason for revocation: Key has been compromised
    (No description given)
    Is this okay? (y/N) # y <--

    You need a passphrase to unlock the secret key for
    user: [Your name] <[your email address]>
    4096-bit RSA key, ID [Your key ID], created 2017-04-17
    # Enter passphrase <--

    Revocation certificate created.

Make several copies of it and save it in a safe place (ideally not the same one as the master key!)

Remove the master key
---------------------

Before proceeding, make sure to have backups of the `.gpg` folder (perhaps on an encrypted media)

Temporarily export the subkeys:

    :::bash
    $ gpg --export-secret-subkeys [your email address] > /media/encrypted-media/subkeys

Delete the master key:

    ::: bash
    $ gpg --delete-secret-key 0x6F87F32E2234961E

Re-import the subkeys and remove the temporary export:

    :::bash
    $ gpg --import /media/encrypted-usb/subkeys
    $ shred -u /media/encrypted-usb/subkeys

Check that everything worked as intended - the hash (#) next to the `sec` line means that the master key is missing.

    :::bash
    $ gpg -K [your email address]

    /home/username/.gnupg/secring.gpg
    -----------------------------
    sec#  4096R/[Your key ID] 2017-04-17
    uid                  [Your name] <[your email address]>
    ssb   4096R/[Subkey ID]   2017-04-17
    ssb   4096R/[Subkey ID]   2017-04-17


Upload the key to a keyserver
-----------------------------

Keyservers forward keys to each other, so any keyserver would do.

    :::bash
    $ gpg --keyserver pgp.mit.edu --send-key [your key ID]


Using your master key
---------------------

Assuming that the `.gpg` folder is on some kind of encrypted media:

    :::bash
    $ gpg --home=/media/encrypted-media/.gnupg/ [gpg command]


Parting thoughts
----------------

That's it!

There is probably a lot more to say, but this seems quite enough stuff to read already. Below there's a list of links for further reading/source of inspiration.




### Resources
* [OpenPGP Best Practices](https://riseup.net/en/security/message-security/openpgp/best-practices)
* [The GNU Privacy handbook](https://www.gnupg.org/gph/en/manual/book1.html)
* [Subkeys - Debian wiki](https://wiki.debian.org/Subkeys?action=show&redirect=subkeys)
* [HOWTO prep for migration off of SHA-1 in OpenPGP](https://debian-administration.org/users/dkg/weblog/48)
* [Creating a new GPG key with subkeys](https://www.void.gr/kargig/blog/2013/12/02/creating-a-new-gpg-key-with-subkeys/)
* [Creating the perfect GPG keypair](https://alexcabal.com/creating-the-perfect-gpg-keypair/)
* [Creating a new GPG key](http://ekaia.org/blog/2009/05/10/creating-new-gpgkey/)
* [GPG Quickstart](http://blog.clusterlabs.org/blog/2013/gpg-quickstart)
* [Generating More Secure GPG Keys: A Step-by-Step Guide](https://spin.atomicobject.com/2013/11/24/secure-gpg-keys-guide/)
