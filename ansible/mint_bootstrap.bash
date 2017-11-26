

# run script as me (tin).  
# probably need lot of cut-n-paste
# unless split into multiple part...





sudo useradd -g users -G sudo -m -s /bin/bash  -u 43413  tin
# -g wheel don't work in ubuntu as no wheel group 
# but there should be users:100 group
#pwconv


# mkdir /home/tin
# chown -R tin /home/tin






CASA=/home/tin
mkdir $CASA/tin-gh
cd $CASA/tin-gh
git clone https://tin6150@github.com/tin6150/psg

ln -s $CASA/tin-gh/psg $CASA/PSG
ln -s $CASA/tin-gh/psg/script/sh/.bashrc       $CASA/.bashrc
ln -s $CASA/tin-gh/psg/script/sh/.bash_profile $CASA/.bash_profile
source $CASA/.bashrc

# don't want to do this, but even then sudo visudo still default to nano!!  
#sudo cp -p $CASA/tin-gh/psg/script/sh/.bashrc       /root/.bashrc
#sudo cp -p $CASA/tin-gh/psg/script/sh/.bash_profile /root/.bash_profile
sudo dpkg --remove nano


cd $CASA/tin-gh
git clone https://tin6150@github.com/tin6150/inet-dev-class
ln -s $CASA/tin-gh/inet-dev-class/ansible ~/Ansible
cd $CASA/tin-gh/inet-dev-class/ansible

# install ansible using PIP, from README.rst ::
sudo apt-get -y install python-pip
sudo pip install --upgrade pip
sudo pip install --upgrade setuptools
sudo pip install --upgrade ansible  # 2.4.1.0

# not sure where mate-terminal config are stored
# snMadBook use 9 pt font.  run terminal as login shell, it source .bash_profile



sudo apt-get update
sudo apt-get install openssh-server
sudo systemctl start sshd
sudo systemctl enable sshd
# but still convoluted way to NAT thru vbox
# VBoxManage modifyvm "VMNAME" --natpf1 ...



# git config, not too important
# run as tin

git config --global user.email "tin@mint18"            
git config --global user.name tin6150
git config --global credential.helper 'cache --timeout=36000'
git config --global github.user   tin6150
git config --global alias.lol "log --oneline --graph --decorate"        





# could paste md5 into /etc/shadow, but not sure if that's safe if script is publicly accessible...

echo mate-mouse-properties  to add control to highlight mouse
echo mate-window-properties to change windows focus to follow mouse -- sloppy mouse

echo "run sudo passwd tin; then disable user osboxes"
