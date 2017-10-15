
==========
|TMP note|
==========

for dev on linux, 
maybe copy Vagrantfile here.
then it can be customized to have multiple hosts, which req more convoluted setup.

(but for now, on c7, have continued to use the Vagrantfile on singhub).



Playing with Ansible
====================


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



ref:
https://ryaneschinger.com/blog/ansible-quick-start/
http://people.redhat.com/mskinner/rhug/q2.2017/Ansible-Hands-on-Introduction.pdf p23
https://www.vagrantup.com/docs/provisioning/ansible_intro.html


http://galaxy.ansible.com
Find pre-built playbook roles from the community.



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

https://www.vagrantup.com/docs/provisioning/ansible.html

vagrantfile_play.yml	# eg of this in singhub, vagrant provision to call this play
	# https://www.digitalocean.com/community/tutorials/configuration-management-101-writing-ansible-playbooks 
	# at the end has eg for playbook.yml for Vagrant, but eg for ubuntu or Debian

# http://people.redhat.com/mskinner/rhug/q2.2017/Ansible-Hands-on-Introduction.pdf p23
# https://www.vagrantup.com/docs/provisioning/ansible_intro.html



example ansible playbook yaml 
-----------------------------



tba, but naming like follwing probably work
workstn_mint17.yaml
workstn_sl7.yaml
webserver.yaml
node_sl7.yaml
node_sl6.yaml
