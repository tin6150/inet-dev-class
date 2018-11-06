

tig - telegraph, influx, grafana - stack for monitor and graphing for linux servers

plan to roughly follow this guide, using docker to install the stack.
config files are mapped between host and the container.
	https://hackernoon.com/monitor-your-infrastructure-with-tig-stack-b63971a15ccf

something was missing from above.
this guide maybe better anyway:
	https://blog.linuxserver.io/2017/11/25/how-to-monitor-your-server-using-grafana-influxdb-and-telegraf/


~~~~

first target install is bofh_zorin 2018.0903


prereq for debbian: 
- docker.io
- docker.compose

# edit docker-compose.yml and telegraph.conf to suit local system need.
# port 3000 was in use on bofh_zorin 

docker-compose up 	# see console output, but if hit ^C in this window, all 3 containers are closed!
docker-compose up -d	# daemon mode

docker ps

http://bofh:3000/
note that it is NOT https

graphana login
admin/admin
changed, but where is it saved??
inside the docker container?
influx db?
pwd change persisted after a "docker kill grafana" and ^C on the "docker-compose up" screen.

it would make sense for changes to be saved to influxdb, since there will be lots of customaizations.


FIXME ++ how to make sure data is persistent
============================================

changed docker-compose.yml
hit ^C
then docker-compose up -d
saw:
	**^ tin bofh ~/tin-gh/inet-dev-class/tig/conf ^**>  docker-compose up -d
	Recreating telegraf
	Recreating influxdb
	Recreating grafana
grafana profile was reset :(



Grafana config
==============

adding data source
------------------

For config using docker container, the CNI used by the containe means it cannot reach the influxdb via 
http://localhost:8086
Host FQDN is one solution (else find out that IP kubernetes assigned to the influxdb container).



INFLUXDB config
===============

Digital Ocean mentioned needing to create user
but most other post omited this step. 
no one even map the influx conf file in the docker env.
https://www.digitalocean.com/community/tutorials/how-to-monitor-system-metrics-with-the-tick-stack-on-centos-7

influx
  CREATE USER "sammy" WITH PASSWORD 'sammy_admin' WITH ALL PRIVILEGES
  show users
  exit

other influx commands
show databases
use _internal

~~~~
transiet commands

mkdir TMP; cd tmp
docker exec telegraf           telegraf -sample-config > telegraf.sample.cfg
#           ^^container_name   ^^cmd


docker stop telegraf grafana influxdb


