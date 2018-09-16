

started with TIG stack as in README.rst

but got a feeling that influxDB is not keeping its data thru restart of docker
there used docker-compose

now just following docker run command listed in dockerhub of influxdb.

ensure that i have a stable db first.

2018.0915
noticed some ufw not blocking docker ports
so updated docker-compose.yml with the "M2" config tried out there.
run as:
docker-compose rm			# remove old images, if necessary

docker-compose up | tee compose.M2.out  # see console output, but if hit ^C in this window, all 3 containers are closed!
docker-compose up -d                    # daemon mode
docker-compose logs --tail=5 influxdb   # 



=============================================================
influxDB
=============================================================

Time-Series Data Storage
https://portal.influxdata.com/downloads#influxdb

ref:
https://hub.docker.com/_/influxdb/


docker network create influxdbnet
then start influx with:
--net=influxdbnet

manually init db once:

docker run --rm \
      -e INFLUXDB_DB=db0 -e INFLUXDB_ADMIN_ENABLED=true \
      -e INFLUXDB_ADMIN_USER=grafana -e INFLUXDB_ADMIN_PASSWORD=grafana \
      -e INFLUXDB_USER=telegraf -e INFLUXDB_USER_PASSWORD=telegraf \
      -v /home/tin/tin-gh/inet-dev-class/tig/conf/influxdb.conf:/etc/influxdb/influxdb.conf \
      -v /opt/tigM2/influxdb:/var/lib/influxdb \
      --name i_pod \
      influxdb /init-influxdb.sh




**^ ^** 
**compose.mode2** docker run --rm \
      -e INFLUXDB_DB=db0 \
      -v /home/tin/tin-gh/inet-dev-class/tig/conf/influxdb.conf:/etc/influxdb/influxdb.conf \
      -v /opt/tigM2/influxdb:/var/lib/influxdb \
      -p 8083:8083 \
      -p 8086:8086 \
      --net=influxdbnet \
      --name i_pod \
      influxdb:1.5  
		restarting influxdb this way does not get the message of "recreating influxdb", that's probably a docker-compose thing.
		previously not seeing data probably cuz enable auth and thus need to start influx cli w/ user/pass
		influx -username 'sammy' -password 'sammy_admin' 

results in (very similar to docker compose):
 docker ps
CONTAINER ID        IMAGE               COMMAND                  CREATED             STATUS              PORTS                                            NAMES
4819685d2836        influxdb:1.5        "/entrypoint.sh in..."   24 seconds ago      Up 22 seconds       0.0.0.0:8083->8083/tcp, 0.0.0.0:8086->8086/tcp   i_pod


okay, at least starting db this way works.  data seems to persist.
cece7 got telegraf installed, and used the config that writes to 128.3.10.10:8086, and 
telegraf db got created, and measurments (table? schema?) has tables that grows over span  of (telegraf report every 10s)
select count(*) from diskio


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


use telegraf
show measurements
select count(*) from diskio




root@537c7dfe857f:/# ip a
1: lo: <LOOPBACK,UP,LOWER_UP> mtu 65536 qdisc noqueue state UNKNOWN group default qlen 1000
    link/loopback 00:00:00:00:00:00 brd 00:00:00:00:00:00
    inet 127.0.0.1/8 scope host lo
       valid_lft forever preferred_lft forever
    inet6 ::1/128 scope host
       valid_lft forever preferred_lft forever
52: eth0@if53: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc noqueue state UP group default
    link/ether 02:42:ac:11:00:02 brd ff:ff:ff:ff:ff:ff link-netnsid 0
    inet 172.17.0.2/16 scope global eth0
       valid_lft forever preferred_lft forever
    inet6 fe80::42:acff:fe11:2/64 scope link
       valid_lft forever preferred_lft forever


presumably mapped to host, so bofh should work
but netstat bin not avail.



=============================================================
Chronograf 
=============================================================
Time-Series data viz.

install:
docker pull quay.io/influxdb/chronograf:1.6.2

