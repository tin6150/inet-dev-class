

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




part 2 - join shape with pop data by id
======

https://medium.com/@mbostock/command-line-cartography-part-2-c3a82c5c0f3

# xref: inet-dev-class/mapbox/eg_data_ndjson/README.txt.rst , which likely also in covid19_care_capacity_map/
# **eg 2a**  geojson to ndjson
ndjson-split 'd.features' < ca-albers.json  > ca-albers.ndjson

ndjson-map 'd.id = d.properties.GEOID.slice(2), d'  < ca-albers.ndjson  > ca-albers-id.ndjson


# census api to get pop 
# need census api key, see bmail.


B01003_001E	Estimate!!Total	TOTAL POPULATION	not required	B01003_001EA, B01003_001M, B01003_001MA	0	int

XX curl 'https://api.census.gov/data/2014/acs5?get=B01003_001EA&for=tract:*&in=state:06' -o cb_2014_06_tract_B01003.json # track pop ?
slightly changed api

Example Call:    http://api.census.gov/data/2014/acs/acs5/profile?get=DP02_0001PE&for=state:*&key=... (See notes)
many examples : https://api.census.gov/data/2014/acs/acs5/examples.html
                https://api.census.gov/data/2014/acs/acs5?get=NAME,B00001_001E&for=tract:*&in=state:01&key=YOUR_KEY_GOES_HERE

			  export ApiKey=c9b728... see bmail or . .env , also in .ssh
curl "https://api.census.gov/data/2014/acs/acs5?get=NAME,B01003_001E&for=tract:*&in=state:06&key=$ApiKey" -o cb_2014_06_tract_B01003.json # track pop 
curl "https://api.census.gov/data/2018/acs/acs5?get=NAME,B01003_001E&for=tract:*&in=state:06&key=$ApiKey" -o cb_2018_06_tract_B01003.json # track pop 2018

works! but result now has extra descriptive fields in them...
cat cb_2014_06_tract_B01003.json | wc
cat cb_2014_06_tract_B01003.json | json2csv > cb_2014_06_tract_B01003.json.csv 

[["NAME","B01003_001E","state","county","tract"],
["Census Tract 4382.03, Alameda County, California","4384","06","001","438203"],
["Census Tract 4382.04, Alameda County, California","5338","06","001","438204"],
  ^^extra 1^^           ^^extra 2^^^^^  ^^extra 3^^  ^#0^  ^#1  ^#2^   ^^#3^^
 ^^^^^^single^^field^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
#1, ... #3 are the orig field bostock eg refers to.  so i am no off by +1 

# **eg 2d** 

ndjson-cat cb_2014_06_tract_B01003.json \
  | ndjson-split 'd.slice(1)' \
  | ndjson-map '{id: d[2] + d[3], B01003: +d[0]}'  >        cb_2014_06_tract_B01003.ndjson
#                    ^^^^^1^^^^^          ^^^2^^
#   field 1 is combination of 2 column, 2 and 3, merged, no space.  0-idx
#   field 2 is column 0
#   ndjson has key: value pair, field 1 key is "id: ', field 2 key is "B01003: '

# **fiexed 2d** 
ndjson-cat cb_2014_06_tract_B01003.json \
  | ndjson-split 'd.slice(1)' \
  | ndjson-map '{id: d[3] + d[4], B01003: +d[1]}'  >        cb_2014_06_tract_B01003.ndjson
#                    ^^^^^1^^^^^          ^^^2^^
# should have been off by +1 in the new json retrieved via new census api...

# result is this, which looks like what bostock expect
{"id":"001438203","B01003":4384}
{"id":"001438204","B01003":5338}
{"id":"001438300","B01003":4133}


# json2csv cannot handle ndjson
# use vscode data preview extension to help viz file, using head -4 or so...

# **eg 2e** 

ndjson-join 'd.id' \
  ca-albers-id.ndjson \
  cb_2014_06_tract_B01003.ndjson \
  > ca-albers-join.ndjson

# **$** it is borked here.  fixed now




ndjson-map 'd[0].properties = {density: Math.floor(d[1].B01003 / d[0].properties.ALAND * 2589975.2356)}, d[0]' \
  < ca-albers-join.ndjson \
  > ca-albers-density.ndjson


ndjson-reduce \
  < ca-albers-density.ndjson \
  | ndjson-map '{type: "FeatureCollection", features: d}' \
  > ca-albers-density.json


ndjson-map -r d3 \
  '(d.properties.fill = d3.scaleSequential(d3.interpolateViridis).domain([0, 4000])(d.properties.density), d)' \
  < ca-albers-density.ndjson \
  > ca-albers-color.ndjson

geo2svg -n --stroke none -p 1 -w 960 -h 960 \
  < ca-albers-color.ndjson \
  > ca-albers-color.svg


xviewer ca-albers-color.svg


.. # use 8-space tab as that's how github render the rst
.. # vim: shiftwidth=8 tabstop=8 noexpandtab paste

