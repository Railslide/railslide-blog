Title: Provisioning Vagrant with Ansible
Date: 2016-02-05
Tags: vagrant, ansible, automatization
Slug: provisioning-vagrant-with-ansible
Summary: Vagrant is an amazing tool. However, one thing that bugged me was that provisioning scripts preparation still required me a fair amount of time and trial-errors attempts. Switching to Ansible allowed me to make my life easier and provision times shorter.


When I started using Vagrant I picked bash as my provisioning tool. It looked as the most logical choice as I was already familiar with the command line. It served me well - I brought up a fair amount of virtual machines with it - but the process of getting the provision scripts still gave me some annoyances.

First of all, running a non-interactive installation adds an extra layer of complexity, since you don't always know (or think about) how an interactive command will behave in an unattended installation. For me that often translated itself into: run provision, get a more or less cryptic message, ssh into the machine, run the command manually, figure out what went wrong, edit the provision script, rinse, and repeat.

Then, the provision script runs from top to bottom every time a provision is run - no matter whether the machine has been already partially provisioned. You could throw in a bunch of conditional statements in order to skip the already performed steps, but that would come with the price of adding further complexity to the provisioning script.

Finally, you have to _echo all the things_ in order to keep track of the different installation steps - reducing thus the readability of the script.

Of course these are trivial problems and I've happily coped with them for quite some time. But then I had the chance to have a look at Ansible - and it has been a game changer!

Ansible uses yaml as a language for its orchestration files (aka playbook), which makes them extremely easy to read. For example, this is how a task for installing Git could look

    ::yaml
    - name: Install git
      sudo: yes
      apt: pkg=git state=latest

Pretty easy to figure out what it does! On top of that, Ansible outputs the name of your tasks when running them, making it trivial for you to keep track of what's going on behind the scenes.

Then there are modules, like `apt` in the example above, which are basically wrappers for the most common operations. There are lots of them, so there's a very high chance that you'll find a module for the command you need to run. And in case you don't, you can always use the shell module to run your command as you would type it in the terminal.

Besides making your life easier when it comes to write provision scripts, Ansible also makes the process of running them way faster. In fact, _idempotency_ is one of the key concept of Ansible modules, which basically means that they won't execute if their target state has already been reached. So, if you resume a partial provisioning, Ansible will skip all the previously performed tasks.

Last but not least, Ansible is written in Python which is a nice plus. Unfortunately it does not support Python 3, but I guess I'll have to live with it for the time being.

It is probably worthy mentioning that Ansible doesn't natively run on Windows. Fortunately the [Phansible team](http://phansible.com) came up with a workaround for it: using a shell provision to install Ansible on the guest and the run provision from there. It is a bit slower than running Ansible locally, but works great for projects with cross platforms contributors. Alternatively, I heard of people being able to run Ansible with cgywin, but I have no clues about what it takes to make it happen.

All in all, I would warmly recommend to give Ansible a try - especially if you are currently using bash for provisioning your vagrant machines. Here some links to get you started:

* [Ansible](https://www.ansible.com/)
* [Ansible docs](https://docs.ansible.com)
* [Vagrant docs - provisioning with Ansible](https://docs.vagrantup.com/v2/provisioning/ansible.html)

Happy provisioning!
