
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


SECRET=$a51
TOKEN=$a51
cd MTS117


get list of tileset:
curl "https://api.mapbox.com/tilesets/v1/tin117?access_token=$TOKEN

get tileset's recipe:
