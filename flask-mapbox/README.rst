
flask-mapbox
------------

a simple web app to display geo coordinated data.
learning platform for the ETA collaboration with Ling Jin.

* Flask as simple python web framework (lighter than django)
* mapbox-gl as javascript to display data on map, using mapbox WebGL API


Starting Dev env
----------------

.. code-block:: bash

	# one-time creation of virtual env
	virtualenv venv
	source venv/bin/activate 
	pip install -r requirements.txt 
	# from tyler's biomining tool, should have everything this learning prj need.
	# hmm... many eggs error out during install in wsl: pandas, matplotlib, descartes, psycopg2, Shapely
	# see git log 7dd2894 for full list. 
	# maybe unicode caused problem too...
	# there are multiple problems.  for now, removed things other than flask, just to be able to dev on wsl for a bit
	# per https://opensource.com/article/18/4/flask
	# psycopg2 is required for flask... so if that doesn't install in wsl, no more dev in windoze!!

	# each time needing to start server/app :
	export APP_CONFIG='config.DevelopmentConfig'
	export DEBUG='True'
	source venv/bin/activate 
	python app.py			# use python 2.7


Installing Mapbox GL JS Plugins
-------------------------------

* Style switcher - https://github.com/el/style-switcher

.. code-block:: bash

	bofh> npm i mapbox-gl-style-switcher --save



* https://github.com/mapbox/mapbox-gl-sync-move



Example Flask Apps
==================

* app.py - Simple Hello World
* app_db.py - Was supposed to use DB, didn't get it to work, abandoned.
* app_map.py - Load html that invoke mapbox GL JS.  works.
  http://bofh.lbl.gov:5001/ZWEDC_50x50sq 
  http://bofh.lbl.gov:5001/alviso



###############################################################


Mapbox GL JS Plugins
--------------------

Many of the plugins are npm install, presumably they run on the server side.
These would be features that a simple static html served by github.io won't work, 
since there is no server side execution that a Flask app offer.

* sync move - takes two or more maps and sync their move.  maybe similar to what Ling showed in leaflet
  for side-by-side comparison.  
  https://github.com/mapbox/mapbox-gl-sync-move



DB
--

* try to use sqlite first
* may move to postgres to be compatible with ETA project goals.
* At least for the demo and what Tyler telling us to use, it is sqlite:///biositing.db 


See also/Ref
------------

* http://flask.pocoo.org/docs/1.0/tutorial/factory/
* http://flask.pocoo.org/docs/1.0/tutorial/#tutorial 
* https://opensource.com/article/18/4/flask
* https://bitbucket.org/sn5050/biositing_tool_test/src/master/



Program Entry Point?
====================


@app.route(...) is one way to respond to URL path req.
Biositting use 
app.register_blueprint(...)
Blueprint was supposed to collect bundle of views.
the bundle of route(...) defintions goes into the views.py


views.py (biositting)
	@master.route('/')  def root(): ?
    		return(render_template('mbgl_index.html', error=error, form=form))
		file in `templates/mbgl_index.html`
			this is where mapbox GL JS' map.on('load'... ) is defined 
			map.addLayer is here
		        url: 'mapbox://tylerhuntington222.cjjj38 ...'

			TODO: 
			try loading my map as an layer here.
			but maybe better get a flask app to load mapbox, and 
			add some JS control to it, so i know how it behave first.

			

	@master.route("/basemap") ?
	  return flask.jsonify({'biomass': gpd_to_geojson(counties_df, cols_counties),
				'thermal': gpd_to_geojson(thermal, cols_thermal)})

	@master.route("/points") ?
	  return flask.jsonify({'AD': gpd_to_geojson(AD_pts, cols_AD_pts),
				'COMB': gpd_to_geojson(COMB_pts, cols_COMB_pts),
				'W2E': gpd_to_geojson(W2E_pts, cols_W2E_pts),





..code:: 

	config.py 
	places where os.environ['...'] 
	define where it reads OS Environment var made
	these need to be defined for app to work
	In Biositting, 
	DATABAASE_URL=sqlite:///biositing.db
	APP_VERSION=JBEI


Model relationship
------------------

* Web DOM Model View thing?
* biositting has a model.py, but this seems to be a DB for storing user's "saved site", suggestions, data problem reporting.

 


tin
2018.12.16

