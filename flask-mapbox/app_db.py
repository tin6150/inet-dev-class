# https://opensource.com/article/18/4/flask
# db part

### have not gotten it to work.
### not too meaningful.  abandoning for now.

from datetime import datetime
from flask import request, Response
from flask_sqlalchemy import SQLAlchemy
import json

from .models import Task, User


user = User.query.filter_by(username=username).first()


task = Task(
    name=request.form['name'],
    note=request.form['note'],
    creation_date=datetime.now(),
    due_date=datetime.strptime(due_date, INCOMING_DATE_FMT) if due_date else None,
    completed=bool(request.form['completed']),
    user_id=user.id,
)


db.session.add(task)
db.session.commit()



output = {'msg': 'posted'}
response = Response(
    mimetype="application/json",
    response=json.dumps(output),
    status=201
)


app = Flask(__name__)
#app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL', '')
DATABASE_URL = 'sqlite:///tin_appdb_sqlite.db'
app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_URL
db = SQLAlchemy(app)

INCOMING_DATE_FMT = '%d/%m/%Y %H:%M:%S'

@app.route('/api/v1/accounts/<username>/tasks', methods=['POST'])
def create_task(username):
    """Create a task for one user."""
    user = User.query.filter_by(username=username).first()
    if user:
        task = Task(
            name=request.form['name'],
            note=request.form['note'],
            creation_date=datetime.now(),
            due_date=datetime.strptime(due_date, INCOMING_DATE_FMT) if due_date else None,
            completed=bool(request.form['completed']),
            user_id=user.id,
        )
        db.session.add(task)
        db.session.commit()
        output = {'msg': 'posted'}
        response = Response(
            mimetype="application/json",
            response=json.dumps(output),
            status=201
        )
        return response

# end create_task()


