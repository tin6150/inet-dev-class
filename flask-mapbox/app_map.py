#!/bin/env/python 
# using python 2.7

"""
flask app to load mapbox studio styled map
start with things that i had previously "published" via html in github.io
structuring after Tyler biositting templates/mbgl_index.html
"""


import os
from flask import Flask
from views import master	# this likely the one that loads views.py

from flask_sqlalchemy import SQLAlchemy

def create_app(test_config=None): 
        app = Flask(__name__)
	basedir = os.path.abspath(os.path.dirname(__file__))
	APP_CONFIG='config.DevelopmentConfig'
	config = APP_CONFIG
	#config = os.environ['APP_CONFIG']

	#DATABASE_URL = 'sqlite:///tin_sqlite.db' 
	#app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_URL 
	#config = os.environ['DATABASE_URL'] # biositting_tools get this from OS ENV
	#db = SQLAlchemy(app)
	
	# Tyler Biositting approach 
	app.register_blueprint(master, url_prefix='')
	#app.config.from_object(config)
	#register_extensions(app)
	#register_shellcontext(app)


	# do a "Hello World"
	# ref http://flask.pocoo.org/docs/1.0/tutorial/factory/
	# below register app to http://bofh.lbl.gov:5000/hello
	@app.route('/hi')
	def hi():
		"""Print 'hello world' as the response body."""
		return "Hi, World! (at /hi)"

	# Tyler used blueprint to register bunch of views rather than defining them here.
	# https://opensource.com/article/18/4/flask
	# as main app : 
	#@app.route('/')  # register to top of web server
	#def hello_world():
		#return "Hello, World! (at /)"

	return app
#end create_app()





if __name__ == '__main__':
    app = create_app()
    # Bind to PORT if defined, otherwise default to 5000.
    port = int(os.environ.get('PORT', 5001))
    #app.run(port=port)				# this is default, localhost only
    app.run(host='0.0.0.0', port=port)		# i have iptables limiting exposure

