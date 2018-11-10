
Mapbox Notes
============

learning
mapbox gl js 

as part of collab with Ling Jin of ETA.

from biositing_tools prj via Tyler Huntington



===
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


========
Examples
========

Loading example pages via web site provided by github.io 

- https://tin6150.github.io/inet-dev-class/mapbox/
- 
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


