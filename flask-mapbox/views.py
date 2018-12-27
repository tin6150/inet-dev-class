
"""
Use Flask blueprints to load bunch of views in one go.
app.py flask app has this clause:
	from views import master

modeled after Tyler Biositting views.py
Tin (at) LBL.gov
"""


from flask.blueprints import Blueprint
from flask import render_template	# jinga2 template to escape html


master = Blueprint('master', __name__,
                template_folder='templates',
                static_folder='../static')     # static was used for .js


@master.after_request
def add_header(r):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also to cache the rendered page for 10 minutes.
    """
    r.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    r.headers["Pragma"] = "no-cache"
    r.headers["Expires"] = "0"
    r.headers['Cache-Control'] = 'public, max-age=0'
    return r


@master.route('/')
@master.route('/ZWEDC_50x50sq')
def root():
    #error = None
    #form = LoginForm(request.form)
    #return(render_template('mbgl_index.html', error=error, form=form))
    return(render_template('ZWEDC_50x50sq.html'))
    # http://flask.pocoo.org/docs/1.0/quickstart/#rendering-templates # case 1

@master.route('/alviso')
def alviso():
    return render_template('alviso.html')

## 
@master.route('/about')
def showAbout():
    return(render_template('about.html'))  # static HTML w/o JINJA2 template clause is okay too.  
    # http://flask.pocoo.org/docs/1.0/quickstart/#rendering-templates
    #error = None
    #form = LoginForm(request.form)
    #return(render_template('about.html', error=error, form=form))


# need define bothversion with or without tailing slash, or else web brwoser hangs waiting for timeout
@master.route('/hello')
@master.route('/hello/')
@master.route('/hello/<name>')
def hello(name=None):
    return render_template('hello.html', name=name)
    # http://flask.pocoo.org/docs/1.0/quickstart/#rendering-templates # case 2



## below don't work yet
## but flask app can work without them 
## may need them in near future

# Set the basemap with county biomass totals to geojson for visualization
@master.route("/basemap")
def getCounties():
  return flask.jsonify({'biomass': gpd_to_geojson(counties_df, cols_counties),
                        'thermal': gpd_to_geojson(thermal, cols_thermal)})

# Convert biomass points to geojson for visualization
@master.route("/points")
def getPoints():
  return flask.jsonify({'AD': gpd_to_geojson(AD_pts, cols_AD_pts),
                        'COMB': gpd_to_geojson(COMB_pts, cols_COMB_pts),
                        'W2E': gpd_to_geojson(W2E_pts, cols_W2E_pts),
                        })


