#!/bin/env/python 
# using python 2.7


import os
from flask import Flask

def create_app(test_config=None):
	app = Flask(__name__)
	basedir = os.path.abspath(os.path.dirname(__file__))
	config = os.environ['APP_CONFIG']

	# do a "Hello World"
	# ref http://flask.pocoo.org/docs/1.0/tutorial/factory/
	@app.route('/hello')
	def hello():
		return "Hello, World!"

	return app
#end create_app()



if __name__ == '__main__':
    app = create_app()
    # Bind to PORT if defined, otherwise default to 5000.
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
