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

    ansible all -m shell -a "shellCmd"
    ansible all          -a "shellCmd"               # shortcut of above

    ansible servers -i inventory.ini -m command -u root --args "uptime"
    ansible workstn -i inventory.ini -u root -a "uptime"

    ansible ubu1    -i inventory.ini -m apt -u vagrant -a "name=zsh state=installed -s"
    # "all" means every hosts in the inventory file
    # "servers", "wrokstn" would be group defined in the inventory file.
    " "ubu1" is example one specific machine to run ansible on
    # -s sudo 
    # -K, --ask-sudo-pass
    # -i specify inventory file, can set ANSIBLE_HOSTS, def /etc/ansible/hosts



    ansible localhost -m setup              		# discoverd facts as dict ansible_facts
    ansible localhost -m setup -a 'filter=ansible_eth*'	# filter

    ansible-doc -l          # list docs
    ansible-doc git         # doc on the git module

execute playbook::

    ansible-playbook myplaybook.yml -i inventory.ini -u root
    sudo ansible-playbook -vvv myplaybook.yml -i inventory.ini 

    ansible-playbook myplay.yml -i inventory.ini --limit workstn    # only specific group of machines in inventory 
    ansible-playbook myplay.yml -i inventory.ini --limit ubu1	    # only one specific host

    ansible-playbook myplay.yml -i inventory.ini --list-hosts	    # see which hosts would be included in execution

    -u jane    --remote-user=jane	# think of ssh -l jane
    -e VARS    --extra-vars=VARS	# define extra variables  eg?
    -e http_proxy="http://proxy.myco.com:2011/proxy.pac"  ??

    --check	# dry run mode

help::

    ansible-doc -l      # list ansible modules
    ansible-doc yum     # doc on the yum module
    ANSIBLE_LIBRARY     # default search for ./library 

YAML
****

	"YAML is a crime against humanity"
	https //www.amazon.com/gp/customer-reviews/R290VXURWU5N36/ref=cm_cr_dp_d_rvw_ttl?ie=UTF8&ASIN=B0743VR1MC


.. code:: yaml

    list: entries are prefixed with '-', 
    eg:

        listA:
          - foo
          - bar

    which converts to python as 

    {'listA': [
                'foo',
                'bar'    
              ]
    }


    map/structured list does NOT have '-' prefix in each entry, 
    and each entry contains ':' indicating the key/value.       
    eg:

        mapB:
          foo: 13
          bar: 14

    which converts to python as

    {'mapB': {
               'foo': 13,
               'bar': 14
              }
    }


Now, what clause expect a list and what clause expect a map in ansible??
that's probaly the next insanity that need to be memorized.

(info from J.G. Ansible For DevOps Appendix B p377) 


* with_items expect a '-' list

* tasks expects a '-' list, cuz number of items is variable. (?)
* the "tasks:" keyword itself is not prefixed with '-' ??

* copy:  expects a map, cuz essentially need a key-value map of all parameters.  while some params are optional, it is a FINITE set of possible params, and it is all of ONE copy instruction.  

* "commands" that can be single line with key=value or multi-lines key: value entries are "structured map" and does not use '-' for each item (?)

* block: ??

* - hosts: ...   if hosts: clause is allowed, it is always with '-' prefix?


YAML, example of craziness  
--------------------------

- pay very careful attention to indent level and when to use '-' and when NOT to use '-'.

- Only "hosts:" is prefixed with '-', none of the other clauses at the same indent level.  

- "block" probably throw a wrench into this whole thing.  This thing is quite fuzzy.  Maybe I am using it wrong.  
  Have a look at http://docs.ansible.com/ansible/latest/playbooks_blocks.html

