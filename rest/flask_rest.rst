
following 
https://flask-restful.readthedocs.io/en/latest/quickstart.html
to try sketching a rest skeleton for bofhbot daemon.

cd flask/
virtualenv --python=python3 venv4flask
source     venv4flask/bin/activate

pip install flask-restful

python api.py 0:5000 




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

