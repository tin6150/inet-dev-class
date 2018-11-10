
Mapbox Notes
============

learning
mapbox gl js 

as part of collab with Ling Jin of ETA.

from biositing_tools prj via Tyler Huntington



Ref
===

https://github.com/mapbox/mapbox-gl-js

Examples to try:


Part 1 of choropleth - Load map data into MapBox Studio as TileSet, create viz using "styles":
https://www.mapbox.com/help/choropleth-studio-gl-pt-1/

Part 0 - Leaflet.  Background on how geojson data was created: 
https://leafletjs.com/examples/choropleth/

Part 00 - Texas county map with voting result (maybe able to find leaflet or mapbox data for CA county map and not need convert Census TIGER data myself):
http://www.texastribune.org/library/data/us-senate-runoff-results-map/



Part 2 of choropleth - create web page using JavaScript, provides for interactivity: 
https://www.mapbox.com/help/choropleth-studio-gl-pt-2/


Blog on building net-neutrality map
https://blog.mapbox.com/the-net-neutrality-map-how-i-built-it-c387c9cb64a8

Shape file (from ESRI) import into Mapbox (Census TIGER data are provided as shape files)
https://www.mapbox.com/help/define-shapefile/


Examples
========

Loading example pages via web site provided by github.io 

- https://tin6150.github.io/inet-dev-class/mapbox/
  
- https://tin6150.github.io/inet-dev-class/mapbox/mapbox-gl-eg-circle-color.html
- https://tin6150.github.io/inet-dev-class/mapbox/mapbox-gl-eg-geojson-line.html
- https://tin6150.github.io/inet-dev-class/mapbox/mapbox-gl-test1.html
- https://tin6150.github.io/inet-dev-class/mapbox/mapbox-population-sn.html
- https://tin6150.github.io/inet-dev-class/mapbox/mapbox-population-tutorial-solution.html
- https://tin6150.github.io/inet-dev-class/mapbox/mapbox-population-tutorial.html






Mapbox data structure
=====================

* Tileset is basic store of vector data that will be rendered by Mapbox (studio) style.  not editable, just optimization intermediate internal format for mapbox.
* Dataset.  what user import as data.  vector or raster.
* (ESRI) Shape file are imported into Dataset.

* Mapbox studio create layers in the "style" for visualization and UI.
* Style can be access by URL by JavaScript (Mapbox GL JS) for web app.

* geojson, when imported in to MapBox Studio, is converted into vector tileset for efficient rendering.
* density coloring is done by layer styling in MapBox studio (ie web app), though there maybe something in JS that can set/ovewrite(?) this coloring.



Snipplet from stateData.geojson  
-------------------------------


{"type":"FeatureCollection","features":[

{"type":"Feature","id":"01","properties":{"name":"Alabama","density":94.65},"geometry":{"type":"Polygon","coordinates":[[[-87.359296,35.00118],[-85.606675,34.984749],[-85.431413,34.124869],[-85.184951,32.859696],[-85.069935,32.580372],[-84.960397,32.421541],[-85.004212,32.322956],[-84.889196,32.262709],[-85.058981,32.13674],[-85.053504,32.01077],[-85.141136,31.840985],[-85.042551,31.539753],[-85.113751,31.27686],[-85.004212,31.003013],[-85.497137,30.997536],[-87.600282,30.997536],[-87.633143,30.86609],[-87.408589,30.674397],[-87.446927,30.510088],[-87.37025,30.427934],[-87.518128,30.280057],[-87.655051,30.247195],[-87.90699,30.411504],[-87.934375,30.657966],[-88.011052,30.685351],[-88.10416,30.499135],[-88.137022,30.318396],[-88.394438,30.367688],[-88.471115,31.895754],[-88.241084,33.796253],[-88.098683,34.891641],[-88.202745,34.995703],[-87.359296,35.00118]]]}},

{"type":"Feature","id":"02","properties":{"name":"Alaska","density":1.264},"geometry":{"type":"MultiPolygon","coordinates":[[[[-131.602021,55.117982],[-131.569159,55.28229],[-131.355558,55.183705],[-131.38842,55.01392],[-131.645836,55.035827],[-131.602021,55.117982]]],[[[-131.832052,55.42469] 
... }},

{"type":"Feature","id":"06","properties":{"name":"California","density":241.7},"geometry":{"type":"Polygon","coordinates":[[[-123.233256,42.006186],[-122.378853,42.011663],[-121.037003,41.995232],[-120.001861,41.995232],[-119.996384,40.264519],[-120.001861,38.999346],
... }}]}



RST ref
-------

::

	pip install rstvalidator
	python -m rstvalidator README.rst


apparently boxing title with ===== above and below a line could throw off validator.
was that a .md feature?  but it had worked on short rst...
