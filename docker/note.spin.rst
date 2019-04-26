

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

~~~~~~~~~~
~~~~~~~~~~
~~~~~~~~~~
~~~~~~~~~~


Day 2, Fri 2019.0426
9:30

start with Storage.
(actually left from last session)


docker storage is confusing.
- kinda there, works.  but ephemeral!!!!!
- container can be restarted, but it is taking a fresh copy, changes in a last instance, in a /var, and vanishes.  stateless.
- additional storage provided by spin.
- block? file? db? image? table?
- trying to store compute and science gateway?

- mount volume.  DATA... don't want to be part of image.
- alt is interactively interact with the image.  but not recommended, maybe hard to find the image/data in the future.  ie, it is an undocumented path of how it got there.


- GHI - GPFS + HPSS - being worked on by storage group.


volume must be associated with a stack.
- see slide, which include naming convention
- named after the service and stack that owns it
- 


rancher stack create --empty mystack

rancher up also create a stack 

perm
o+x for mount path (all along the path)
g+s for dir

could mount single file.
but if unlink the inode, may get weird

be careful with database container
mounting db volume via bind

if use scale:2, then it will be a race condition of
two db writting to the same place
and things may seems to run, but will get garbage.

for postres, there was example of mounting 
/var/postgresql
but container end up writting to /var/postgressql/data
which became a second volume, internal to container
so it was ephemeral!
this BIT Cory and took long time to figure out.
see pic/ slide for detail.



spin to submit job, 
use ssh keypair from within the container
- API coming in future


with rancher 2, 
- support rancher ui (currently user not allowed to use ui cuz could not secure it).
- 

networking and dns
- very autoamtic, but some perf hit, due to ipsec.
- generated DNS names and created for non-human access
  (ie, dynamic, long names).
  cutom name need NERSC help.


*they did a lot of work / customization to secure the env*

eg, they check the compose file that CAP_DROP all 
is used, but allow adding back some cap that does not compromise 
FS/security 


~~

10:45, real start of day 2 materials as published.

(Ron ?) as presenter


Microservice design.

(so spin group maybe 3 guys + Kelly)

Attendees to present a sample use case
and try to get SPIN for it.


11:04 am
Dilan
ALS 
new app.
beam line.

Authentication and Authorization 
is a big piece and need answer.
Spin (Ron?) says has all the answer to that.

set of files 
are likely in HDF5.
to retrieve subset of file
would need some logic to fetch that.
this means it is not going to be nginx to serve static file.
likely need to go thru API server to make req
and have it return the sub-setted data.


green unicorn, flask, nginx 
as stack.

ugx uwsgi server ?

flask and tornado has way to break things up internally.
flask blueprint that works ok
tornado has a request handler.
	not cuz of perf, but for compatibility reasons.

if api are versioned separately



~~

life experience of using spin.

On Ramp dev model (in contrast to "classic" build/ship/run of docker).

create flask/green unicorn/whatever app 
put container image in cori

mount ap.py dir and run it with 
"reload on source change" turned on
(11:25 am)

so, get basic stuff working.
but can do the polish up in live-ish spin/cori env.

will depend othe data fs (ie, global fs in cori)




avoid docker commit
it enable untrack changes into the container.
just don't do it!!

can export rancher compose
stick that into git.
(shreyas use it all the time, but Ron says don't use it!)

overall, spin folks don't touch the rancher compose much.



docker 
RUN env
vs 
RUN pwd
(force a build from a point,
docker don't always know something changed).


can run supervisor as PID 1

jupyther hub, 

monitor can be split into diff microservice.


~~

building docker images
(11:42)

alpine is small, nice, but no tools (not even ps).
bigger image is easier to work with.

many image start as root and drop cap.
but don't work well for those req global fs mount.
Spin has recipe for nginx

each time add a command, docker create a layer
thus, using && to chain the command help reduce layering.

RUN command will always run.

ADD vs COPY
very similar semantics
ADD has more fn semantics.
Share recommend using ADD rather than COPY.

COMMAND content get appended to the end of the ENTRYPOINT
(slide at 11:50)
tend to be exec $APP
but this behave oddly (eg when try to exec into the container).
if entrypoint isn't expected to take that argument, just run the old stuff.

&& rm -rf ...

so that clunk won't even end up in the layer.



SECRETS
11:53

eg ssh private key.  passwords. 

docker 
use to have a var, then password in there.
check into git, and password shared to the world!!!! :(

SECRETY in docker.

secrete naming.

using secrete is 3 step process.

_FILE  most are automagic looking for secret in a file.

create secret

echo "password" | rancher secret create db.stefanl-webapp.mysql-password

do this in cli, not in compose file.


rancher secret ls
have access control

can't read secret from cli
but can do that from the container shell.

(none of these thing seems encrypted)

look at the mysql
postgres
mongodb

all have same way of reading the same way to access secret.

don't check the password _FILE into git
they are not encrypted
grab the password _FILES and manally copy from laptop into production

but if they are just password for diff app layer to share data
can have some "garbage" data in it.

they are not encrypted
(but then why can't cat it, why need to retrieve via container?)


rancher 
  retain_ip: true

so that the contianer will always start under the same ip
nginx would work better in this setup.


Cron style syntax for non continuous job.
time in UTC. (docker native timezone).


passing compose var
like shell var, but some strange twist.

env set in shell 
can be accessed in the compose file eg ${PORT}


hack-a-thon
pretty much open
come with idea of things that we would like to implement.
come as far as possible
then come and ask for help.
come with some kind of project to do, even if it i just an exercise.




~~~~

Meet:
val / valerie
danniel
cory


~~~~




