Title: Managing virtual machines with Qemu
Date: 2024-10-30
Tags: virtual-machines, virtualization, qemu, gnome-boxes, virt-manager
Summary: A while ago I switched from Virtualbox to Qemu for virtual machines management. Here are my notes on how to set it up and all the gotchas I stumbled upon while doing it.



A while ago I switched from Virtualbox to Qemu for virtual machines management. Here are my notes on how to set it up and all the gotchas I stumbled upon while doing it.

## Step 0: check if you can run it

First thing first, it might be a good idea to verify that your system supports this kind of virtualization. A quick way to verify is to run

```bash
grep -Ec '(vmx|svm)' /proc/cpuinfo
```

and check if the output is greater than zero.

## Gnome-boxes, aka my go-to solution

When I first started playing around with Qemu I went for the manual installation (more on that below). Then I discovered gnome-boxes and never looked back. Gnome-boxes basically has everything I need for 99% of my user cases: it is simple stupid to create and manage VMs through it, it automatically resizes the guest screen to fit the host window, transferring files to the VM is super straightforward and it doesn't require you to actually drag-and-drop things.

Gnome-boxes also allows to download ISO files directly through it. Besides being a nice time-saver (i.e. no more need of switch to browser, download the ISO, import the ISO, etc.), it will also automagically set up copy-paste and file transfer for you!

Ok, so gnome-boxes sounds great - are there any cons to it? Well, while not dealbreakers, there are definitely a couple of gotchas. First of all, the ISO download function doesn't support all the distros (e.g. Kali cannot be downloaded through it). So if you need one of those, just be aware that - besides getting the ISO file yourself - you'll also have to take care of enabling copy-paste and file transfer on the VM (see below for how to do it).

Also, while simplicity is definitely one of the strenghts of gnome-boxes, there are cases where you might need more granular control over the settings of your VM. A good example for it is if you are trying to use a distro using Sway as desktop enviroment: default graphical settings don't work in Sway and gnome-boxes doesn't offer a workaround for it. So if you want to run a Sway-based machine, you'll have to install virt-manager and adjust the settings from there (again, see below for how to do it).

## Manually enable copy-paste & file transfer

If the distro you wanted was not in gnome-boxes OS list, you'll need to manually enable up copy-paste and file transfers. To do so, install `spice-vdagent` on the guest system. Reboot the VM after installing it and you are good to go.

## Installing Qemu manually

If gnome-boxes is not your thing, you can install Qemu manually. The dark side of it is that the package has different names in different distros (e.g. on Arch it's called `qemu-full`, on Ubuntu Jammy is `qemu-kvm`, while in newer Ubuntu version is called `qemu-system`. So arm yourself of Google, find what's the package is called in your distro and install it with your favorite package manager.

After that, you'll likely want to install `virt-manager` as Qemu doesn't come with a GUI by default.

## Installing virt-manager

First, install the `virt-manager` package (which thankfully maintains the same name across distros!) using your distro's package manager.

In order for `virt-manager` to work, your user needs to have access to the `libvirtd` daemon and the easiest way to achieve that is to add yourself to the `libvirt` user group

```bash
sudo usermod -aG libvirt $USER
```

Next start and enable the `libvirt` daemon

```bash
$ systemctl start libvirtd
$ systemctl enable libvirtd
```

Launch `virt-manager` and if it succesfully connects to Qemu/KVM (you might need to double click on it), you are good to go!

## VM Gotchas and troubleshooting

Creating VMs is pretty straightforward as both gnome-boxes and virt-manager interfaces are extremely intuitive. Tweaking the machines might be a bit more fiddly though, so here's a list of tips and tricks that might come in handy.

### Sway

Sway on Qemu comes with its own specific weird behaviors/bugs.

In order to prevent the screen from constantly flickering, you will have to manage the VM through virt-manager and change its video settings before installing it. To do so, select the checkbox for customizing configuration (if you forget, you can still reach those settings from Edit -> Preferences on the guest menu), then select `Video Virtio` and change the model from `Virtio` to `VGA` to avoid any graphical glitch.

Copy-paste and drag-and-drop don't work in Sway. For copy-paste, you can use [`xsel` as a workaround](https://www.reddit.com/r/swaywm/comments/pg0rqi/clipboard_sharing_using_spicevdagent_not_working/), while for drag-and-drop I have yet to find one.

### Scaling and resolution on virt-manager

After launching the VM, in the guest menu select View -> Scale display -> Always. Select the "Autoresize VM with window" checkbox as well.

Or even better, you set scaling on all the machines by default by going to Edit -> Preferences -> Console in the host menu.

Just note that after that you might still need to play around resolution from inside the VM os.

## References

- [Gnome-boxes](https://apps.gnome.org/Boxes/)
- [Qemu](https://www.qemu.org/)
- [Virt-manager](https://virt-manager.org/)
