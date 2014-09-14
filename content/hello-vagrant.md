Title: Hello Vagrant! (aka development environment made easy)
Date: 2014-09-14
Category: Utilities
Tags: vagrant, virtual machine, development environment
Slug: hello-vagrant
Author: Giulia Vergottini
Summary: If you don't use Vagrant yet, you should. Here's why.
Status: draft

For a long time my first step for starting a PHP based project has been to install Xampp on my machine. Xampp provides a considerably easy-to-install full lamp stack - no question about that. However, when I started working on more complicated projects which implied to work together with other developers issues started rising. The main problem was the differences between my local environment and the production one. Add the a further layer of differences for potentially each person involved in the project and it doesn't take much to figure out that moving the result of your work somewhere else than your machine was a guaranteed headache.

Now imagine a full LAMP stack that gets activated with a command as simple as `vagrant up` and takes automatically care of all the dependencies and needed libraries. Add on top of it that it's easily portable and tailored to your needs and you should already have enough reasons for giving Vagrant a try.

If you are still not fully convinced or just curios, here is a more detailed insight of how Vagrant increases productivity and makes your life so incredibly easier.

Exactly what you need
---------------------

Since you are the one provisioning your virtual machine, you get the total freedom of setting it up the way you want. This means that you can have a VM that perfectly replicates your production environment, removing thus all the potentially annoying discrepancies between your local system and the production one.


Setup only once
---------------

All you need for bringing up a VM with Vagrant is just the Vagrantfile and the provision script(s). Once you have those you are just a `vagrant up` away from that very machine every time you need it.

But the coolness doesn't stop here! If you commit the Vagrantfile and the provision scripts together with the rest of your projects files (and I don't see any good reason why you shouldn't), any developer checking out the code will be able to run the same VM on her/his computer.

This is particularly useful when working in a team, since *one person* set up the VM *just once* and a whole team benefits from it. Furthermore, thanks to CVS, if someone needs to install a library for carry out her/his job, s/he simply edits the provision file accordingly and commit it. In this way, everyone will get the needed library installed on the VM and so long forgotten dependencies.

Develop the way you like
-----------------------

Vagrant automatically syncs files between the host and the guest machine. So there's no need to change anything in your beloved setup nor to use something other than your favorite editor. Any file you edit locally in a synced folder will automagically appear in the VM as well, ready to be used.


Multiple machines? Not a problem!
---------------------------------

Vagrant allow you to have multiple VMs within the same project. They can communicate to each other, so that you can accurately reproduce the production environment of your multi-servers killer app. By the way, they are also independent from each other, so no need of bringing them all up when you need to work on only one.


Summing up
-----------

I guess it's pretty obvious that I am a huge fan of Vagrant. It makes my life so much easier (and my working team's too!) and I can no longer imagine my development workflow without it. Finally, the fact that it's also open source it's just the cherry on top.

* [Vagrant homepage](http://vagrantup.com/)
