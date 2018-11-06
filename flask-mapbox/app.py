#!/bin/env/python 
# using python 2.7


import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

def create_app(test_config=None):
	app = Flask(__name__)
	basedir = os.path.abspath(os.path.dirname(__file__))
	APP_CONFIG='config.DevelopmentConfig'
	config = APP_CONFIG
	#config = os.environ['APP_CONFIG']

	DATABASE_URL = 'sqlite:///tin_sqlite.db' 
	app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_URL 
	#config = os.environ['DATABASE_URL'] # biositting_tools get this from OS ENV
	db = SQLAlchemy(app)
	
	# do a "Hello World"
	# ref http://flask.pocoo.org/docs/1.0/tutorial/factory/
	# below register app to http://bofh.lbl.gov:5000/hello
	@app.route('/hello')
	def hello():
		return "Hello, World! (at /hello)"

	# https://opensource.com/article/18/4/flask
	# as main app : 
	@app.route('/')  # register to top of web server
	def hello_world():
		"""Print 'Hello, world!' as the response body."""
		return "Hello, World! (at /)"

	return app
#end create_app()





if __name__ == '__main__':
    app = create_app()
    # Bind to PORT if defined, otherwise default to 5000.
    port = int(os.environ.get('PORT', 5000))
    #app.run(port=port)				# this is default, localhost only
    app.run(host='0.0.0.0', port=port)		# i have iptables limiting exposure

