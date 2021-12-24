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

Besides not being a not-so-great user experience, Snap packages also come with some ethical concerns. Ideally if I don't like them I could just stay away from them, right? Unfortunately that's easier said than done. Since Ubuntu 20.04 installing Chromium via Apt will install Chromium as a Snap package instead of a native one. [The reason for this change was that the native package required developers to build releases for every supported version Ubuntu, while Snap allows them to maintain a single package that works on all of them](https://snapcraft.io/blog/chromium-in-ubuntu-deb-to-snap-transition). The problem though is that this switcharoo happens without warning or asking the user. Don't get me wrong, as a developer myself I understand that maintaining Chromium might have been a gigantic pain in the ass, but I also believe that simply printing out a notice rather than go ahead and install a snap package would have gone a long way.

On a similar note, I was also surprised to discover that Ubuntu Disk Creator doesn't support ISO images for anything other than Ubuntu and its flavours. I am aware that this is old news, but I still found it fairly irritating, since it felt a bit like being punished (_no GUI for you!_) for going for a different distro. Also, the fact that the official Ubuntu guide suggested two ppa as alternatives was not super encouraging either. And while this wasn't a deal breaker per se, it added up to my frustration. So, when the opportunity came along in the form of a new work laptop, I decided it was time to explore the distro landscape.

## Enter Manjaro

Manjaro is a user-friendly distro based on Arch, which means rolling releases and access to the Arch User Repository (AUR).

### The good parts

1. It's fast.
2. Extensive community support
3. It natively supports Flatpak, Snap, Aur packages - it's only a matter of toggling a setting in the package manager
4. It looks good

## The bad parts

While in general I really liked Manjaro, it would be a lie to say that it is free from flaws.

My major complain about it are its disk encryption settings. By default if you decide to encrypt your disk, Manjaro will encrypt everything including the boot partition.
