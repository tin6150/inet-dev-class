
jquery inside SCRIPT area
rewrite DOM:

            document.getElementById('features').innerHTML = "<H3>ZWEDC</H3>\n" + "n/a"


~~~~

mbgl_index.html 
js 
to handle zwedc selector in dropdown 

many many functions are defined inside the map.on('load',... 
__2spaces_indent__
  map.on('load', function() {
    |
    | ie at the same level as many 
    map.addLayer({...
    |
    | also same level as many 
    map.on('click', 'wwt_pts', function(e)
    |
    |
    function updatePolyLayerVis() {
    |
    // likely also need to  add ZWEDC selector listener handle here (actually no) ##
    function updateDataFiltersPanel(layer_data_type) {
    |
    |
    |
    // added ZWEDC overlay dropdown handler here (bottom of if/elseif block) -tin ## 
    // still need addLayer() for the data... 
    // Listener for changes in the Overlay Layer dropdown menu
    var poly_selector = document.getElementById("polygon-layer-selector");
    poly_selector.addEventListener('change', function(e) {
      if (poly_selector.value == "biomass") {
        map.setLayoutProperty('counties', 'visibility', 'visible');
        map.setLayoutProperty('zwedc', 'visibility', 'none');			// ##
        ...
      } else if (poly_selector.value == "zwedc") {     			// ZWEDC ##
        map.setLayoutProperty('zwedc', 'visibility', 'visible');
        map.setLayoutProperty('terrain-data',   'visibility', 'none');	// tmp use by zwedcSpringMam ##
        map.setLayoutProperty('zwedcSpringMam', 'visibility', 'none');  // doesnt exist yet
        map.setLayoutProperty('zwedcSummerJja', 'visibility', 'none');     	// used point data from heatmap test
        // update the swatches in the legend.  Tyler had 9 entries, I am trying with fewer now... ##
        // http://html-color.org/DBEE72
        // var zwedc_gradient = ['#ff0000', '#ffff00', '#00ff00', '#00ffff', '#0000ff', '#ff00ff', '#777777', '#000000', '#edac70']; // need 9 values in this list
        var zwedc_gradient = ['#f2f3f4', '#FED976', '#FEB24C', '#FD8D3C', '#FC4E2A', '#E31A1C', '#BD0026', '#800026', '#7c27c2', '#5b08a3']; // need 9 values in this list. there are 10 here, last one is dropped
        for (i = 0; i < zwedc_gradient.length; i++) {
          elem = 'legend-swatch-' + i.toString();
          swatch = document.getElementById(elem);
          swatch.style.backgroundColor = zwedc_gradient[i];
        }
        swatch.style.backgroundColor = zwedc_gradient[i];
        // update the header for the swatch gradient
        swatch_header = document.getElementById('swatch-gradient-header');
        swatch_header.innerHTML = "ZWEDC max (unit?)";
        // update the max value for the swatch gradients
        max = document.getElementById('legend-gradient-scale-label-max');
        max.innerHTML = "25"	// ## fix number?  25 was highest range used in ZWEDC_50x50sq_js.html
        //scale_label_min.innerHTML = "< 10";			// default set higher up, hopefully can overwrite with below
        innerHTML = "0";					// ZWEDC will use a diff value for min... ##
        // update global layer tracking vars
        current_poly_layer = 'counties';
        current_poly_boundary_layer = 'county_lines';
        analysis_params['sel_poly_data_type'] = 'zwedc';
        updateDataFiltersPanel('zwedc');
      } else if (poly_selector.value == "zwedcSpringMam") {    		// ZWEDC Spring MAM ##
 


~~~~

instead of converting geojson to create tileset, 
sometime Tyler just load the geojson file as static file 
see mpgl_index.html  hear start of JS section:

  function loadPointData() {
    $.getJSON("/static/geo_data/crp2016_pts.geojson", function(json) {
        crop_2016_pts = json; // this will show the info it in firebug console
    });
    $.getJSON("/static/geo_data/crp2020_pts.geojson", function(json) {
        crop_2020_pts = json; // this will show the info it in firebug console
    });
    $.getJSON("/static/geo_data/crp2050_pts.geojson", function(json) {
        crop_2050_pts = json; // this will show the info it in firebug console
    });    


~~~~

Census data for california
tabblock2010_06_pophu.zip
from census, URL in gist.

gonna rename this ca2010census.zip


Tile Brute? hadoop script for generating 14 zoom levels of all states?
was for mapbox, but not sure what kind of result is produced.
follow later if run into walls.  but probably better look into gdal and mapnik
https://github.com/ndimiduk/tilebrute
bg info in slide  https://www.slideshare.net/xefyr/cartography-to-the-cloud
