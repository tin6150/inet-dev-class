

# script to setup one time commands for the TIG stack used by Grafana
# "mode 3".  
# don't think need to use default password, hopefully nothing is hard coded to use "default" passwords used in various web pages.

# passwords are currently in protonmaial: tig "M3"
# future may investigate docker secret or some such.
# https://www.famousscientists.org/list/

# -e INFLUXDB_ADMIN_USER=dba -e INFLUXDB_ADMIN_PASSWORD=$INFLUXDB_ADMIN_PASS \
##export INFLUXDB_ADMIN_PASS=I_999 # dba

# -e INFLUXDB_USER=telegraf -e INFLUXDB_USER_PASSWORD=$INFLUXDB_TELEGRAF_PASS \
##export INFLUXDB_TELEGRAF_PASS=...   # telegraf

# tba, grafana container, default is admin/admin
##export GRAFANA_APP_PASS=... # grafana  http://...:3000 web login



[[ -d /opt/tig/grafana ]] || sudo mkdir -p /opt/tig/grafana 
sudo chown -R 472 /opt/tig/grafana 
# the rest docker-compose likely create them
#mkdir /opt/tig
#mkdir /opt/tigM2


# influx one time initialization

docker run --rm \
      -e INFLUXDB_DB=db0 -e INFLUXDB_ADMIN_ENABLED=true \
      -e INFLUXDB_ADMIN_USER=dba -e INFLUXDB_ADMIN_PASSWORD=$INFLUXDB_ADMIN_PASS \
      -e INFLUXDB_USER=telegraf -e INFLUXDB_USER_PASSWORD=$INFLUXDB_TELEGRAF_PASS \
      -v /home/tin/tin-gh/inet-dev-class/tig/conf/influxdb.conf:/etc/influxdb/influxdb.conf \
      -v /opt/tigM2/influxdb:/var/lib/influxdb \
      --name i_pod \
      influxdb /init-influxdb.sh