info:
https://docs.docker.com/samples/library/chronograf/#using-the-container-with-influxdb


change influxdb to create a docker network "influxdbnet"
docker network create influxdbnet
--net=influxdbnet

docker run --rm \
    --net=influxdbnet \
    -p 8888:8888 --name c_pod \
    chronograf --influxdb-url=http://bofh.lbl.gov:8086 

db query doesn't work yet

strangely i can connect to port 8888, ufw somehow not blocking it !!
cuz docker setup the network using iptables, so it allows where can connect, no longer limited by my ufw rules!!
docker overlay network uses 172....

Docker deamon adds DOCKER chain to `*filter` and `*nat`
ufw or iptables reset will break them!!
but Docker does not change INPUT rules.  thus my ufw should still block access
restarting it may have been bad.  ufw update may require all docker container to be restarted...
https://serverfault.com/questions/714276/bind-docker-container-ports-only-to-specific-outside-server-address





not sure if still need to mount persistent volume
    -v ...:/var/lib/chronograf



=============================================================
telegraf
=============================================================

Time-Series Data Collector
Also see netdata, collectd.

	TODO: 
	check ufw, ensure bofh can connect to itself.
	why cece7 can connect from home IP and not on same host??
	see the telegraf.M2.conf

**^ ^** 
**compose.M2** docker run --rm \
  --name t_pod \
      -v /home/tin/tin-gh/inet-dev-class/tig/conf/telegraf.M2.conf:/etc/telegraf/telegraf.conf:ro \
      -v /opt/tigM2/telegraf:/var/lib/telegraf \
      -v /var/run/docker.sock:/var/run/docker.sock \
      -v /var/run/utmp:/var/run/utmp:ro  \
      -v /sys:/rootfs/sys:ro  \
      -v /proc:/rootfs/proc:ro  \
      -v /etc:/rootfs/etc:ro  \
  telegraf:1.5


**^ ^**   ##no need## docker exec -it t_pod bash 
**^ tin bofh ~ ^**>  docker logs t_pod
2018/09/10 00:32:26 I! Using config file: /etc/telegraf/telegraf.conf



	influx container i_pod, don't see new database (telegraf) :(

	> show databases
	name: databases
	name
	----
	db0
	_internal
	tin_dockerrun



**^ tin bofh /opt/tigM2/telegraf ^**>  tail -f telegraf.log
2018-09-10T01:06:48Z I! Database creation failed: Post http://128.3.10.10:8086/query?q=CREATE+DATABASE+%22telegraf%22: net/http: request canceled while waiting for connection (Client.Timeout exceeded while awaiting headers)
2018-09-10T01:06:48Z I! Starting Telegraf v1.5.3
2018-09-10T01:06:48Z I! Loaded outputs: influxdb
2018-09-10T01:06:48Z I! Loaded inputs: inputs.cpu inputs.diskio inputs.kernel inputs.mem
2018-09-10T01:06:48Z I! Tags enabled: host=59787d029f8c
2018-09-10T01:06:48Z I! Agent Config: Interval:10s, Quiet:false, Hostname:"59787d029f8c", Flush Interval:10s
2018-09-10T01:07:05Z E! InfluxDB Output Error: Post http://128.3.10.10:8086/write?db=telegraf: net/http: request canceled while waiting for connection (Client.Timeout exceeded while awaiting headers)
2018-09-10T01:07:05Z E! Error writing to output [influxdb]: Could not write to any InfluxDB server in cluster
2018-09-10T01:07:15Z E! InfluxDB Output Error: Post http://128.3.10.10:8086/write?db=telegraf: net/http: request canceled while waiting for connection (Client.Timeout exceeded while awaiting headers)






~~~~~

(this was before docker network create ... influxdbnet by me for chronograf)
docker network ls
docker network inspect cd52fd39c5b1


