#!/bin/env python 

# flask main executable
# run as (with python3 in venv): 
# python api.py 


# this is rest quickstart for flask-rest framework
# https://flask-restful.readthedocs.io/en/latest/quickstart.html

# eg 2 resource routing
# CRUD = Create Read Update Delete - REST HTTP action verbs


from flask import Flask, request
from flask_restful import Resource, Api
import os 


app = Flask(__name__)
api = Api(app)

todos = {}

class TodoSimple(Resource):
    def get(self, todo_id):
        return {'todo_id': todos[todo_id]}   # actually return json, or flask create such html content type?

    def put(self, todo_id):
        todos[todo_id] = request.form['data']
        return {todo_id: todos[todo_id]}

api.add_resource(TodoSimple, '/<string:todo_id>')

if __name__ == '__main__':
    #app.run(debug=True)
    port = int(os.environ.get('PORT', 5000))
    #app.run(port=port)                         # this is default, localhost only
    app.run(host='0.0.0.0', port=port, debug=True)          # i have iptables limiting exposure


# vim:shiftwidth=2 tabstop=4 formatoptions-=cro list nu expandtab filetype=python
