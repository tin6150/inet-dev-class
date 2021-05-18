
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

- https://stevage.github.io/ndgeojson/
- npm install geojson2ndjson
- no need for geojson2ndjson conversion now, use batchCsv2ldGson.sh / adjointCsv2ldGson.py
- cat ls-tielsetSource.json | jq        # much easier to read
- cat ls-tielsetSource.json | json2tsv  # like a compact csv


create tileset source
---------------------

trying api route first, since lazy with installing another sdk
ref: https://docs.mapbox.com/api/maps/mapbox-tiling-service/#create-a-tileset-source

cd ~/tin-gh/inet-dev-class/mapbox/DATA_adjoin_0413a # domingo
#File=o3gt70sjvNOxMxDaySp_h3
username=tin117
File=o3gt70sjvNOxMxDaySp
Name=$File   # tile source name, can have up to 10 ource files # currently empty
#// curl -X POST "https://api.mapbox.com/tilesets/v1/sources/$username/$Name?access_token=$TOKEN" \
    curl -X PUT  "https://api.mapbox.com/tilesets/v1/sources/$username/$Name?access_token=$TOKEN" \
    -F file=@${File}.geojson.ld \
    --header "Content-Type: multipart/form-data"

## got output:                  {"id":"mapbox://tileset-source/tin117/o3gt70sjvNOxMxDaySp","files":1,"source_size":5702002,"file_size":5702002}
## replace with smaller ldgson: {"id":"mapbox://tileset-source/tin117/o3gt70sjvNOxMxDaySp","files":1,"source_size":4517867,"file_size":4517867}

  -X POST = create/append tileset
  -X PUT  = create/replace tileset - so, maybe better to use PUT

even after replace (ie there is existing tileset recipe, have to run other commands to recreate tileset, probably a publish)

the Tileset CLI toolkit (github) does this conversion automatically, so good reason to use it (installed to lunaria) ref: https://docs.mapbox.com/help/tutorials/get-started-mts-and-tilesets-cli/#create-a-tileset-source
	source venv4mapbox/bin/activate
	pip install mapbox-tilesets
	didn't work... problem with pyrsistent... will try ndjson stuff... 



list existing tileset source (stored in mapbox.com) (like dir?)
curl "https://api.mapbox.com/tilesets/v1/sources/tin117?access_token=$TOKEN" | tee ls-tielsetSource.json
cat ls-tielsetSource.json | jq       # much easier to read
cat ls-tielsetSource.json | json2tsv # like compact csv, tab separated

	eg output:
	[{"id":"mapbox://tileset-source/tin117/o3gt70sjvNOxMxDaySp","size":5702002,"files":1},
     {"id":"mapbox://tileset-source/tin117/o3gt70sjvNOxMxDaySp_h3","size":1006,"files":1},
     {"id":"mapbox://tileset-source/tin117/mapbox_hello","size":467,"files":1}]

retrieve tileset source info (for a specific tileset?, like cat?)
uname=tin117
curl "https://api.mapbox.com/tilesets/v1/sources/tin117/$uname.$tileset?access_token=$TOKEN"
curl "https://api.mapbox.com/tilesets/v1/sources/tin117/mapbox_hello?access_token=$TOKEN"
curl "https://api.mapbox.com/tilesets/v1/sources/tin117/o3gt70sjvNOxMxDaySp?access_token=$TOKEN"


get tileset's recipe
--------------------

# curl "https://api.mapbox.com/tilesets/v1/{tileset}/recipe?access_token=$TOKEN"
# This endpoint requires a token with tilesets:list scope.

## this is pretty inconsistent, tileset here need username embeded in it?

tileset=o3gt70sjvNOxMxDaySp        # {"message":"Not Found"}
tileset=tin117.o3gt70sjvNOxMxDaySp # worked
curl "https://api.mapbox.com/tilesets/v1/${tileset}/recipe?access_token=$TOKEN"
# no recipe for tilesetup uploaded using old mapbox python sdk

validate recipe
---------------

ref: https://docs.mapbox.com/api/maps/mapbox-tiling-service/#validate-a-recipe