**^ tin bofh /opt/tigM2/telegraf ^**>  telnet 128.3.10.10 8086
Trying 128.3.10.10...
Connected to 128.3.10.10.
Escape character is '^]'.
GET /
HTTP/1.1 400 Bad Request
Content-Type: text/plain; charset=utf-8
Connection: close

400 Bad RequestConnection closed by foreign host.
**^ tin bofh /opt/tigM2/telegraf ^**>  curl http://128.3.10.10:8086
404 page not found



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





=============================================================
Grafana
=============================================================
Visualization tool
Needs lots of config to create graphs.
Alternative: Kapacitor.
NetData come with a nicely default visualization page already, but it does not save data for long term analysis/trending.

GF_PATHS_CONFIG /etc/grafana/grafana.ini
GF_PATHS_DATA   /var/lib/grafana                # most important for persistent storage
GF_PATHS_HOME   /usr/share/grafana
GF_PATHS_LOGS   /var/log/grafana                # map this so that can see what grafana may complain about (or docker logs?).




mkdir /opt/tig/grafana
mkdir /opt/tig/grafana/log # not created automatically? :(
chown -R 472 /opt/tig/grafana  # Grafana 5.1+   (prior use uid 104)
# telegraf had similar uid problem.

**^ ^** 
docker run --rm \
  --name g_pod \
      -e "GF_PATHS_LOGS=/var/lib/grafana/log" \
      -v /opt/tig/grafana/:/var/lib/grafana \
      -p 3000:3000 \
   grafana/grafana:5.1.5

      #-v /opt/tig/grafana/logs:/var/log/grafana \
      #-v /opt/tig/grafana/plugins:/var/lib/grafana/plugins \



when saving datasource, still get gateway timeout.
probably got saved, but can't talk.
is the 73... the ip it is using to go out?
not likely... 
docker net ls ??? 


t=2018-09-11T06:54:53+0000 lvl=info msg="Request Completed" logger=context userId=0 orgId=0 uname= method=GET path=/ status=302 remote_addr=73.170.217.126 time_ms=0 size=29 referer=

=============================================================
container tool for troubleshooting
=============================================================


maybe vanilla centos 7 has enough troubleshooting tools:

docker run -it  --rm   centos:7 bash
docker run -it  --rm   tin6150/apache_psg3 bash

seems like need to put the tools there myself :(

::

	mkdir c7tools
	vi c7tools/dockerfile 
	docker build      -t tin6150/satools    . 
	#docker run -it --rm  bofh/c7tools:v7 
	docker push  tin6150/c7tools # optional push to dockerhub... 
	docker push  tin6150/satools # decided to change name :)
	# the "upload path" of docker push depends on the tags in the build, not the dir path where dockerfile resides.


ref: https://tin6150.github.io/psg/docker.html#dockerfile


=============================================================
netdata
=============================================================

**early test, no longer needed, see below** 
    docker run --rm -d --cap-add SYS_PTRACE \
           -v /proc:/host/proc:ro \
           -v /sys:/host/sys:ro \
           --name n_stock -p 19999:19999 \
           titpetric/netdata 

Open a browser on http://server:19999/ and watch how your server is doing.

dashboard shows right away, no config needed.
probably not storing any data for long term... 

netdata can send data to say influx backend.  see 
https://github.com/firehol/netdata/wiki/netdata-backends

- netdata collects a lot of data, multiple hosts can flood server quickly.
- use average, probably a good start  (def is 10 sec?)


port 19998 in version below use mapped .conf file to send backend data to influxdb.
first port of mapping is the host, 2nd is inside the container.
netdata.conf is generated automatically by netdata, it is huge.  only specifying a small number of clauses to configure backend to use influxdb

**compose.M2** docker run --rm -d \ 
        --cap-add SYS_PTRACE \
           -v /home/tin/tin-gh/inet-dev-class/tig/conf/netdata.conf:/etc/netdata/netdata.conf \
           -v /proc:/host/proc:ro \
           -v /sys:/host/sys:ro \
           --name n_infx -p 19998:19999 \
           titpetric/netdata 








