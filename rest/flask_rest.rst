
following 
https://flask-restful.readthedocs.io/en/latest/quickstart.html
to try sketching a rest skeleton for bofhbot daemon.

cd flask/
virtualenv --python=python3 venv4flask
source     venv4flask/bin/activate

pip install flask-restful

python api.py 0:5000    # don't think 0:5000 works
						# need to change app.py with specific param.




Flask reference
===============

* http://flask.pocoo.org/docs/1.0/quickstart/#routing
  parsing URL, invoking the right fn to respond 

* http://flask.pocoo.org/docs/1.0/quickstart/#the-request-object
  To access parameters submitted in the URL (?key=value) you can use the args attribute:
        searchword = request.args.get('key', '')

* http://flask.pocoo.org/docs/1.0/quickstart/#sessions
  sessions (client-side).  using cryptographically signed cookie.
  this is for Flask in general, but probaly then allow for REST call to be authenticated.

* server-side session 
  is avail in Flask, dig if need it.


Notes on flask and helper libraries
-----------------------------------

* blueprint
  use to make routing URL to multiple "apps"
  make programming more modular
  avoid having a huge app.py with many routes dispatching to many fn.
  Used by Tyler in bio-siting.
  On the fence if need this for bofhbotD

* reqparse, for parsing request (as body in POST?)
  similar to argparse
  But said to be deprecating in flask 2.0
  Recommend use like marshmallow, 
  but flask RESTful doc still written with reqparse (only).

* marshmallow
  really a object serialization library
  convert ORM/ODM or any complex data types (to json)
  Serialize/Deserialize/Validate fn in the library
  reqparse would be more familiar to me at this point.
  marshmallow is said to do a better job, but also covering lot more things?
    - Maybe more object based and easier to modify and resuse
      https://marshmallow.readthedocs.io/en/3.0/why.html


* 
