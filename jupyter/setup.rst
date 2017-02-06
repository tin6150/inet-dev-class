
Setting up to run jupyer in various platform
--------------------------------------------




# these didn't work 

module load python/3.4.2-goolf-1.5.14-NX
pyenv ~/local_python_3.4.2                     # python2 use virtualenv
source ~/local_python_3.4.2/bin/activate


# trying this now:
module load python/3.5.1-goolf-1.5.14-NX
pyvenv ~/local_py351goolf
source ~/local_py351goolf/bin/activate
pip install pylint                              # didn't really need this?  it was just eg?
pip install --upgrade pip



cd /home/ti1/code/sn-gh/inet-dev-class/jupyter
jupyter notebook



pip install --upgrade https://github.com/ipython-contrib/jupyter_contrib_nbextensions/tarball/master
jupyter contrib nbextension install [--user] [--sys-prefix] [--symlink]
jupyter nbextensions_configurator enable [--user] [--sys-prefix]
jupyter nbextension enable|disable <extension>

# edit from jupyter web page :)


the .ipynb file is a json file, so can dump to github and diff it.
use "new" to create a new notebook from the browser interface that load
typically http://localhost:8888/ 