::


    - hosts: all
      vars:
         ftp_proxy: "http://ex-proxy:80"
      vars_files:
         - vars.yml
      pre_tasks:
         - name: update apt cache
           apt: update_cache=yes cache_valid_time=3600
           when:  # ... some condition here
      tasks:
         - name: install sw list
           apt: name={{ item }} state=present
           with_items:
             - python-apt
             - git
         - apache2_module: name=rewrite state=present
           notify: restart apache
         - name: symlink example
           file: 
               src:  "template/{{ domain}}.conf
               dest: "/etc/apache2/{{ domain}}.conf
               state: link
           notify: restart apache
         - copy:
               src:  "{{ item.src }}"
               dest: "{{ item.dest }}"
           with_items:
                - src:  "httpd.conf"
                  dest: "/etc/httpd/conf/httpd.conf"
                - src:  "httpd-vhosts.conf"
                  dest: "/etc/httpd/conf/httpd-vhosts.conf"
      handlers:
         - service: name=apache2 state=restarted
      


Why YAML maybe good for reading, but is a crime against programmers
*******************************************************************

The fact that things are treated as string more or less by default means 
A LOT of unintended errors are not catched when .yml is "compiled".

Have a look at this block:

::

          notify:
               - Create new initramfs
               - register: buildInitramfs

I am a novice in Ansible, I was HOPING that "register:" command would work when the 
notification section is triggered.
No it doesn't.  
YAML treated it as any string, not special keyword/clause for Ansible to act on.


Now have a look at this other block:

::

	- hosts: none
	  tasks:
	  - include_tasks: task1.yml
	  - include_tasks: task2.yml
	    when: ansible_os_family == "Debian"    # Delete two leading space and this line has a whole different meaning!!


I get it, people want to read text.  Lisp with all its parenthesis are very horrible to read.
But proper braces help cut-n-paste and shifting of block level to realize what the original meaning was.

::

	Thus, while "YAML is a crime against humanity" maybe overblown, 
	"YAML is a crime against programmer" should be quite fitting.  While I am at it, food for search robots:
	"YAML is a crime against DevOps"
	"YAML is a crime against SysAdmins"
	"YAML is Madness"

	Some tweeter post said "YAML is a hate crime".  yeah, that's it!!

But i guess... YAML itself is fine.  Making list and array with simple english is fine.
It really is Ansible using YAML to implement a highly complex definition language that makes it so disgusting.
Yet I like the simple, incremental deployment that Ansible provides (vs say Puppet, CFEnggine).  
So, I take my hate against YAML, and not Ansible.  Crazy eh?
Did someone say Salt??  Never mind, it has the partner in crime.



Where is the grammar book for Ansible's YAML?
*********************************************

I know - define a list, and there are things like list and ??
But, a play expect it to be started as "- hosts:" ?
And a handler is allowed in a play?
But not inside a block construct?

*sigh* 
I have not been able to find the "Regular Grammar" definition for any ansible yaml definition.  
The list of playbook keywords is the closest thing.  But I am still very fuzzy what is allowed where.  
http://docs.ansible.com/ansible/latest/playbooks_keywords.html#task


YAML constructs/keywords
************************

- lineinfile
- regexp
- notify
- get_url
- command   # pretty close to verbatim cli
- shell     # has clause for chdir, creates, etc.
- register
- git       # depends on git package installed on ansible client machine
- file      # state: directory  to create dir rather than file
- stat      # can create symlink, etc
- copy
- rsync
- unarchive # good for large amount of files to copy



ref
---

* https://github.com/geerlingguy/ansible-for-devops [reading book also ex]
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

    sudo easy_install pip
    sudo pip install ansible
    -or-
    wget https://dl.fedoraproject.org/pub/epel/epel-release-latest-7.noarch.rpm
    sudo yum install ./epel-release-latest-7.noarch.rpm
    sudo yum install python2-pip 
    sudo pip install ansible         # 2.5.0

Mint 18.2 MATE::

    sudo apt-get -y install ansible          # ubuntu 16.04 comes with ansible 2.1.1.0, no "import_tasks"
    --or--
    sudo apt-get -y install python-pip       # cueball
    sudo pip install --upgrade pip
    sudo pip install --upgrade setuptools
    sudo pip install --upgrade ansible  # 2.4.1.0
    #					# 2.5.2 on lunaria 2018.05

