

2019.0424 
nersc spin (docker/rancher) training session #1.


presenter:
Stefan Lasiewski
Kelly Rowland (former UCB Domain consultant)
Cory Snavely
Rollin Thomas

https://docs.nersc.gov/services/spin/getting_started/lesson-1/


need dir to be chmod g+x 
so that spin can see the dir and not try to create it.

port was assigned randomly for each user.

   ext: internal port mapping:
   ports:
    - 60039:8080
	(currently random for 60000-60050)
	port 8080 is allowed from general internet.


container volume mapping is also external to internal
      - /global/project/projectdirs/isguser/SpinUp/lesson-2-data/web/nginx-proxy.conf:/etc/nginx/conf.d/default.conf:ro

spin need access to the full dir path.
note that isguser is not world readable, only world executable.
so, can cd to the path, but not run ls at the isguser dir

lower leve is more open.

use userid is simpler than username
if using username, the username need to be defined inside the image (eg /etc/passwd?) 

even when container run as root, it is root without any power
cuz of the capabilities drop clause.

this help if web server is compromised, it cant really have much access.

    user: 80115:80115


~~~~

rancher up --render	# read docker-compose file, check most syntax error

unset RANCHER_ENVIRONMENT



start the stack
rancher up

alt start, for dev:
rancher up -d 
	-d take logs and put it in background.  semilar to docker -d option



ERRO[0020] Failed to get logs for tin-first-stack-app-1: Failed to find action: logs 
ERRO[0020] Failed to get logs for tin-first-stack-web-1: Failed to find action: logs 

this means web service failed to start
(for everyone in the class)

\rancher stack ls

see STATE unhealthy for the stack.
often will find many such case in dev 




 rancher ps
ID        TYPE      NAME                  IMAGE                                                         STATE        SCALE     SYSTEM    ENDPOINTS   DETAIL
1s11472   service   tin-first-stack/app   registry.spin.nersc.gov/tin/my-first-container-app:latest     activating   1/1       false                 Container should have been running but is in error state. Check logs for more information.: Error response from daemon: pull access denied for registry.spin.nersc.gov/tin/my-first-container-app, repository does not exist or may require 'docker login'
1s11474   service   tin-first-stack/web   registry.spin.nersc.gov/tin/my-first-container-nginx:latest   activating   1/1       false                 Container should have been running but is in error state. Check logs for more information.: Error response from daemon: pull access denied for registry.spin.nersc.gov/tin/my-first-container-nginx, repository does not exist or may require 'docker login'


STATE is activating
means rancher is restarting.


upgrade the stack
rancher up --upgrade


don't work cuz state is activating, not inactive.
so blow away the stack and restart.

rancher rm --type stack tin-first-stack

	default get name from the directy
	can give it diff name by using a flat to spell it out 


find name in registry

https://registry.spin.nersc.gov
login with NIM password (no OTP) .
see what username was assigned

can hit ^C to stop viewing the log, service will keep running.
(not for docker, which would stop the stack).
rancher is a saner default from Stephan's perspective.



                service name (thus /web):
rancher inspect tin-first-stack/web

-web-instanceName for container ... watch out for this in rancher ps vs service

