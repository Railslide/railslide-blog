Title: How to encrypt a removable disk in Ubuntu 14.04
Date: 2015-04-27
Category: Cryptography
Tags: ubuntu, encryption, howto
Slug: encrypt-removable-disk-ubuntu-1404
Author: Giulia Vergottini
Summary: Most of the guides on how to encrypt a removable disk in Ubuntu still refer to Ubuntu 12.04. Here's how to do it in Ubuntu 14.04 and to cope with the changes it introduces to the disks manager tool.

The other day, while encrypting a USB stick, I discovered that most of the available howtos (including the community wiki) refers to Ubuntu 12.04. So, here's how to do it in Ubuntu 14.04, taking into account the changes that the latest LTS introduced to the disks manager tool.

1. Install cryptsetup
---------------------

The first thing you need to do is to install `cryptsetup`:

    :::bash
    sudo apt-get install cryptsetup

You can also install it from the Software center if you feel more comfortable with a graphical interface.


2. Disks manager
----------------

Launch the disk manager via _Dash > Disks_ and select the volume you wish to encrypt.

_**WARNING: The encryption process will format the volume, so any previously stored data will be wiped off.**_

In other words,

* If you have any data on your USB, you probably want to back them up.
* Make sure to select the rigth volume to encrypt, otherwise you could accidentally wipe your hard disk off.

Select the partition, click on the gear icon under it, and choose `Format`. Select `Overwrite existing data with zeroes (slow)` and `Encrypted, compatible with Linux systems (LUKS + ext4)` as type.

Then insert the passphrase, confirm it, and wait until the process it's complete. Click on the lockpad icon (i.e. to close it) and you're ready to go.

Troubleshooting
---------------

* You need to have `cryptsetup` installed in order to get `LUKS + ext4` option showing up in the list of available system format.

* If you had the disk manager already open while installing `cryptsetup`, you have to restart it in order to see the `LUKS + ext4` option.
