
mts - mapbox tileset service
============================

new api (in beta still in 2021.05) for uploading tileset source 
for processing and storage in mapbox server.

this new method use a recipe file to specify resolution
which affect pricing.
old method defaulted to 1m (meter) resolution
for adjoint data covered too much space and 10m res is needed to remain in free tier.


intro guide:
https://docs.mapbox.com/mapbox-tiling-service/guides/

API: 
https://docs.mapbox.com/api/maps/mapbox-tiling-service/#update-a-tilesets-recipe


actually many are usable as curl calls, eg:

HISTCONTROL=ignorespace
  SECRET=$a51
  TOKEN=$a51   # ensure there is no space in token!

cd MTS117

get list of tileset:
curl "https://api.mapbox.com/tilesets/v1/tin117?access_token=$TOKEN" | tee tileset_list.json

this is shared with Mikal Maron, seems like good example with lots of color showing simulatio area coverage, 
first tileset to rework into 10m resolution.
tin117.o3gt70sjvNOxMxDaySp
tin117.dacsjvnewNOxMxNitSp lower case dac no dash also used by adjoint2021


Creating/Uploading new data
https://docs.mapbox.com/mapbox-tiling-service/guides/#create-a-new-tileset-with-mts
1. convert to line-delimited geojson  (.geojsonl or .geojson.ld ?)
2. create tileset source
3. create tileset recipe - create a json file with resolution, maxzoom, etc.
4. create tileset  - upload to mapbox
5. publish tileset - trigger job to create vector tiles  - cost significant money

there is storage cost, think that's after the conversion step (and not stuff uploaded in step 4).


tools
=====

- npm install geojson2ndjson
- https://stevage.github.io/ndgeojson/
- I can likely generate geojson.ld from csv easier than geojson!  since it doesn't need that stupid wrapper 
  "type": "FeatureCollection", "features"
- yeap, now should use batchCsv2ldGson.sh / adjointCsv2ldGson.py


create tileset source
---------------------

trying api route first, since lazy with installing another sdk
ref: https://docs.mapbox.com/api/maps/mapbox-tiling-service/#create-a-tileset-source

# This endpoint requires a token with tilesets:write scope.


cat o3gt70sjvNOxMxDaySp.geojson | ~/node_modules/geojson2ndjson/geojson2ndjson.js  > o3gt70sjvNOxMxDaySp.geojson.ld
        above has missing "id" field and thus rejected by mapbox  **++**
        i guess may as well update csv2geojson script to csv2ldgeojson directly...
cat o3gt70sjvNOxMxDaySp.geojson.ld | ~/node_modules/geojson2ndjson/geojson2ndjson.js  > o3gt70sjvNOxMxDaySp_h2.geojson.ld

cd ~/tin-gh/inet-dev-class/mapbox/DATA_adjoin_0413 # luna
#File=o3gt70sjvNOxMxDaySp_h3
File=o3gt70sjvNOxMxDaySp
Name=$File   # tile source name, can have up to 10 ource files # currently empty
curl -X POST "https://api.mapbox.com/tilesets/v1/sources/tin117/$Name?access_token=$TOKEN" \
    -F file=@${File}.geojson.ld \
    --header "Content-Type: multipart/form-data"

## got output: {"id":"mapbox://tileset-source/tin117/o3gt70sjvNOxMxDaySp","files":1,"source_size":5702002,"file_size":5702002}


the Tileset CLI toolkit (github) does this conversion automatically, so good reason to use it (installed to lunaria) ref: https://docs.mapbox.com/help/tutorials/get-started-mts-and-tilesets-cli/#create-a-tileset-source

	source venv4mapbox/bin/activate
	pip install mapbox-tilesets
	didn't work... problem with pyrsistent... will try ndjson stuff... 



list existing tileset source (stored in mapbox.com)
curl "https://api.mapbox.com/tilesets/v1/sources/tin117?access_token=$TOKEN"



get tileset's recipe
--------------------

# curl "https://api.mapbox.com/tilesets/v1/{tileset}/recipe?access_token=$TOKEN"
# This endpoint requires a token with tilesets:list scope.

tileset=tin117.o3gt70sjvNOxMxDaySp
curl "https://api.mapbox.com/tilesets/v1/${tileset}/recipe?access_token=$TOKEN"
# no recipe for tilesetup uploaded using old mapbox python sdk

validate recipe
---------------

ref: https://docs.mapbox.com/api/maps/mapbox-tiling-service/#validate-a-recipe

curl -X PUT "https://api.mapbox.com/tilesets/v1/validateRecipe?access_token=$TOKEN" \
  -d @recipe.json \
  --header "Content-Type:application/json"


create tileset 
--------------

(think of upload tileset)

this is like uploading source data to mapbox, a prep step (later need conversion into mapbox tileset using PUBLISH)
ref: https://docs.mapbox.com/api/maps/mapbox-tiling-service/#create-a-tileset
need a recipe, so create and validate that first 

curl -X POST "https://api.mapbox.com/tilesets/v1/{tileset}?access_token=YOUR MAPBOX ACCESS TOKEN" \
  -d @tileset-recipe.json \
  --header "Content-Type:application/json"

contrast this curl API method vs Tileset CLI 
https://docs.mapbox.com/help/tutorials/get-started-mts-and-tilesets-cli/
	Tileset CLI has: 
	- estimate area size
	- overwrite existing data
	- need to install some sdk (github)
	- output/result probably more human readable than API/curl, which is likely json.
 

publish tileset
---------------

publish actually convert the "created tileset" into vectors, this is the step that has processing charges from mapbox web service.

ref: https://docs.mapbox.com/api/maps/mapbox-tiling-service/#publish-a-tileset


~~~~




Future tasks
------------

remove unused tileset.  Adjoin 2019-2020 data no longer needed, should have been named like 
DAC-topo3AvAVOCSpAl
likely tin.117-DAC-* can be removed.  check older html code for name used if need be.
(But these are likely using the old method with no specific resolution attached, so not in current charge model?)
data might still be useful for comparison for Ling's old poster data, which is for a specific receptor area... , eg https://mail.google.com/mail/u/1/?zx=eshqnmfwg3mp#search/adjoin/FMfcgxwGCtHpRJJCcRmWqgsWrgLMBjWTo
	overall, that version of "adjoin " probably should have a release label on it for future ref... (if can afford to keep the data)
to delete via API/cure, use something like 
curl -X DELETE ... 
