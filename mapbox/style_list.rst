

trying to find out if i had a data layer in zwedc/smelly.  adjoin not displaying tile data correctly :(

mapbox://styles/sn50/cjory4ozjhkzy2smnzzt6pi7a likely what i refered as "caltrans tass cities 2015  population" title was "cali terrain" - url from share button ( publish only have names now)

mapbox://styles/sn50/cjpdk7mpgbx8f2ss4bu9vzfsl "ZWEDC 50x50m - Light" (layer with data low in the list, colored in mapbox studio itself)
above eventually lead to 
source:{  ... url: 'mapbox://sn50.aae3dmkj ...}  in caair.html (and likely some older ones)   but how did i generate aae3dmkj ?? which map is that one??

smelly.html went on to use:
        addStatus = map.addLayer({
            id: currentLoadedMapLayer, //--id: 'caair',
            type: 'fill',
            layout: {
                visibility: 'visible'
                //visibility: zwedcPolyVis
                //visibility: 'none'        // can use this to make ZWEDC data disapear ##
            },
            // sn50.SfZwedcAllHiBi10x need to be in url and source-layer, w/ username in url, NO username in source-layer.  be careful!!
            source: {
                type: 'vector',
                //url: 'mapbox://sn50.aae3dmkj'   // ZWEDC 25x25 sq first test data set (at 10x?)
                //url:   'mapbox://sn50.SfZwedcSprHiBi10x'                  // 2nd csv2gson upload    ... next, try to make way to toggle between them.   hmm. ready to upload em all!
                url:   'mapbox://' + mapboxUser + "." + inputFormSelection
            },
            //'source-layer': 'ZWEDC_50x50m-29q7xv',    // retrieved from mapbox web site Tile management...  [1st dummy test data]
            //'source-layer': 'SfZwedcSprHiBi10x',  // no username prefix here!! duh!!
            'source-layer': inputFormSelection,     //  grab source layer name from parsed input form

