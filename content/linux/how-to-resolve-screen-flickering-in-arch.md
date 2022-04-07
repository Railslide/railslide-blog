Title: How to resolve screen flickering in Arch
Date: 2022-04-07
Tags: linux, arch, intel, systemd-boot, troubleshooting
Slug: how-to-resolve-screen-flickering-in-arch
Summary: How to solve screen flickering in Arch when using Intel graphics and systemd-boot

After a system upgrade, I got this annoying screen flickering happening at random intervals. Initially I thought the issue was Gnome related, but after a bit of research it turned out to be caused by a [power saving feature on my Intel graphic card](https://wiki.archlinux.org/title/Intel_graphics#Screen_flickering).

The solution to it is to disable the feature through a kernel parameter. For doing so you need to edit a configuration file specific to the chosen boot loader. In my case it's systemd-boot, so the file was located in `/boot/loader/entries/[SOMETHING].conf` (in my case the filename was the timestamp of my system installation, but mileage may vary).

Open the file with your favourite editor
```
sudo nano /boot/loader/entries/[SOMETHING].conf
```

Add `i915.enable_psr=0` at the end of the `options` line.

Reboot, and enjoy your epilepsy-free screen time again.

Further readings
----------------

- [Arch wiki page about Intel graphics](https://wiki.archlinux.org/title/Intel_graphics)
- [Arch wiki page about kernel paremeters](https://wiki.archlinux.org/title/Kernel_parameters)
