
## https://opensource.com/article/18/4/flask
## database part: initializedb.py



from todo.app import db
import os

if bool(os.environ.get('DEBUG', '')):
    db.drop_all()
db.create_all()
