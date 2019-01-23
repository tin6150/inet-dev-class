
Mapbox Notes
============

learning
mapbox gl js 

as part of collab with Ling Jin of ETA.

from biositing_tools prj via Tyler Huntington

Gist: https://gist.github.com/tin6150/e271e5d3bef6d93ebc6817170ddd2456

.. image:: https://gist.githubusercontent.com/tin6150/e271e5d3bef6d93ebc6817170ddd2456/raw/e5a53cc65f39bc97dabaf3a54ed6c3cac1c2ab3d/census_wilmington.png 
   :scale: 50%
   :alt: screenshot of census data displayed in Mapbox WebGL JavaScript


Mapbox FAQ
==========

* Use LngLat, just like geoJSON.  ie, it is Longitude first, then Latitude (in the paired geo coordinate). 
	* Lng is East-West.   range [-180,180].  Milpitas is -121.985.  Y-axis on paper map.
	* Lat is North-South. range [-90,90].  Milpitas is 37.408.      X-axis on paper map.
	* Leaflet seems to use LatLng :(

* Use Mercator Coordinate
	* https://www.mapbox.com/mapbox-gl-js/api/#mercatorcoordinate

* Mapbox.js is legacy raster-based server generated tilemap.  Inherited (all?) features from leaflet

* Mapbox GL JS is newer vector-based client assembled tilemap that is more performing and feature rich. (and way to divert from opensource/leaflet?)


Ref
===

Mapbox webgl javascript: https://github.com/mapbox/mapbox-gl-js

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

Convert shapefile and GeoJSON to MBTiles (tileset importable into Mapbox)
 * https://openmaptiles.org/docs/generate/custom-vector-from-shapefile-geojson/
 * tippecanoe


Reading list
============

* Choropleth by census track population, shows population density, possibly as 3D.  Peter Liu, mapbox engineer.  https://blog.mapbox.com/dive-into-large-datasets-with-3d-shapes-in-mapbox-gl-c89023ef291

* https://www.mapbox.com/help/processing-satellite-imagery/ tools, Turf.js, side-by-side swipe comparison.
  addLayer before/after X, etc 

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

- https://tin6150.github.io/inet-dev-class/mapbox/mapbox-census-pop-delaware.html  Delaware population count choropleth
- https://tin6150.github.io/inet-dev-class/mapbox/mapbox-census-pop.html  Similar to above, with some hover data display.  

- https://tin6150.github.io/inet-dev-class/mapbox/tass_city_pop.html  CalTrans TASS CA cities population (count, not density)

- https://tin6150.github.io/inet-dev-class/mapbox/ZWEDC_gson.html  ZWEDC csv->geojson, point data.  
- https://tin6150.github.io/inet-dev-class/mapbox/ZWEDC_heatmap.html  ZWEDC csv->geojson, point data, heatmap coloring.  
- https://tin6150.github.io/inet-dev-class/mapbox/ZWEDC_50x50sq.html  ZWEDC csv->geojson, data in 50x50m sq.  
- https://tin6150.github.io/inet-dev-class/mapbox/ZWEDC_50x50sq+Plugin.html  As above, trying to use some mapbox plugin (js module via import?).  Have not been able to get this to work.  tried moving code under js/, there are more notes there, but overall, no dice yet.

- https://tin6150.github.io/inet-dev-class/mapbox/ZWEDCcsv2gson_heatmap.py.  (was thinking of naming it ZWEDC_countDup.html).  The value of the point is used to duplicate the number of appearance of the point with value of one.  This hopefully create a data set for a dot-plot that is HOT at the point with highest ZWEDC value....
  use point data, not 50x50 sq.  didn't work well.  
Scale:
- 0.1 may need to be come 1 point.
- 0.2 become 2 points.
- 1.0 become 10 points
- 12.7 becomes 127 points.

- https://tin6150.github.io/inet-dev-class/mapbox/mapbox-addLayer.html  Use addLayer() to get ZWEDC_50x50 as tileset data, then use JS to do data-driven presentation.  (thus essentially not using mapbox studio styling to present the data).  Need to understand JS much more here to do the work.

- https://tin6150.github.io/inet-dev-class/mapbox/ZWEDC_50x50sq_js.html - GL JS version of ZWEDC_50x50sq.html  (ie, use JS instead of Studio to color render data), which is the method needed to addLayer() to Tyler's framework.

- https://tin6150.github.io/inet-dev-class/mapbox/mapbox-leaflet.html - GL JS bind with leaflet.  Note that Leaflet seems to use LatLng !! :(

- https://tin6150.github.io/inet-dev-class/mapbox/ZWEDC_jq_slider.html - jquery slider version of ZWEDC_50x50sq_js.html (jquery-ui slider is quirky in mobile, need to click on desired spot.  there is a "hack" to allow for dragging on touch screen, need to load an extra script.  see http://touchpunch.furf.com/

- https://tin6150.github.io/inet-dev-class/mapbox/caair.html - drop down menu to pick sites, season, etc.  early draft to eventually pick multiple sites.  not functional yet.  zoom 5.5 to see whole ca.  population layer there at 761747b
- https://tin6150.github.io/inet-dev-class/mapbox/caair_zwedc.html - fork of caair.html, with a make up data set for Ling to comment on coloring scale.  have state vs population layers in there still at 761747b.
- https://tin6150.github.io/inet-dev-class/mapbox/caair_zwedc_uicode.html - fork of caair_zwedc.html, coding handler to respond to drop down selector (add/remove layer/source).   working at git log 21d86ad


gdal - Geospatial Data Abstraction Library
==========================================

gdal.org
apt install gdal-bin


convert from (24bit?) TIFF to 8bit TIFF:
gdal_translate -ot Byte -of GTiff path\Input.tif path\output.tif

(Mapbox supports geocoded TIFF, but only in 8bit format, which maybe likely means single color grayscale)


Mapbox data structure
=====================

* Dataset.  what user import as data.  vector or raster.  
* Tileset is basic store of vector data that will be rendered by Mapbox (studio) style.  not editable, just optimization intermediate internal format for mapbox.
* (ESRI) ``ShapeFile`` are imported into Dataset, then converted into Tileset (immutable).
* Actually, Dataset import required geojson.  Tileset import can handle .zip containting shapefile (<=260 MB)


* Mapbox studio create layers in the "style" for visualization and UI.
* Style can be access by URL by JavaScript (Mapbox GL JS) for web app.

* geojson, when imported in to MapBox Studio, is converted into vector tileset for efficient rendering.
* density coloring is done by layer styling in MapBox studio (ie web app), though there maybe something in JS that can set/ovewrite(?) this coloring.

* Brief doc on uploading data to mapbox studio: https://www.mapbox.com/studio-manual/overview/geospatial-data/ .  bottom of page has some tricks to shrink large .zip, though not sure if that will work for CA.


Barebone geoJSON
----------------

.. code:: json

        {
          "type": "FeatureCollection",
          "features": []
        }



geoJSON with single point
-------------------------

.. code:: json5

        {
          "type": "FeatureCollection",
          "features": 
          [
              {
                      "type": "Feature",
                      "properties": {
                        "name": "Van Dorn Street",
                        "marker-color": "#0000ff",
                        "marker-symbol": "rail-metro",
                        "line": "blue"
                      },
                      "geometry": {
                        "type": "Point",
                        "coordinates": [
                          -77.12911152370515,
                          38.79930767201779
                        ]
                      }
              }
          ]
        }       // tagged as json5, comments would be allowed if parser supports this new version


* Example geoJSON: https://www.mapbox.com/help/data/stations.geojson
* Additional ref: https://www.mapbox.com/help/define-geojson/


ZWEDC data with two example points
----------------------------------

This format has been tested to work, see ZWEDCcsv2gson.py that creates .geojson that was imported successfully into mapbox tileset.

.. code:: geojson


        { "type": "FeatureCollection", "features": [
            { "type":       "Feature",
              "properties":
                   {"avecon": 0.18577}
                   // properties is required (at least for mapbox), even if empty.  could give it name or timestamp
              ,
              "geometry": { "type": "Point", "coordinates": [ -121.985002139616, 37.4079452829464 ] }
            }
            ,
            { "type":       "Feature",
              "properties":
                   {"avecon": 0.18817}
              ,
              "geometry": { "type": "Point", "coordinates": [ -121.984437247048, 37.4079404316778 ] }
            }
            //,   // add comma iff there is next entry. json don't have a comment officially.  tailing comma not allowed either
        ] }



ZWEDC data as polygon
---------------------

Below should work to create polygon to make density coloring on map easier.

.. code:: geojson

        { "type": "FeatureCollection", "features": [
            { "type":       "Feature",
              "properties":
                   {"avecon": 0.18577}
                   // properties is required (at least for mapbox), even if empty.  could give it name or timestamp
              ,
              "geometry": { "type": "Polygon", "coordinates": [ [
                      [ -121.985, 37.407 ],     // LT
                      [ -121.984, 37.407 ],     // RT
                      [ -121.984, 37.406 ],     // RB
                      [ -121.985, 37.406 ],     // LB
                      [ -121.985, 37.407 ],     // LT, close it back.  5 points make a square :)
              ] ] }  // strangely need to open two square bracket (support for multi-polygon?)
            }
            //,   // add comma iff there is next entry, json don't have a comment officially
        ] }




Snipplet from stateData.geojson  
-------------------------------

stateData.geojson is the example data source for the choropleth tutorial (mapbox, leaflet).
The geojson file has the polygon info, as well as name and density value, all embeded as one record per state.

Note Alaska and some other state use "MultiPolygon", which are more time consuming to process.

{"type":"FeatureCollection","features":[

{"type":"Feature","id":"01","properties":{"name":"Alabama","density":94.65},"geometry":{"type":"Polygon","coordinates":[[[-87.359296,35.00118],[-85.606675,34.984749],[-85.431413,34.124869],[-85.184951,32.859696],[-85.069935,32.580372],[-84.960397,32.421541],[-85.004212,32.322956],[-84.889196,32.262709],[-85.058981,32.13674],[-85.053504,32.01077],[-85.141136,31.840985],[-85.042551,31.539753],[-85.113751,31.27686],[-85.004212,31.003013],[-85.497137,30.997536],[-87.600282,30.997536],[-87.633143,30.86609],[-87.408589,30.674397],[-87.446927,30.510088],[-87.37025,30.427934],[-87.518128,30.280057],[-87.655051,30.247195],[-87.90699,30.411504],[-87.934375,30.657966],[-88.011052,30.685351],[-88.10416,30.499135],[-88.137022,30.318396],[-88.394438,30.367688],[-88.471115,31.895754],[-88.241084,33.796253],[-88.098683,34.891641],[-88.202745,34.995703],[-87.359296,35.00118]]]}},

{"type":"Feature","id":"02","properties":{"name":"Alaska","density":1.264},"geometry":{"type":"MultiPolygon","coordinates":[[[[-131.602021,55.117982],[-131.569159,55.28229],[-131.355558,55.183705],[-131.38842,55.01392],[-131.645836,55.035827],[-131.602021,55.117982]]],[[[-131.832052,55.42469] 
... }},

{"type":"Feature","id":"06","properties":{"name":"California","density":241.7},"geometry":{"type":"Polygon","coordinates":[[[-123.233256,42.006186],[-122.378853,42.011663],[-121.037003,41.995232],[-120.001861,41.995232],[-119.996384,40.264519],[-120.001861,38.999346],
... }}]}


mapbox zoom levels
------------------

tileset have defined zoom extent, which is range where it can add/remove data depending on zoom level.
vector data can zoom (in) all the way to z22, but if tileset don't have lots of data, it would seem simplified.

- z22 : most detailed?

- z16 : max zoom where data is relevant for census population tiger/line shapefile .  probably city block level detail.
- z16 : lot size starts to show
- z15 : see about 50 blocks of a city
- z13 : streets starts to have some width
- z12 : streets of one main city
- z10 : min zoom for census population tiger/line to be visible.  Good starting point to work on Census data map. 
- z10 : cut off for station-6yhf0y, a simple example shapefile by mapbox (for where?)

- z8  : many cities name showed on a map
- z6  : cut off used for cholopleth tutorial (state level data)  

- z3  : continent wide

- z0  : least detailed , world wide map


ESRI shapefile
--------------

Example from mapbox at
https://www.mapbox.com/help/data/stations.zip ::

-rw-r--r-- 1 tin itd 87623 Nov  4  2015 stations.dbf	# dBase III, 86 records
-rw-r--r-- 1 tin itd  2508 Nov  4  2015 stations.shp	# esri binary
-rw-r--r-- 1 tin itd   788 Nov  4  2015 stations.shx    # esri binary
-rw-r--r-- 1 tin itd   143 Nov  4  2015 stations.prj	# ascii 
GEOGCS["GCS_WGS_1984",DATUM["D_WGS_1984",SPHEROID["WGS_1984",6378137,298.257223563]],PRIMEM["Greenwich",0],UNIT["Degree",0.017453292519943295]]


* no need to expand the zip file before upload to mapbox
* rename the .zip  to something I like, eg mv tabblock2010_06_pophu.zip tiger_delaware.zip

* so, shapefile can be imported directly into a tileset.  hopefully style it to be visually useful.

* Then still need to extract the pouplation info which in in dBase III... and create it as a csv to be added as a layer to mapbox studio?


WebApp
======

Creating webapp with Mapbox has a number of tools.
The GL JS may be the core for putting WebGL with a JavaScript (browser client).
But also watch for these things:

* Start with the "How web apps work" page:
	* https://www.mapbox.com/help/how-web-apps-work/

* Mapbox.js
	* extends leaflet, mapbox studio classic
	* LEGACY.  no longer in dev.
	* use raster tiles (tiles generated by server, can't change style)
	* (mapbox GL js use vector tiles, tiles generated by client, change style dynamically.  may not have all the features, eg, things that leaflet does with raster not avail in GL js?)
	* Encourage users to switch to gl js, as vector performs better.
	* https://www.mapbox.com/help/transition-from-mapbox-js-to-mapbox-gl-js/
	* Tyler biositting tool use: ??? TBA


* Mapbox GL JS 
	* https://www.mapbox.com/mapbox-gl-js/api/
	* CDN vs module bundler methods, other than invokation approach, everything else remains the same.
	* CDN method is using `<script src=http... >`, probably less cumbersome
	* Module bundler is using `npm install --save mapbox-gl`, same approach plugin use, but maybe instructions not fully clear

* Mapbox Plugins.  These are extension to GL JS.
  A number of them need to be installed as npm package (ie module bundler approach).
  But still run on client side (have yet to figure out, one plugin, 
  styles/zoom/compass/ruler used webpack to create a bundle.js, and 
  example was clearly running off github pages.
  so, no fancy node.js server needed.  
  No need for Flask either (but does not prevent its use)
	* https://www.mapbox.com/mapbox-gl-js/plugins/  
	* compare plugin.  swipe left/right to see diff.  Maybe useful.  https://www.mapbox.com/mapbox-gl-js/example/mapbox-gl-compare/ 
	* infobox
 	* style-switcher (to change basemap?)
	* gl-layer-groups (toggle layers? so switch b/w source data?)
	* gl-sync-move (side-by-side comparison and move?)
	* gl-inspect - help with debugging... 
* Mapbox React.  
	* sync move - takes two or more maps and sync their move.  maybe similar to what Ling showed in leaflet for side-by-side comparison.  https://github.com/mapbox/mapbox-gl-sync-move
	* need to learn what really is React.  (vs Angular, etc?) https://github.com/mapbox/mapbox-react-examples


* Property Expression vs Property Function
	* Property Expression - new api for data-driven styling, logic, manipulation
	* Property Function   - legacy, still works, but recommend going away
	* https://www.mapbox.com/help/mapbox-gl-js-expressions/
	* https://www.mapbox.com/mapbox-gl-js/example/updating-choropleth/ Use Property Expression with fill (polygon) data to do choropleth of state population (unlike the beginner tutorial, this use GL JS and not mapbox studio)   Oh heck, it zoom it to provide county population data!!
	

Mapbox GL JS
============

https://www.mapbox.com/mapbox-gl-js/api/
src/ui/map.js

IControl  
NavigationControl
are these to add control widget on the web page?

ScaleControl - zoom?
AttributionControl - credits
Popup

ImageSource - map.addSource(...) 
CanvasSource

addLayer(...) - https://www.mapbox.com/help/analysis-with-turf/  (early part cover addLayer() )


Also read before coding
https://www.mapbox.com/help/how-web-apps-work/


Mapbox SDK
==========

* There is a python sdk for things like uploading data to mapbox.
* There is a CLI sdk based on the python sdk.  Used that to upload data.
* SDK has way to delete dataset, but not sure if that works for removing tileset.  maybe stuck with the 1200 tileset for ETA collab.


Census data
===========

probably need some conversion to get population density (population divided by the census block or census track area). 

census block geo boundary and population data can be found here: https://www2.census.gov/geo/tiger/TIGER2010BLKPOPHU/
California is:

[   ]	tabblock2010_06_pophu.zip	08-Jun-2011 07:28	408M
(CA is state 06 always?) 
https://www2.census.gov/geo/tiger/TIGER2010BLKPOPHU/tabblock2010_06_pophu.zip ::

	-rw-rw-r-- 1 tin itd  34M Mar 28  2011 tabblock2010_06_pophu.dbf
	-rw-rw-r-- 1 tin itd  167 Mar 28  2011 tabblock2010_06_pophu.prj
	-rw-rw-r-- 1 tin itd 653M Mar 28  2011 tabblock2010_06_pophu.shp
	-rw-rw-r-- 1 tin itd  17K May 20  2011 tabblock2010_06_pophu.shp.xml
	-rw-rw-r-- 1 tin itd 5.5M Mar 28  2011 tabblock2010_06_pophu.shx

See https://www.mapbox.com/help/define-shapefile/  on importing esri shapefile.
Import .zip, must uncompress to <= 260 MB :(

start with a smaller state first...
below reverse search matched Delaware.  It is TIGER/Line Shapefile 2010
https://catalog.data.gov/dataset/tiger-line-shapefile-2010-2010-state-delaware-2010-census-block-state-based-shapefile-with-hous

[   ]	tabblock2010_10_pophu.zip	08-Jun-2011 07:28	12M    
(Delaware is state 10 always?)
ftp://ftp2.census.gov/geo/tiger/TIGER2010BLKPOPHU/tabblock2010_10_pophu.zip ::

	-rw-rw-r-- 1 tin itd  1206040 Mar 29  2011 tabblock2010_10_pophu.dbf
	-rw-rw-r-- 1 tin itd      167 Mar 29  2011 tabblock2010_10_pophu.prj
	-rw-rw-r-- 1 tin itd 19819640 Mar 29  2011 tabblock2010_10_pophu.shp
	-rw-rw-r-- 1 tin itd    16978 May 20  2011 tabblock2010_10_pophu.shp.xml
	-rw-rw-r-- 1 tin itd   193020 Mar 29  2011 tabblock2010_10_pophu.shx


Tileset detail (without dbf info?) :: 

	BLOCKCE 	String
	BLOCKID10 	String
	COUNTYFP10 	String
	HOUSING10 	Number  0 - 971
	PARTFLG 	String
	POP10 		Number 	0 - 2590
	STATEFP10 	String
	TRACTCE10 	String

Bounds for Delaware ::

 * -75.8,  38.5,  -75.0,  39.8
 * Wilmington, DE lat long: 39.739071 , -75.539787
 * Mapbox GL JS use `center: [-121.95978, 34.73907],` ie, lng, lat (cuz geoJson is ordered as longitude, lat pair as well).



Misc
====

eg_data
-------

small version (eg head -10) of input file to aid coding.
they do not need to be uploaded to mapbox, they are not production data.

DATA_caair, DATA_zwedc are geojson converted from csv generated by Wei.  
Since all data are generated from upstream source, not checked in, no backup.


TMP_DATA folder
---------------

The TMP_DATA directory contains various zip files that I downloaded and may have played with.
Data imported into mapbox (tileset) as appropriate.
They are large files, do not check them into git.
eg.  Census zip file (shapefile), CalTrans/TASS zip (pbf)


RST ref
-------

::

	pip install rstvalidator
	python -m rstvalidator README.rst


apparently boxing title with ===== above and below a line could throw off validator.
was that a .md feature?  but it had worked on short rst...