Mint 17.2::

    sudo apt-get install ansible	# 1.5.4+dfsg-1  ... very old, don't understand "become"
    sudo apt-get remove  ansible
    sudo pip install --upgrade setuptools
    sudo pip install --upgrade ansible	# 2.4.1.0
    sudo apt-get install python
    sudo apt-get autoremove				# clear out python-jinja2 python-yaml

    arggg... backbox / ubuntu notes not pushed...   but I think same versions as mint 17.2

Fedora 25::

	have ansible go in there and install? :)

backbay 14::

    sudo pip install ansible   # 2.4.1.0
    sudo aptitude show ansible # 1.5.4+dfsg-1

Windows Services for Linux aka Ubuntu 16.04 on win10::

    # sudo apt-get -y install python 
    # sudo apt-get -y install python-pip python-dev libffi-dev libssl-dev
    # pip install ansible  # 2.4.2.0
    # https://www.jeffgeerling.com/blog/2017/using-ansible-through-windows-10s-subsystem-linux
    # I didn't use this, but JG suggested: (--user installs packages local to the user account instead of globally to avoid permissions issues with Pip and the Linux Subsystem)



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

    [server]
    svr1
    svr2

    [workstn]
    ubu1
    ubu2
    centos1
    centos2
    cueball
    swingset



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
    


Ansible Pull
************

For "pull method" where ``hosts: localhost`` is used in the playbook:

``ansible-playbook -v site.yml -i "localhost," -c local`` should be prefered over  
``ansible-playbook -v site.yml -l localhost``
the former will work for group_by, the latter don't.


Troubleshooting
***************

ansible localhost -m setup 			# run ansible, print out all "facts" it gather.  eg grep os_family



Books
*****

Was just trying to find a book to buy to learn about it.  Impression from reading ToC and Reivews.
many seems disapointing from just the review.
if/when i actually get a book may be dissapointing.
another reason why i kinda gave up on buying book to learn new tech.
but reading online is just not a cohesive flow.
If can find a good book, it should still make learning easier.  it is whether such a book exist at my right learning level...


- Ansible for DevOps by Jeff Geerling 
	trying to get this.  covers vagrant and ansible to get started.  then move to playbook and roles.  seems the right stuff to cover.


- Ansible Playbook Essential (packt)
	possible.  not very extensive, but seems to cover from starting up to some good fundamentals for basic project.

- Insfrastructure as Code (o'rly)
	possible.  Not really on ansible, but sections cover patterns and antipatterns of config mgmt.  may hopefully learn how to lay the structure of a site, how to divide, what modularity granularity to employ...




- ansible up and running (o'rly)
	some good review, yet other review says code not tested.  too many fragments, so not good end to end, which maybe important cuz way of YAML.


- mastering ansible by jessie kidding (packt)
	cover internal of how ansile work.  
	hot it eval vars, templates, send code to remote host for execution.
	maybe good for sys admin trying to get ansible work in existing large scale deployment
	but then maybe just need to google for these as they come up...

- Implementing DevOps with ansible
	Don't like, too much about teaching the way of devops, and ansible is just like an example.  

- Learning Ansible 2 (packt)
	maybe a very beginner book.  talk about setup, test.  1 reviewer said spend too little time to reallhy teach ansible.


TMP note
********

cueball/bofh in CF_BK/cueball/ANSIBLE/ 

for dev on linux, 
maybe copy Vagrantfile here.
then it can be customized to have multiple hosts, which req more convoluted setup.

(but for now, on c7, have continued to use the Vagrantfile on singhub).


mint182 vm in snMadBook "localhost" yaml in this dir as of 2017.1126

rst cheatsheet https://github.com/ralsina/rst-cheatsheet/blob/master/rst-cheatsheet.rst



GitHub rst parser notes
-----------------------

indent of block above with === header trip github parser.

dotdot comment block are NOT liked by github -- maybe trips the parser, maybe just not render them as comment.
not even when as footnote notation (cuz lacked ref?)  just avoid them for github rst parsing.


~~~~


:url: https://github.com/tin6150/inet-dev-class/tree/master/ansible
:author: tin6150
:version: 2017-1210

