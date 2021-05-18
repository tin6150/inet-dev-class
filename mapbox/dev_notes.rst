

node_modules/ 
contain npm installed pacakges.
eg 
npm install geojson2ndjson

for converting regular geojson into newline delimited geojson, which is the tileset source format for mts

(but eventually I changed adjointCsv2ldGson.py to output geojson.ld directly and don't have a need for it.)

tippercanoe also has function to do such conversion

~~~~

mapboxTileService.rst has commands for uploading ldgson to mapbox tileset service.
	commands used to reprocess adjoint 2021.0413 data as 10m resolution tilesets
