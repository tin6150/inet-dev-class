.. figure:: xkcd_usb_cables.png
    :align: center
    :alt: https://www.explainxkcd.com/wiki/index.php/1892:_USB_Cables

    `s/usb cables/config management/ :) <https://www.explainxkcd.com/wiki/index.php/1892:_USB_Cables>`_



Playing with Ansible
********************


/etc/ansible/hosts  = default inventory.ini file for defining host group.  
all = all hosts in inventory.ini file


adhoc::

    ansible all -i inventory.ini -m ping -u root
    ansible all --inventory-file=inventory.ini --module-name ping -u vagrant --private-key=~/.vagrant.d/insecure_private_key


    ansible all -i inventory.ini -m command -u root --args "uptime"
    ansible all -i inventory.ini -u root -a "uptime"

    ansible all -i inventory.ini -m apt -u vagrant -a "name=zsh state=installed -s"
    # -s sudo 
    # -K, --ask-sudo-pass

    ansible localhost -m setup              # display discoverd facts

    ansible-doc -l          # list docs
    ansible-doc git         # doc on the git module

execute playbook::

    ansible-playbook myplaybook.yml -i inventory.ini -u root



ref
---

* https://ryaneschinger.com/blog/ansible-quick-start/                                       [read]
* http://people.redhat.com/mskinner/rhug/q2.2017/Ansible-Hands-on-Introduction.pdf p23      [read]
* https://www.vagrantup.com/docs/provisioning/ansible_intro.html

* http://galaxy.ansible.com - Find pre-built playbook roles from the community.



Installing Ansible
------------------

mac::

    sudo /usr/bin/easy_install pip 
    sudo pip install ansible

centos 7::

    sudo pip install ansible


Mint 17.2::

    sudo apt-get install ansible	# 1.5.4+dfsg-1  ... very old, don't understand "become"
    sudo apt-get remove  ansible
    sudo pip install --upgrade setuptools
    sudo pip install --upgrade ansible	# 2.4.1.0
    sudo apt-get install python
    sudo apt-get autoremove				# clear out python-jinja2 python-yaml

    arggg... backbox / ubuntu notes not pushed...   but I think same versions as mint 17.2

Vagrant container setup using Ansible playbook
----------------------------------------------

For vagrant to provision VM with ansible playbook, the vagrant host must have ansible installed.
A bit more details in https://www.vagrantup.com/docs/provisioning/ansible.html


* vagrantfile_playbook.yml 
  eg of this in singhub, vagrant provision to call this play
* https://www.digitalocean.com/community/tutorials/configuration-management-101-writing-ansible-playbooks 
  at the end has eg for playbook.yml for Vagrant, but eg for ubuntu or Debian
* http://people.redhat.com/mskinner/rhug/q2.2017/Ansible-Hands-on-Introduction.pdf p23 has rhel7 eg
* https://www.vagrantup.com/docs/provisioning/ansible_intro.html


example ansible playbook yaml 
-----------------------------

::

        tba, but naming like follwing probably work
        workstn_mint17.yaml
        workstn_sl7.yaml
        webserver.yaml
        node_sl7.yaml
        node_sl6.yaml



One example approach at config
******************************


inventory
---------

::

    [servers]
    svr1
    svr2

    [workstations]
    ubuntu1
    ubuntu2
    centos1
    centos2


Roles
-----

Use roles to more narrowly group machines.   they can be bundled for "install" into specific host.
eg:    

::

    common
    apache
    mysql
    login_otp
    login_local_passwd


OS Platform Specific Issue
--------------------------

Handling tasks that are OS platform specific is a thorny issue.  There is really no good/general solution for this.  
The way how Ansible YAML files define workflow, named tasks use a `when: ansible_os_family == "Debian"` or `== "RedHat"` etc to handle the task.
As such, say, running a command and grepping output that is platform specific, the "default" way is to split them in to multiple tasks, one for each platform that need to handle the command in one way.  

There are ways to include different yaml file depending on the OS platform using variables.  see:

1. https://stackoverflow.com/questions/26226609/ansible-conditional-user-based-on-platform
2. http://docs.ansible.com/ansible/latest/playbooks_best_practices.html#operating-system-and-distribution-variance

But there are many tasks that maybe commont amont all platform.  and splitting 
YAML file at the highest level for each OS platform may cause logic code to be repeated.  Cut-n-paste is easy, but having to update/maintain the same logic in multiple files is error prone.

Thus, this will likely be the black art part of how to split ansible YAML files.

Have some high level Roles-based separation for server vs workstaion, or to separate between say web servers vs db servers.

But while coding the logic for the role, things that are obviously platform specific should be grouped together, and either have a block that eveluate the OS family to group these tasks or split into differe file.

Point is, try to keep the logic in one place, then group the OS family code together as much as possible while doing one logical task.  

Don't be running every logic and duplicating the named task for each os family where possible.

eg: see https://github.com/tin6150/singhub/blob/master/virtualbox-guest/tasks/main.yml

Overall, this is tedious if not painful.  Having IF or CASE would be nice.
YAML is a PITA anyway.


Package is a platform independent module that can install packages.  It will work when the package name is the same between the platforms.  
But no easy way to define package name variability (eg linux-headers vs kernel-headers).  
There are things that need to be defined for yum vs apt-get, eg cache, EPEL repo, etc.  those are not handled by Package.


pros and cons, check points to keep in mind:

- tasks to check what OS it is would provide basic sanity check that task is running in desired env, and more sane error message when applied incorrectly
- Each OS platform to have its own play avoid needing constant "block ... when platform==rhel"  and then another block for deb.
- If change name/ip of say Radius Server, or NTP server, change one task file vs change 2+ task file?
    


TMP note
********

for dev on linux, 
maybe copy Vagrantfile here.
then it can be customized to have multiple hosts, which req more convoluted setup.

(but for now, on c7, have continued to use the Vagrantfile on singhub).

rst cheatsheet https://github.com/ralsina/rst-cheatsheet/blob/master/rst-cheatsheet.rst



GitHub rst parser notes
-----------------------

indent of block above with === header trip github parser.

dotdot comment block are NOT liked by github -- maybe trips the parser, maybe just not render them as comment.
not even when as footnote notation (cuz lacked ref?)  just avoid them for github rst parsing.


~~~~


:url: https://github.com/tin6150/inet-dev-class/tree/master/ansible
:author: tin6150
:version: 2017-1021

