Title: Switching from Ubuntu to Manjaro
Date: 2021-12-20
Category: linux
Tags: os, linux, distro
Slug: switching-from-ubuntu-to-manjaro
Author: Giulia Vergottini
Summary: After many years on Ubuntu I decided it was time for some distro hopping and I gave Manjaro a spin.
Status: draft

I've been an Ubuntu user for about 14 years and while I have been using other distros (mostly on servers) from time to time, I never felt the need to switch away from it. Lately though a mix of curiosity and some Ubuntu stuff rubbing my nerves gave me the nudge to try something else. I had heard good things about Manjaro, so I decided to give it a shot.

## What's wrong with Ubuntu?

Let's be clear, I don't hate Ubuntu. I still believe it's a great distro and definitely a great candidate for beginner and experienced users alike. That said, there were some things that annoyed me.

At the top of the list of my pain points there were Snap packages. When they were announced I thought it was a great idea. Containerized, cross-distribution applications - what's not to like? But while theory was great, practice turned out to be fairly mediocre: snap packages are slow, they clutter the filesystem, and they don't always work with your system theme. AppImage and Flatpak are way better alternatives and I would take them over Snap every given day.

### Ubuntu/Canonical
I also

### Wanna try another distro? Sorry, no GUI for you

I wanted to try Manjaro without commitment before deciding whether to make the jump. However, when I tried to create a bootable usb stick, I discovered that Ubuntu Disk Creator doesn't support ISO images for anything other than Ubuntu and its flavours. I am aware that this is old news, but I still found it very irritating nonetheless. And while I know that there are alternatives, netbootin is a ppa and `dd` (which I ended up using) is not exactly user friendly.

All in all I felt like Canonical/Ubuntu was taking a bit too many decisions on my behalf. So, when the opportunity came along in the form of a new work laptop, I decided it was time to explore the distro landscape.

## Enter Manjaro

Manjaro is a user-friendly distro based on Arch, which means rolling releases and

### The good parts


1. It's fast.
2. Extensive community support
3. It natively supports Flatpak, Snap, Aur packages - it's only a matter of toggling a setting in the package manager
4. It looks good

## The bad parts

While in general I really liked Manjaro, it would be a lie to say that it is free from flaws.

My major complain about it is its disk encryption settings. By default if you decide to encrypt your disk, Manjaro will encrypt everything including the boot partition.
