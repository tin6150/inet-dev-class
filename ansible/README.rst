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


Whether to do a play for specific OS platform 
or have each task evaluate which platform it is and run yum vs apt (etc) depends on how
ansible modules does things.

pros and cons:

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

