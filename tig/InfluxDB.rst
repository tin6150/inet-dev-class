


=============================================================
influxDB
=============================================================

101
--------------------------------------------------------------------------------

InfluxDB is a time series database.
Essentially, it stores a lot of data points.  Each data point is a measurement.

measurements eg cpu-load, temperature
each of the measurement would be a "table" in SQL parlance

each data point key is the timestamp.
each data point have additional data (stored as "columns").  
- tags are indexed (eg hostname/cpu#).  
- fields are not (eg the actual value of cpu-load measurement)


Ref: https://docs.influxdata.com/influxdb/v1.6/introduction/getting-started/

data format
--------------------------------------------------------------------------------

<measurement>[,<tag-key>=<tag-value>...] <field-key>=<field-value>[,<field2-key>=<field2-value>...] [unix-nano-timestamp]
                                        ^---- note the space separating tag vs field               ^---- timestamp space
eg
cpu,host=serverA,region=us_west value=0.64
    ^^^tag       ^^^tag        ^--- space for field
temperature,machine=unit42,type=assembly external=25,internal=37 1434067467000000000
  ^^^measurement                        ^-- field               ^--- timestamp




=============================================================
SysAdmin Setup/config
=============================================================


ref:
https://hub.docker.com/_/influxdb/

config: 
/etc/influxdb/influxdb.conf \

database (all permanent storage) goes to:
/var/lib/influxdb 


influx
influx -username 'sammy' -password 'sammy_admin'



=============================================================
DBA cmd
=============================================================

eg adding example data point
--------------------------------------------------------------------------------

create database mydb
use mydb
INSERT cpu,host=svrA,loc=CA value=0.88
INSERT cpu,host=svrA,loc=CA cpu1=0.10,cpu2=0.20
# timestamp is added by server when not specified, but there are internal marking that it was not "written".


SHOW measruements             # think of this as list all tables


select * from cpu
	name: cpu
	time                cpu1 cpu2 host loc value
	----                ---- ---- ---- --- -----
	1537139481253530800           svrA CA  0.88
	1537139786867579372 0.1  0.2  svrA CA

# best way to see "table" structure (since no "describe")
# also repeated use can see if data is being added to it
select COUNT(*) from cpu
	name: cpu
	time count_cpu1 count_cpu2 count_value
	---- ---------- ---------- -----------
	0    1          1          4

# good way to take peek at data
select * from cpu LIMIT 10



Query Template from Chronograf
SHOW MEASUREMENTS ON "db_name"
SHOW TAG KEYS ON "db_name" FROM "measurement_name"
SHOW TAG VALUES ON "db_name" FROM "measurement_name" WITH KEY = "tag_key"
CREATE RETENTION POLICY "rp_name" ON "db_name" DURATION 30d REPLICATION 1 DEFAULT


SHOW TAG KEYS   ON "telegraf" FROM "cpu"
SHOW TAG VALUES ON "telegraf" FROM "cpu" WITH KEY = "host"
                ^^^db name^^^


Go-style regex supported for queries.


curl-ing the influx db
--------------------------------------------------------------------------------

ref: https://docs.influxdata.com/influxdb/v1.6/guides/writing_data/

curl -i -XPOST http://bofh.lbl.gov:8086/query --data-urlencode "q=show databases"
# equiv of influx "show databases"

curl -i -XPOST http://bofh.lbl.gov:8086/query --data-urlencode "q=show measurements on mydb"
# equiv of "show measurements on mydb" issued at influx cli

# same req using port 2003 (graphite) just hangs
# same req using port 4242 (opensmdb) returns error 404
# same req using port 8089 (udp) returns error 

curl -i -XPOST http://bofh.lbl.gov:8086/query --data-urlencode "q=CREATE DATABASE mydb2"
# create a DB called "mydb2"
# use the query end point
# influx has 3 end ponits, HTTP protocol, does not claim to be REST compliant

curl -i -XPOST http://bofh.lbl.gov:4242/query --data-urlencode "q=CREATE DATABASE mydb3"

curl -i -XPOST 'http://bofh.lbl.gov:8086/write?db=mydb2' --data-binary 'cpu_load_short,host=server01,region=us-west value=0.64 1434055562000000000'
# return code of 204 No Content is actually success!  (wrote to DB, just that nothing is retruend).

curl -i -XPOST 'http://bofh.lbl.gov:4242/write?db=mydb2' --data-binary 'cpu_load_short,host=server02,region=us-west,method=opentsdb value=0.65'
# return code of 404 is truly error in writting







influx cmd for influx, general
--------------------------------------------------------------------------------

#?  use db0
create user "tin" with password 'tintin168' with all privileges
create user "tin2" with password 'tintin168' with all privileges
create user "sammy" with password 'sammy_admin' with all privileges

**>** show users

**>**> create database tin_dockerrun
**>**> show databases

_internal  # special internal db of influxDB

show measurements ON telegraf 
# -or-
use telegraf
show measurements

### not sure if some of telegraf etc wrote to the _internal db

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





influx cmd for telegraf
--------------------------------------------------------------------------------


select count(*) from diskio
select count(*) from cpu,diskio  # produce a strange merge 

select count(*) from kernel

,mem,swap,system


> select * from cpu limit 10
name: cpu
time                cpu       host  usage_guest usage_guest_nice usage_idle        usage_iowait        usage_irq usage_nice usage_softirq usage_steal usage_system        usage_user
----                ---       ----  ----------- ---------------- ----------        ------------        --------- ---------- ------------- ----------- ------------        ----------
1536556270000000000 cpu-total cece7 0           0                98.44533600801769 0.02507522567700536 0         0          0             0           0.5265797392176115  1.0030090270813548


# count(*) omits the cpu and host column!!
> select count(*) from cpu
	name: cpu
	time count_usage_guest count_usage_guest_nice count_usage_idle count_usage_iowait count_usage_irq count_usage_nice count_usage_softirq count_usage_steal count_usage_system count_usage_user
	---- ----------------- ---------------------- ---------------- ------------------ --------------- ---------------- ------------------- ----------------- ------------------ ----------------
	0    524925            524925                 524925           524925             524925          524925           524925              524925            524925             524925


select * from cpu LIMIT 10
# note that telegraf write data from all hosts into the same table of the same measurement type.



select distinct(host) from cpu;             ## does NOT work.  distint() is for fields only
select count(*) from cpu group by host;



influx cmd for netdata (via graphite)
--------------------------------------------------------------------------------

probably not working yet

> show measurements
name: measurements
name
----
Upgrade-Insecure-Requests:
>