curl -X PUT "https://api.mapbox.com/tilesets/v1/validateRecipe?access_token=$TOKEN" \
  -d @o3gt70sjvNOxMxDaySp.json \
  --header "Content-Type:application/json"

resolution info is not explicityly defined, but embeded in zoom
https://www.mapbox.com/pricing/#tilesets 
10m is zoom  6-10
 1m is zoom 11-13

so, let's try a recipe with maxzoom 10
but recipe keep getting rejected.  API vs 

create tileset 
--------------

(think of upload tileset)

this is like uploading source data to mapbox, a prep step (later need conversion into mapbox tileset using PUBLISH)
ref: https://docs.mapbox.com/api/maps/mapbox-tiling-service/#create-a-tileset
need a recipe, so create and validate that first 

tileset=o3gt70sjvNOxMxDaySp
#-- curl -X POST "https://api.mapbox.com/tilesets/v1/${tileset}?access_token=$TOKEN" \
#-- this result in error "Not Found"

#++ below seems to be the right syntax.  should make a suggestion to the doc
curl -X POST "https://api.mapbox.com/tilesets/v1/tin117.${tileset}?access_token=$TOKEN" \
  -d @${tileset}.json \
  --header "Content-Type:application/json"

	# eg output
	{"message":"Successfully created empty tileset tin117.o3gt70sjvNOxMxDaySp. Publish your tileset to begin processing your data into vector tiles."}


get list of tileset:
curl "https://api.mapbox.com/tilesets/v1/tin117?access_token=$TOKEN" | tee tileset_list.json

delete a tileset

username=tin117
tileset=o3gt70sjvNOxMxDaySp
curl -X DELETE "https://api.mapbox.com/tilesets/v1/${username}.${tileset}?access_token=$TOKEN"


contrast this curl API method vs Tileset CLI 
https://docs.mapbox.com/help/tutorials/get-started-mts-and-tilesets-cli/
	Tileset CLI has: 
	- estimate area size
	- overwrite existing data
	- need to install some sdk (github), and i got some error and abandoned the install
	- output/result probably more human readable than API/curl, which is likely json.

 

publish tileset
---------------

publish actually convert the "created tileset" into vectors, this is the step that has processing charges from mapbox web service.

ref: https://docs.mapbox.com/api/maps/mapbox-tiling-service/#publish-a-tileset

username=tin117
tileset=o3gt70sjvNOxMxDaySp
#xx curl -X POST "https://api.mapbox.com/tilesets/v1/{tileset}/publish?access_token=$TOKEN"
curl -X POST "https://api.mapbox.com/tilesets/v1/$username.${tileset}/publish?access_token=$TOKEN"

	eg output from above, with $username
	{"message":"Processing tin117.o3gt70sjvNOxMxDaySp","jobId":"ckosble6i000008lccevs3drf"}
    {"message":"Processing tin117.o3gt70sjvNOxMxDaySp","jobId":"ckote6u5q000208l6e8tugmxx"} # resubmit processing smaller ldgson


get status of job for specific tileset
#xx curl "https://api.mapbox.com/tilesets/v1/${tileset}/jobs?access_token=$TOKEN"               # did not work
    curl "https://api.mapbox.com/tilesets/v1/${username}.${tileset}/jobs?access_token=$TOKEN"   # worked


    # [{"id":"ckosble6i000008lccevs3drf","stage":"success","created":1621238584842,"created_nice":"Mon May 17 2021 08:03:04 GMT+0000 ... 
data not showing up in stats dashboard yet 

    "tilesetId": "tin117.o3gt70sjvNOxMxDaySp",
    "errors": [],
    "warnings": [
      "W201: Features were dropped from o3gt70sjvNOxMxDaySp layer in 2 tile(s) to enforce tile size limits. Affected zoom levels are: 4,5"

no warnings for ckote6u5q000208l6e8tugmxx (2nd run with smaller ldgson)
++ TODO: should actually query for all job output to track results.
	

~~~~

notes
=====

- tileset created in studio is not covered in the tileset processing pricelist
  (so my big box around adjoint sim coverage was likely free and not cause of invoice.



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
