

started with TIG stack as in README.rst

but got a feeling that influxDB is not keeping its data thru restart of docker
there used docker-compose

now just following docker run command listed in dockerhub of influxdb.

ensure that i have a stable db first.


influxDB
========


https://hub.docker.com/_/influxdb/

manually init db:

docker run --rm \
      -e INFLUXDB_DB=db0 -e INFLUXDB_ADMIN_ENABLED=true \
      -e INFLUXDB_ADMIN_USER=grafana -e INFLUXDB_ADMIN_PASSWORD=grafana \
      -e INFLUXDB_USER=telegraf -e INFLUXDB_USER_PASSWORD=telegraf \
      -v /home/tin/tin-gh/inet-dev-class/tig/conf/influxdb.conf:/etc/influxdb/influxdb.conf \
      -v /opt/tigM2/influxdb:/var/lib/influxdb \
      --name i_pod \
      influxdb /init-influxdb.sh

**^ ^** 
docker run --rm \
      -e INFLUXDB_DB=db0 \
      -v /home/tin/tin-gh/inet-dev-class/tig/conf/influxdb.conf:/etc/influxdb/influxdb.conf \
      -v /opt/tigM2/influxdb:/var/lib/influxdb \
      -p 8083:8083 \
      -p 8086:8086 \
      --name i_pod \
      influxdb:1.5  

results in (very similar to docker compose):
 docker ps
CONTAINER ID        IMAGE               COMMAND                  CREATED             STATUS              PORTS                                            NAMES
4819685d2836        influxdb:1.5        "/entrypoint.sh in..."   24 seconds ago      Up 22 seconds       0.0.0.0:8083->8083/tcp, 0.0.0.0:8086->8086/tcp   i_pod


**^ ^** 
docker exec -it i_pod influx


#?  use db0
create user "tin" with password 'tintin168' with all privileges
create user "tin2" with password 'tintin168' with all privileges
create user "sammy" with password 'sammy_admin' with all privileges

> show users
user     admin
----     -----
grafana  true
telegraf false
tin      false
tin2     true
sammy    true


> create database tin_dockerrun
> show databases
name: databases
name
----
db0
_internal
tin_dockerrun



**^ ^** 
docker run --rm \
  --name t_pod \
      -v /home/tin/tin-gh/inet-dev-class/tig/conf/telegraf.M2.conf:/etc/telegraf/telegraf.conf:ro \
      -v /opt/tig/telegraf:/var/lib/telegraf \
      -v /var/run/docker.sock:/var/run/docker.sock \
      -v /var/run/utmp:/var/run/utmp:ro  \
      -v /sys:/rootfs/sys:ro  \
      -v /proc:/rootfs/proc:ro  \
      -v /etc:/rootfs/etc:ro  \
  telegraf:1.5


**^ ^**   ##no need## docker exec -it t_pod bash 


influx container i_pod, don't see new database (telegraf) :(

> show databases
name: databases
name
----
db0
_internal
tin_dockerrun





~~~~~



testing against old docker-compose 
now that auth-method has been reset to (def: false)

**^ tin bofh ~/tin-gh/inet-dev-class/tig ^**>  docker run --rm \
>   -v /home/tin/tin-gh/inet-dev-class/tig/conf/influxdb.conf:/etc/influxdb/influxdb.conf \
>       -v /opt/influxdb:/var/lib/influxdb \
> --name influxdb_pod influxdb:1.5

create user "dc" with password 'dc168' with all privileges



> show users
user admin
---- -----
dc   true
> show databases
name: databases
name
----
_internal


some db and retention really seems gone from this instance :(
> show retention policies on _internal
name    duration shardGroupDuration replicaN default
----    -------- ------------------ -------- -------
monitor 168h0m0s 24h0m0s            1        true


> create database tin
> show databases
name: databases
name
----
_internal
tin

