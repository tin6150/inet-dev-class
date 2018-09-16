


=============================================================
influxDB
=============================================================

ref:
https://hub.docker.com/_/influxdb/

config: 
/etc/influxdb/influxdb.conf \

database (all permanent storage) goes to:
/var/lib/influxdb 


influx
influx -username 'sammy' -password 'sammy_admin'

influx cmd
---------------------------------------------------------------

#?  use db0
create user "tin" with password 'tintin168' with all privileges
create user "tin2" with password 'tintin168' with all privileges
create user "sammy" with password 'sammy_admin' with all privileges

**>** show users

**>**> create database tin_dockerrun
**>**> show databases

_internal  # special internal db of influxDB

use telegraf
show measurements
select count(*) from diskio

use _internal
show measurements
	name: measurements
	name
	----
	cq
	database
	httpd
	queryExecutor
	runtime
	shard
	subscriber
	tsm1_cache
	tsm1_engine
	tsm1_filestore
	tsm1_wal
	write

select count(*) from subscriber
	52325



some db and retention really seems gone from this instance :(
**>**> 
show retention policies on _internal
name    duration shardGroupDuration replicaN default
----    -------- ------------------ -------- -------
monitor 168h0m0s 24h0m0s            1        true




Query Template from Chronograf
SHOW MEASUREMENTS ON "db_name"
SHOW TAG KEYS ON "db_name" FROM "measurement_name"
SHOW TAG VALUES ON "db_name" FROM "measurement_name" WITH KEY = "tag_key"
CREATE RETENTION POLICY "rp_name" ON "db_name" DURATION 30d REPLICATION 1 DEFAULT


