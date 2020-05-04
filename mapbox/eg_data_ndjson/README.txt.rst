(this likely won't render well in rst, mostly code needing to be lined by character/column.  but using rst as highlight)

trying to learn ndjson
as it should make processing files in a more standard way rather than writting custom script
to generate csv files.


and download those files as example for practice.

would need to use them for covid19_care_capacity_map



example ndjson commands.  

Part 1: https://medium.com/@mbostock/command-line-cartography-part-1-897aa8f8ca2c


wget 'http://www2.census.gov/geo/tiger/GENZ2014/shp/cb_2014_06_tract_500k.zip' -o cb_2014_06_tract_500k.zip

unzip -o cb_2014_06_tract_500k.zip

shp2json cb_2014_06_tract_500k.shp -o ca.json

ca.json is a geojson, looks like this:
{"type":"FeatureCollection",
 "bbox":[-124.409591,32.534155999999996,-114.131211,42.009518],
 "features":[
     {"type":"Feature",
      "properties":{"STATEFP":"06","COUNTYFP":"001","TRACTCE":"400300","AFFGEOID":"1400000US06001400300","GEOID":"06001400300","NAME":"4003","LSAD":"CT","ALAND":1105329,"AWATER":0},
       "geometry":{"type":"Polygon","coordinates":[[[-122.264164,37.839997],[-122.26186,37.841353],[-122.257923,37.842605999999996],...


change map projection to ConicEqualArea (Albers?)

geoproject 'd3.geoConicEqualArea().parallels([34, 40.5]).rotate([120, 0]).fitSize([960, 960], d)' < ca.json > ca-albers.json
geoproject 'd3.geoConicEqualArea().parallels([34, 40.5]).rotate([120, 0]).fitSize([960, 960], d)' < stateData.geojson > stateData-albers.json  # works

input is above geojson
output is another geojson, but coordinate is different.  also notice "bbox" was dropped:

{"type":"FeatureCollection",
 "features":[
     {"type":"Feature",
      "properties":{"STATEFP":"06","COUNTYFP":"001","TRACTCE":"400300","AFFGEOID":"1400000US06001400300","GEOID":"06001400300","NAME":"4003","LSAD":"CT","ALAND":1105329,"AWATER":0},
      "geometry":{"type":"Polygon","coordinates":[[[224.3021507494117,425.1613296471837],...



convert geojson to svg:
geo2svg -w 960 -h 960 < ca-albers.json > ca-albers.svg



Part 2: https://medium.com/@mbostock/command-line-cartography-part-2-c3a82c5c0f3


**Step 1: geojson to ndjson**
To convert a GeoJSON feature collection to a newline-delimited stream of GeoJSON features, use ndjson-split:

ndjson-split 'd.features'  < ca-albers.json  > ca-albers.ndjson # **1** **geo2ndj**
        cat stateData-albers.json     | ndjson-split 'd.features' > stateData-albers.ndjson  # work 
        cat stateData.geojson         | ndjson-split 'd.features' > stateData.ndjson         # dont work :/
        cat stateData.geojson | json5 | ndjson-split 'd.features' > stateData.ndjson         # work, just that ndjson cant handle white space/newline! pff!

so, mainly stripping tailing , of json and convert to newline....
BUT, to form proper json, the "opener marker of geojson" is stripped.  ie, remove the first two line what were:

{"type":"FeatureCollection",
 "features":[

and result from the 3rd line are the items, which make sense.  (eg below, split into multiple lines so that i can read it):

{"type":"Feature",
 "properties":{"STATEFP":"06","COUNTYFP":"001","TRACTCE":"400300","AFFGEOID":"1400000US06001400300","GEOID":"06001400300","NAME":"4003","LSAD":"CT","ALAND":1105329,"AWATER":0},
 "geometry":{"type":"Polygon","coordinates":[[[224.3021507494117,425.1613296471837],[224.4889212459765,425.02853000146524],[224.8054892227229,424.90924473882023],[225.09157727394734,424.797926817982],[225.29373002719294,424.7042420166931],[225.65996339344974,424.52901179192713],[225.95108431320563,424.3385241647384],[225.912059937863,424.3983338513344],[225.81079279254033,424.6100213459463],[225.58249395352414,425.05059707011105],[225.35882837057437,425.47619464326226],[225.22516372508392,425.73538936106115],[224.86658222608307,425.5294755512],[224.63434603931907,425.4732297669584],[224.43926884491924,425.4361850983005],[224.44504485979195,425.3811563562076],[224.37116077415172,425.3749388649712],[224.17960589902756,425.397389513148],[224.3021507494117,425.1613296471837]]]},
 "id":"001400300"}
{"type":"Feature","properties":{"STATEFP":"06","COUNTYFP":"001",...


**Step 2: add key field**
add an id feature (think field key) to each entry (each line):

ndjson-map 'd.id = d.properties.GEOID.slice(2), d'  < ca-albers.ndjson  > ca-albers-id.ndjson # **2** **+key**
            ^^^^                               ^^
            new field to be added is named id
            the data is extracted from "properties:{... GEOID"
            slice(2) likekly is substring( position 2 onward )
# intput line again:           #                                                                                      VVVVV-------here                                                           #
{"type":"Feature","properties":{"STATEFP":"06","COUNTYFP":"001","TRACTCE":"400300","AFFGEOID":"1400000US06001400300","GEOID":"06001400300","NAME":"4003","LSAD":"CT","ALAND":1105329,"AWATER":0},"geometry":{"type":"Polygon","coordinates":[[[224.3021507494117,425.1613296471837],[224.4889212459765,425.02853000146524],[224.8054892227229,424.90924473882023],[225.09157727394734,424.797926817982],[225.29373002719294,424.7042420166931],[225.65996339344974,424.52901179192713],[225.95108431320563,424.3385241647384],[225.912059937863,424.3983338513344],[225.81079279254033,424.6100213459463],[225.58249395352414,425.05059707011105],[225.35882837057437,425.47619464326226],[225.22516372508392,425.73538936106115],[224.86658222608307,425.5294755512],[224.63434603931907,425.4732297669584],[224.43926884491924,425.4361850983005],[224.44504485979195,425.3811563562076],[224.37116077415172,425.3749388649712],[224.17960589902756,425.397389513148],[224.3021507494117,425.1613296471837]]]}}


result is essentially the same, each line ends like this below.  All of the orig line is printed, with id added at the end, at the same level as type/properties/geometry:

...[224.3021507494117,425.1613296471837]]]},"id":"001400300"}
                                           ^^^^^^^|^^^^^^^^^----<<< new addition.
                                                06001400300
                                                  +-----------<<< slice(2) is likely like a substring, taking char 2 onward (0th index?)


download population from census.  should be this command, but didn't work.  there were some discussion about api id

wget 'http://api.census.gov/data/2014/acs5?get=B01003_001E&for=tract:*&in=state:06' -o cb_2014_06_tract_B01003.json

cb_2014_06_tract_B01003.json is a JSON array.  could not download, so just hand creating a couple of entry modeled after the screenshot.

[["B01003_001E","state","county","tract"],
["3385","06","001","400100"],
["3000","06","001","400200"],


**step 3**
The resulting file is a JSON array. To convert it to an NDJSON stream, use 
* ndjson-cat (to remove the newlines), 
* ndjson-split (to separate the array into multiple lines) and 
* ndjson-map (to reformat each line as an object) 
- B01003_001E is the key for population estimate

ndjson-cat cb_2014_06_tract_B01003.json            | ndjson-split 'd.slice(1)'  | ndjson-map '{id: d[2] + d[3], B01003: +d[0]}'  > cb_2014_06_tract_B01003.ndjson
ndjson-cat cb_2014_06_tract_B01003.tin_manual.json | ndjson-split 'd.slice(1)'  | ndjson-map '{id: d[2] + d[3], B01003: +d[0]}'  > cb_2014_06_tract_B01003.ndjson # **3**

which result in file looking like this:

{"id":"001400100","B01003":3385}
{"id":"001400200","B01003":3000}




**Step 4: join**
Now, magic! Join the population data to the geometry using ndjson-join:

ndjson-join 'd.id'  ca-albers-id.ndjson  cb_2014_06_tract_B01003.ndjson  > ca-albers-join.ndjson # **4** **join**
                      |||                           ^^^--- {"id":...}                       
                      ...]]]},"id":"001400300"}

a field named "id" exist on both file, so join is by explicit field name, easy enough.
Note the shape/geometry is on the first item d[0], while information desired for the map is on the second item d[1]


example result (originally in a single line):
[{"type":"Feature",
  "properties":{"STATEFP":"06","COUNTYFP":"001","TRACTCE":"400200","AFFGEOID":"1400000US06001400200","GEOID":"06001400200","NAME":"4002","LSAD":"CT","ALAND":587453,"AWATER":0},
  "geometry":{"type":"Polygon","coordinates":[[[224.8468880310794,424.86063151200733], ...  [224.8468880310794,424.86063151200733]]]},
  "id":"001400200"},    // end   of d[0]
 {"id":"001400200",     // start of d[1]
  "B01003":3000}          
]

It may be hard to see in the screenshot, but each line in the resulting NDJSON stream is a two-element array. 
* The first element (d[0]) is from ca-albers-id.ndjson: a GeoJSON Feature representing a census tract polygon. 
* The second element (d[1]) is from cb_2014_06_tract_B01003.ndjson: an object representing the population estimate for the same census tract.
* since it is two element array, each entry is wrapped with [ ].

**Step 5: re-map/restructure**
To compute the population density using ndjson-map, and to remove the additional properties we no longer need:
* some math was done to create density, converting units on the way.  

ndjson-map 'd[0].properties = {density: Math.floor(d[1].B01003 / d[0].properties.ALAND * 2589975.2356)}, d[0]'  < ca-albers-join.ndjson  > ca-albers-density.ndjson  # **5** **re-map/restructure**
                              ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^  vvvv
            def new prop as:  the properties field got mapped/replaced by a single density field.        \+++---- 

result is below.  Note:
- properties now only have density, rest of the stuff stripped.  
- there is still a tailing id field after geometry, but it is no longer a d[1] like before (ie, not at same level as (?property?)
- outermost [ ] has been stripped!

{"type":"Feature",
 "properties":{"density":1271},     // rest of fields inside property {} dropped.
 "geometry":{"type":"Polygon","coordinates":[[[225.78448190453653,420.5969486666927],[226.16999566793743,420.96146665947435],[226.4353743202891,420.8262305437552],[227.0435109343402,421.0430112662498],[227.60162914715443,421.35968917847185],[227.79368079351016,421.66795781610017],[228.10358341413718,422.03971187751495],[228.18429031174105,422.3353438365616],[227.9492345357079,422.4913940675069],[227.7603476189215,422.709657233876],[227.8464272831202,422.77230577293994],[228.28488422579164,423.2802694112406],[228.4029946455624,423.4762599002197],[228.4671021897194,423.51490468836937],[228.3682635536222,423.6398327507818],[228.1177255118626,423.6115068800532],[227.91336265873127,423.4519570947591],[227.91560198258557,423.2814509959426],[227.78118790546952,423.20734637243413],[227.65278999008922,423.4475726822302],[227.72763251990452,423.69428383640025],[227.58052940292242,423.7091559803025],[227.52942794659128,423.86333274239223],[227.56487795225692,424.0061786892675],[227.51148880348578,424.1219386837456],[227.30576347231454,424.22379677756226],[226.94607949082956,424.1265671904739],[226.72767076239282,423.9514709792952],[226.71968773230475,423.948752276458],[226.68633496533795,423.4168536461566],[226.13133024332436,423.45861132498203],[226.08187361311477,423.42079911786414],[225.9136826045701,423.2630619409483],[225.95266111609692,423.0972716892352],[225.84422691328982,422.7647192999211],[225.9114812192646,422.5889708679274],[225.863788172538,422.567799325785],[225.9011857050594,422.53933062786473],[225.88726595634404,422.1886710527401],[225.81261372317394,421.0262903359594],[225.7882126691558,420.7318646942922],[225.78448190453653,420.5969486666927]]]},
 "id":"001400100"}     // this id field was originally as part of d[0] (at the end)




To convert back to GeoJSON, use ndjson-reduce and ndjson-map:

ndjson-reduce  < ca-albers-density.ndjson    | ndjson-map '{type: "FeatureCollection", features: d}'  > ca-albers-density.json     # or below, easier to read
cat ca-albers-density.ndjson | ndjson-reduce | ndjson-map '{type: "FeatureCollection", features: d}'  > ca-albers-density.json     # **6a** **ndj2geo**
                                                           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^|^---<<<--- re-add the opener needed to create geojson

	opinion gratuita:
	as used above, the ndjson-reduce just convert from ndjson back to bad old json.  
	ie, it simply add a [ ] wrapper around the whole file, convert newline to comma, and the whole thing is one long ass ugly line.
	maybe better called ndjson2json !

	the ndjson-map add the header and wrap the json in more nesting to create geojson.
	the "d" in there maybe the key for the whole ndjson entries to be added.
	the [ ] that create array to be the list ofe entries is added by the ndjson reduce function, no need to spell that out here..


Or, using ndjson-reduce alone:   
ndjson-reduce 'p.features.push(d), p' '{type: "FeatureCollection", features: []}'  < ca-albers-density.ndjson  > ca-albers-density.alt.json # **6b**  **ndj2geo** ndjson-reduce method, i like this better**
                                   |   ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^||^-------<<<--- re-add the opener needed to create geojson
                                   more cler of where ndjson data get shoved into



Also see https://github.com/tin6150/covid19_care_capacity_map
README there used these steps to create covid19 care capacity map

