Title: Switching from Ubuntu to Manjaro
Date: 2021-12-26
Category: linux
Tags: os, linux, distro
Slug: switching-from-ubuntu-to-manjaro
Summary: After many years on Ubuntu I decided it was time for some distro hopping and I gave Manjaro a spin.

I've been an Ubuntu user for about 14 years and while I have been using other distros (mostly on servers) from time to time, I never felt the need to switch away from it. Lately though a mix of curiosity and some Ubuntu stuff rubbing my nerves gave me the nudge to try something else. I had heard good things about Manjaro, so I decided to give it a shot.

## What's wrong with Ubuntu?

Let's be clear, I don't hate Ubuntu. I still believe it's a great distro and definitely a great candidate for beginner and experienced users alike. That said, there were some things that annoyed me.

At the top of the list of my pain points there were Snap packages. When they were announced I thought it was a great idea. Containerized, cross-distribution applications - what's not to like? But while theory was great, practice turned out to be fairly mediocre: snap packages are slow, they clutter the filesystem, and they don't always work with your system theme. AppImage and Flatpak are way better alternatives and I would take them over Snap every given day.

Besides not being a not-so-great user experience, Snap packages also come with some ethical concerns. Ideally if I don't like them I could just stay away from them, right? Unfortunately that's easier said than done. Since Ubuntu 20.04 installing Chromium via Apt will install Chromium as a Snap package instead of a native one. [The reason for this change was that the native package required developers to build releases for every supported version Ubuntu, while Snap allows them to maintain a single package that works on all of them](https://snapcraft.io/blog/chromium-in-ubuntu-deb-to-snap-transition). The problem though is that this switcharoo happens without warning or asking the user. Don't get me wrong, as a developer myself I understand that maintaining Chromium might have been a gigantic pain in the ass, but I also believe that simply printing out a notice rather than go ahead and install a snap package would have gone a long way.

On a similar note, I was also surprised to discover that Ubuntu Disk Creator doesn't support ISO images for anything other than Ubuntu and its flavours. I am aware that this is old news, but I still found it fairly irritating, since it felt a bit like being punished (_no GUI for you!_) for going for a different distro. Also, the fact that the official Ubuntu guide suggested two ppa as alternatives was not super encouraging either. And while this wasn't a deal breaker per se, it added up to my frustration. So, when the opportunity came along in the form of a new work laptop, I decided it was time to explore the distro landscape.

## Enter Manjaro

Manjaro is a user-friendly distro based on Arch, which means rolling releases and access to the Arch User Repository (AUR). It also comes with its own dedicated software repositories, a graphical installer, automatic hardware detection, and pre-installed codecs.

### The good parts

Being based on Arch, Manjaro is fast and has a low memory footprint. Installation goes in a breeze (around 2 minutes!) and I was surprised on how little it took me to have it up and running. I later installed Ubuntu on the same machine and it felt like waiting for ages in comparison.

The next thing I really appreciated with Manjaro is that it gives the user a lot of freedom when it comes to customization. Take the desktop environment for example: the Manjaro development team provides and maintains XFCE, KDE and Gnome editions out of the box. On top of that, the community maintains 6 additional flavours (i3, Budgie, Cinnamon, Deepin, Mate, and Sway). So, whatever is favourite DE, you're likely to get it covered.

Another awesome feature is that Manjaro natively supports Flatpak, Snap, and Aur packages. Whatever you want to use it's up to you, all it takes is toggling a setting in the package manager. No more surprise Snap packages popping up in your system - if you want to use Snap you do, if you don't you don't.

I also loved the extensive community support. Besides the already mentioned community editions, Manjaro also has an extensive an lively forum where users can get help from other community members. This reminded me of Ask Ubuntu (definitely one of Ubuntu's strengths in my opinion!) and I was very pleased to see that Manjaro had something similar - in 99% of the cases I stumbled on some issue or had doubts, a quick search on there provided me with all the answers I needed.

Last but not least, Manjaro looks good. While aesthetic is not my primary concern when it comes to choosing an operative system, I must admit that I always found Ubuntu's default appearance somehow outdated and not very appealing. Again, not a breaking deal per se, but it was refreshing to work on something that pleased the eye without any further action on my side.

### The bad parts

While in general I really liked Manjaro, it would be a lie to say that it is free from flaws.

My major complain about it are its disk encryption settings. By default if you decide to encrypt your disk, Manjaro will encrypt everything including the boot partition. The good part is that an encrypted boot partition comes with the perk of not being vulnerable to an [evil maid attack](https://en.wikipedia.org/wiki/Evil_maid_attack). Though the bad part is that it comes with several drawbacks on your day-to-day activities, such as:

- Decryption is slow because it cannot leverage hardware acceleration and it can takes up to 20/30 seconds. So booting your computer takes time.
- You only have one try to type the decryption key correctly. If you make a typo, you'll have to reboot.
- The correct keyboard layout is not loaded yet, so if you're using special chars good luck with that.

A workaround for it is to do a manual partitioning and leave `/boot` unencrypted. However documentation and/or steps-by-steps instructions for how to do it are not easy to find, and even if you know how to do it you might still bump into some [installer bug](https://github.com/calamares/calamares/issues/1073) and end up with an unbootable system.

# Conclusion
In general I got a really nice impression of Manjaro and I definitely landed in my list of recommended distros.

Will I stay with it? Well, I ended up not to. Due to frequent crashes to my machine, I tried to install other distros to see if it was something related to Manjaro. While the problem turned out to be a hardware issue, the debugging process resulted in me stumbling on the above Calamares bug when trying to go back to Manjaro, getting frustrated, and eventually install something else (more on this in another post!). That said, I'd be more than willing to give Manjaro another chance in the future, once such bug gets fixed.

TL;DR: a great distro, with some encryption pain.
