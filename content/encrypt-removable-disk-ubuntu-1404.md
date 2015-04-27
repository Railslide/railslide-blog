Title: How to encrypt a removable disk in Ubuntu 14.04
Date: 2015-04-27
Category: Ubuntu
Tags: ubuntu, encryption, howto
Slug: encrypt-removable-disk-ubuntu-1404
Author: Giulia Vergottini
Summary: Most of the guides (including the official ones) on how to encrypt a removable disk in Ubuntu still refer to Ubuntu 12.04. Here's how to do it in Ubuntu 14.04 and to cope with the changes it introduces to the disks manager tool.
Status: draft

The other day I wanted to encrypt a USB stick, but to my dismay I discovered that all the available howtos (including the community wiki) refers to Ubuntu 12.04. Ubuntu 14.04 introuced some changes to the disks manager tool, which - even

1. Install cryptsetup
---------------------

The first thing you need to do is to install `cryptsetup`:

    :::bash
    sudo apt-get install cryptsetup

You can also install it from the Software center if you feel more comfortable with a graphical interface.


2. Disks manager
----------------

Launch the disk manager via __Dash > Disks__ and select the volume you wish to encrypt.

> A word of warning
> If you have any data on your USB, you probably want to back them up. The encryption process requires will format the volume, so any previously stored data will be wiped off.
