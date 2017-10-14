
Play with Ansible
=================

maybe tba.

currently dev on mac...
nah, dev on cueball... darn in

so just copy a new vagrantfile here.
one that need two or three hosts anyway.


ref:
https://ryaneschinger.com/blog/ansible-quick-start/


adhoc:
ansible all -i inventory.ini -m ping -u root
ansible all --inventory-file=inventory.ini --module-name ping -u vagrant --private-key=~/.vagrant.d/insecure_private_key


$ ansible all -i inventory.ini -m command -u root --args "uptime"
ansible all -i inventory.ini -u root -a "uptime"

$ ansible all -i inventory.ini -m apt -u vagrant -a "name=zsh state=installed -s"
# -s sudo 
# -K, --ask-sudo-pass

execute playbook
ansible-playbook myuser.yml -i inventory.ini -u root




http://galaxy.ansible.com
Find pre-built playbook roles from the community.



Vagrant container setup using Ansible playbook
----------------------------------------------

https://www.vagrantup.com/docs/provisioning/ansible.html

vagrantfile_play.yml	# eg of this in singhub, vagrant provision to call this play
	# https://www.digitalocean.com/community/tutorials/configuration-management-101-writing-ansible-playbooks 
	# at the end has eg for playbook.yml for Vagrant, but eg for ubuntu or Debian


example ansible playbook yaml 
-----------------------------


tba, but naming like follwing probably work
workstn_mint17.yaml
workstn_sl7.yaml
webserver.yaml
node_sl7.yaml
node_sl6.yaml
