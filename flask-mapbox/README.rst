
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
	pip install -r requirements.txt # from tyler's biomining tool, should have everything this learning prj need.
	# hmm... many eggs error out during install in wsl: pandas, matplotlib, descartes, psycopg2, Shapely

	source venv/bin/activate 
	python app.py			# use python 2.7




DB
--

* try to use sqlite first
* may move to postgres to be compatible with ETA project goals.


See also
--------

* http://flask.pocoo.org/docs/1.0/tutorial/factory/
* https://bitbucket.org/sn5050/biositing_tool_test/src/master/



tin
2018.10.28

