https://grafana.com/dashboards/3938
may need to change data source...

$datasource
$rootdir.$server

are there ways to specify variables substitution in json or grafana?  
this thing is quite painful!


sed -i 's/\$datasource/
not sure with what... :(


- grafana.netdata_graphine.stock.json # stock
- grafana.netdata_graphine.json       # config to use influxdb on cueball (server name, not client).  testing...


doc page suggest to use some rewrite rules (to change hostname and stuff)
TBD


Configuration
Optional but recommended: deploy provided rewriting
Optional but recommended: Master-Slave Setup
Configure netdata to write to Graphite
Import Dashboard and select the appropriate values at the top variable list for: datasource, rootdir, server.   **!**
Adopt the dashboard's refresh interval to fit your needs.
Enjoy!