rancher inspect tin-first-stack/web | jq '.fqdn'
# jq parses json to be more human readable 
also query for specific string (essentially grep?)
# jq req a param of what to look for.  for everything, use '.'
rancher inspect tin-first-stack/web | jq . | less 

	"fqdn": "web.tin-first-stack.sandbox.stable.spin.nersc.org",

	"publicEndpoints": [
	    {
	      "hostId": "1h84",
	      "instanceId": "1i2842191",
	      "ipAddress": "128.55.206.20",
	      "port": 60039,


	dont use the IP, as that floats in the famr.

if getting null, skip the use of jq
actually, forgot /web in the service name

my service is started as:
	http://web.tin-first-stack.sandbox.stable.spin.nersc.org:60039/



update docker-compose
rancher up --upgrade

refresh browser


rancher ps 

shows state UPGRADED

export RANCHER_MATCH
upgrade has 2 steps
scale: 2/1
two instance of container avail, but only 1 running

rancher ps --containers --all

container run as a service

when doing upgrade, stop old container, start new one.
need to get rid of old container, 
ie, commit the upgrade

rancher up --confirm-upgrade 
--or--
rancher up --upgrade --confirm-upgrade   # this does the two step upgrade and confirm in one go, ie, by pass a temp stage to manually check for the upgrade.


healthy vs running
if no health check in the container, then it only shows running.



need confirm upgrade
if not done, other rancher command will fail in weired way

once confirmed, the old container is gone and gone forever.
image is still there, still in the registry, on a diff server.
but container instance is gone.


scale to 2 server
rancher scale tin-first-stack/web=2 

rancher ps --containers --all


rancher logs tin-first-container-web-2
ie, need to use container name, not the service name in this case.


get shell into the service
can't ssh, 
but can use
rancher exec  -it tin-first-stack/web /bin/bash
(similar to docker exec)

provided service name, will get prompted on which container to connect

based on alpine, smallest possible linux
don't have much util to speak of.  not even ps

the username is not avail, so bash prompt is also funky



host web.tin-first-stack.sandbox.stable.spin.nersc.org
	web.tin-first-stack.sandbox.stable.spin.nersc.org has address 128.55.206.71
	web.tin-first-stack.sandbox.stable.spin.nersc.org has address 128.55.206.20

this exercise not using load balancer
just round robbin to two instance

(host is a standard unix cmd, not rancher/docker thing)

host sciencesearch-ncem.lbl.gov 



10 things for rancher in spin


rancher export STACK

	good to mkdir/cd ~/spin
	so that output is dumped in there

	STACK is the dir name and the def stack name.

rancher export -f - STACK | less

this is super important ...
when there are several folks is managing the stack.

instead of using rancher hub... use git instead.
so that it ensure it is commited change.

export RANCHER_ENVIRONMENT=<env>

if don't set ENVI.. rancher will ask to pick.
(curently sandbox, dev, proc)_

rancher up --upgrade -d 
# -d = dont keep going, return to shell immediately 
  so dont have to hit ctrl-c to get back to shell

rancher up --rollback -d



current reverse proxy handle some cookie-based stickiness.
underneath is HAproxy




rancher export 
to put the thing in docker-compose and check into git.


rancher logs STACK/SERVICE

rancher logs -f STACK/SERVICE
-f = follow, like tail -f

--tail NUMBER
to get x number of tailing line in the log

rancher logs --help

log retention is not indefinate in rancher

these logs that go to std out and std err
go to nersc cybersecurity

add other logging if desired, eg complete repo in fs.
but don't skip out std out

rancher up --render

it is similar than docker-compose config --quiet




rancher stop tin-first-container
             ^^^ service name


can't have rancher cli on laptop
cuz they had some customization in spin
to enforce user separation, also perf enhancement.

so must use cori/edison.

in future, as move to rancher 2.0
use kubernetes
may allow external access if possible.

want to decouple spin from cori, so their maintenance don't affect spin.



docker compose... 
if have keywork like BUILD
that does things on the fly.

work for docker cuz self contained.

but only subset that works in rancher.
rancher req images retrievable from registry.




11:48

networking overview.

Shifter.. shane cannon


scale container
ping on service name
has a private DNS
multiple instance
same name...

eg ping DB
in dev, prod.
portable naming.

reverse proxy
can stop https at the reverse proxy

a number of peep did lets encrypt at the container, and that will work too

CNAME
to lb.reverse-proxy.prod-cattle.stable.spin.nersc.org

they will config the reverse proxy
www.mydomain.org -> stack/service

ssl config within 
SNI protocol is support.
virtual hosting w/o ssl connection 

end-to-end encryption, spin dont see.. but still a bit of info, SNI use that to load balance.

dyn dns name created is
<service>,<stack>.<env>.stable.spin.nersc.org

3128, 3306, 8008

a number of such ports are made avail to public by default.
other are restricted to LBL address range automatically



Cory
prefer to handle ssl for us
directive from homeland security
on how https should be configured

if we do ssl termination, then it becomes our problem.
they can ensure ssl use req encryption, etc.


rancher 2
internal traffic are ipsec ssl encrypted
10G
but in practice see 1G
overhead seems high.


~~~~

SNI 
allos TLS cert
multiple to a single IP
so used by hosting provider.

~~~~~

corky bug
my username i guess in spin is tin63
so push to registry, 
docker-compose etc
should all use that 'tin63' as the username

as that's what is used internally







~~~~

val / valerie
daniel
cory

