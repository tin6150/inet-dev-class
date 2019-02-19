#!/bin/env python 

# flask main executable
# run as (with python3 in venv): 
# python api.py 


# this is rest quickstart for flask-rest framework
# https://flask-restful.readthedocs.io/en/latest/quickstart.html

# hello world, returning as json key-value pair


from flask import Flask
from flask_restful import Resource, Api
import os 


app = Flask(__name__)
api = Api(app)

class HelloWorld(Resource):
    def get(self):
        return {'hello': 'world'}   # actually return json, or flask create such html content type?

api.add_resource(HelloWorld, '/')

if __name__ == '__main__':
    #app.run(debug=True)
    port = int(os.environ.get('PORT', 5000))
    #app.run(port=port)                         # this is default, localhost only
    app.run(host='0.0.0.0', port=port, debug=True)          # i have iptables limiting exposure

# vim:shiftwidth=2 tabstop=4 formatoptions-=cro list nu expandtab filetype=python
