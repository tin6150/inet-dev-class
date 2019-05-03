
Following spin nersc docker tutorial #1
https://docs.nersc.gov/services/spin/getting_started/lesson-1/

a docker container for flask application (maybe put psg as static pages in there)


~~~~
bofh is having problem building container...
so moving (really meant cp) to tin-gh/inet-dev-class/docker  

export DOCKER_OPTS="--dns 8.8.8.8"
docker build
didn't work either

/etc/docker/daemon.json 
i had said iptables: false
which causes problem for this
(prob can't talk to dns server, no matter what other changes i do).

firewalling container images will continue to be an issue.
which is why docker, imposing its own network stuff, becomes a pain

~~~~


spin run permissions.
see lesson 2
https://docs.nersc.gov/services/spin/getting_started/lesson-2/

#SPIN_DIRECTORY=/global/project/projectdirs/YOUR_COLLAB_DIRECTORY/YOURUSERNAME-first-stack
SPIN_DIRECTORY=/global/project/projectdirs/m669/tin-first-stack
mkdir $SPIN_DIRECTORY
mkdir $SPIN_DIRECTORY/web
chmod o+x $SPIN_DIRECTORY $SPIN_DIRECTORY/web

change docker-compose from laptop version to spin version

export RANCHER_ENVIRONMENT=sandbox

rancher up --render


~~~~

docker tag commands

**^ tin bofh ~ ^**>  docker image tag my-first-container-app registry.spin.nersc.gov/tin63/my-first-container-app 
**^ tin bofh ~ ^**>  docker image tag my-first-container-nginx registry.spin.nersc.gov/tin63/my-first-container-nginx
**^ tin bofh ~ ^**>  docker login https://registry.spin.nersc.gov 
**^ tin bofh ~ ^**>  docker image push registry.spin.nersc.gov/tin63/my-first-container-app
**^ tin bofh ~ ^**>  docker image push registry.spin.nersc.gov/tin63/my-first-container-nginx



rancher up --render
rancher up 

rancher stack ls
rancher rm tin-first-stack     --type stack 
rancher rm my-first-container  --type stack 



concept of container vs stack
rancher ps
rancher ps --containers --all 

rancher stop  my-first-container
	# rancher ps show entries, with state as inactive
rancher start my-first-container


rancher inspect my-first-container/web | jq . | less
	# look for fqdn and pubilc
	# http://web.my-first-container.sandbox.stable.spin.nersc.org:60000
	

see https://docs.nersc.gov/services/spin/cheatsheet/#rancher-cli-cheat-sheet

