
VirtualBox Ref
**************

(placed here cuz VirtualBox almost always used with Vagrant and Ansible in my setup).

::

	VBoxManage list vms
	VBoxManage getextradata singhub_default_1510004309623_760 enumerate

	VBoxManage setextradata "[VM_NAME]" VBoxInternal2/EfiGopMode N
	Replace N with one of 

	N=   	Resolution=
	0    	640x480, 
	1	800x600, 
	2	1024x768, 
	3	1280x1024, 
	4	1440x900, 
	5 	1920x1200 


	VBoxManage setextradata to add CustomVideoMode1 with your desired resolution.

	Also need VirtualBox Guest Addition

	export KERN_DIR=/usr/src/kernels/2.6.18-... 
	actually, best to ask yum to install specific version that matches uname -r.
	yum apparently just install latest version by default, which make sense knowing how yum works.
	patching and reboot should get them to be at the same level...
	but for centos 6 maybe not...


	VirtualBox Extension for additonal driver, etc
	wget http://download.virtualbox.org/virtualbox/5.1.0/Oracle_VM_VirtualBox_Extension_Pack-5.1.0.vbox-extpack


	VBox
	VirtualBox	# start main gui




Resolution:
https://github.com/geerlingguy/macos-virtualbox-vm


