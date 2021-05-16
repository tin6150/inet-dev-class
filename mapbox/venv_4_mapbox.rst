

toolkit for uploading tiles

installed as virtual env on lunaria 2021.04,  Zink/Domingo 2021.0516

sudo apt install python3-venv


python3 -m venv ./venv4mapbox
source venv4mapbox/bin/activate

# pip install -r requirements.txt

# domingo just did

pip install mapbox-tilesets



requirements.txt had 
mapboxcli

changed to have 
mapbox-tilesets

(Lunaria, Zink, Domingo could not get this installed cuz error with pyrsistent, so this is the new mapbox-tilesets req, not old mapboxcli 

so stuck at the moment, can't get this installed.
was needed to do upload so it converts geojson to geojson.ld, will look at old ndjson thing to see if can convert manually...)



