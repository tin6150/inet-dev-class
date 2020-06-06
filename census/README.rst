

2020.0605

playing with census data.

Ling is interested to see if can get pop at census tract vs block level.  
preferably density, so need aland 

ref:
https://medium.com/@mbostock/command-line-cartography-part-4-82d0d26df0cf
https://blog.mapbox.com/dive-into-large-datasets-with-3d-shapes-in-mapbox-gl-c89023ef291

maybe tidycensus in R
maybe mapbox
tbd


~~~~

part 1 - census shape to svg
======

https://medium.com/@mbostock/command-line-cartography-part-1-897aa8f8ca2c


TIGER = very detailed.
SHAPE file - much smaller, good for thematic maps (cartographically small scale)

need pop data matching shape: tract vs block

CA FIPS code = 06.
download data:

mkdir TMP_DATA
cd    TMP_DATA

curl 'https://www2.census.gov/geo/tiger/GENZ2014/shp/cb_2014_06_tract_500k.zip' -o cb_2014_06_tract_500k.zip  # shape + dbIII
unzip ...

shp2json cb_2014_06_tract_500k.shp -o ca.json
geoproject 'd3.geoConicEqualArea().parallels([34, 40.5]).rotate([120, 0]).fitSize([960, 960], d)' < ca.json > ca-albers.json
geo2svg -w 960 -h 960 < ca-albers.json > ca-albers.svg




part 2 - 
======

https://medium.com/@mbostock/command-line-cartography-part-2-c3a82c5c0f3

ndjson-split 'd.features' \
  < ca-albers.json \
  > ca-albers.ndjson


ndjson-map 'd.id = d.properties.GEOID.slice(2), d' \
  < ca-albers.ndjson \
  > ca-albers-id.ndjson


# census api to get pop 
# need census api key, see bmail.


B01003_001E	Estimate!!Total	TOTAL POPULATION	not required	B01003_001EA, B01003_001M, B01003_001MA	0	int

XX curl 'https://api.census.gov/data/2014/acs5?get=B01003_001EA&for=tract:*&in=state:06' -o cb_2014_06_tract_B01003.json # track pop ?
slightly changed api

Example Call: http://api.census.gov/data/2014/acs/acs5/profile?get=DP02_0001PE&for=state:*&key=... (See notes)

many examples : https://api.census.gov/data/2014/acs/acs5/examples.html

https://api.census.gov/data/2014/acs/acs5?get=NAME,B00001_001E&for=tract:*&in=state:01&key=YOUR_KEY_GOES_HERE


			  export ApiKey=c9b728... see bmail
curl "https://api.census.gov/data/2014/acs/acs5?get=NAME,B01003_001E&for=tract:*&in=state:06&key=$ApiKey" -o cb_2014_06_tract_B01003.json # track pop ?

works! 
cat cb_2014_06_tract_B01003.json | wc
