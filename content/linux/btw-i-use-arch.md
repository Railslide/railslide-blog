Title: Oh btw, I use Arch
Date: 2022-01-13
Tags: os, linux, distro, arch
Slug: oh-btw-i-use-arch
Summary: Somehow I ended up on Arch and so far I'm liking it.
Status: draft

I was happily running Manjaro when my computer started to crash multiple times per day. I tried debugging but that did not lead anywhere (it will later turn out to be a hardware issue). So, out of ideas I decided to see if the problem was somehow Manjaro specific and if another distro would solve it. And it was at that point that a friend somehow convinced me to give Arch a shot.

My approach to Arch
-------------------

The main reason why I've never considered Arch before it was probably that I had the misfortune to run into some terrible Arch users in the past. You know, the _Ubuntu is for noobs, installing and running Arch is so complicated, I made it and hence I'm better than you_ kind of people. So in my mind Arch was pretty much an elitist overcomplicated distro and I didn't really see any good reason for giving it a shot.

What changed my mind then? Well, it has been a combination of things. On one hand - thanks to Manjaro - I got exposed to AUR (Arch User Repository) and grew fond of it. on April 1st Arch had released an installer (fun fact: due to the date many thought it was an April's fool) removing the need to install Arch from scratch. Plus, I was extremely frustrated by the frequent crashes and if Arch was the solution so be it.

On the other hand I realized that a bunch of awesome people in my life were in fact using Arch (I probably had run into nice Arch users even before, but since they didn't go around boosting how cool they were for using Arch I probably missed that). And since I'm not immune to peer reinforcement that definitely helped. Plus a part of me secretly regarded Arch as a sort of mandatory step/rite of passage in my linux journey, so when a friend suggested to give Arch a shot I just assumed that the time for it had come.

I must say, however, that even though I had bought in to the idea of installing Arch, my expectation was very much of giving it try, finding it too complicated/elitist, and moving to another distro. It turned out that I was very wrong.

Installing Arch
---------------

Thanks to the shiny new installer, the process of installing Arch was generally straightforward. The only part I didn't find very intuitive was accessing the wifi from TTY. Thankfully a friend had provided me with instructions, so that went smoothly as well. For the sake of my future self, here they are:

```
iwctl
stations list
stations <probably-wlan0-but-whatever-is-listed-in-list> connect <SSID>
```

The rest went through without too much hassle. A good idea was however to have another computer or a phone ready at hand, for those few times where I felt the need to google something during the process.

My first steps into the Arch world
----------------------------------

My first impression of Arch was that it was very... bare. Being used to distros with a bespoken desktop environment, I was a bit caught off guard when I first logged in. I had picked Gnome during the installation and what I got was indeed Gnome, just stripped to the bare minimum - anything else I wanted I had to install it myself. Don't get me wrong though, that is a good thing! Yes, I did have to figure out what was the name of the components I wanted and how to install them. But after a bit of fiddling I got my DE to work, look and feel exactly the way I wanted - and if that's not the beauty of linux in a nutshell, I don't what that is.

Another thing I noticed is the speed of my system. Compared to a fresh installation of Ubuntu, Arch is just blazing fast. I guess that's probably one of the perks on of not having a lot of useless software installed from the start. Again, yes, I had to install everything I need out of the box, but that also means my system resources are spent only on the programs I actually use.

Last but not least, I cannot really stress enough what an amazing documentation and community Arch has. The internet is full of people praising the Arch wiki and I totally agree - for 99% of the issues I encountered the solution was documented there. And the remaining 1% was usually covered by the [Arch Linux Forum on BBS](https://bbs.archlinux.org/).

Package management
------------------
