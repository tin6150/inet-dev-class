
## https://opensource.com/article/18/4/flask
## database part: models.py

from .app import db
from datetime import datetime

class Task(db.Model):
	"""Tasks for the To Do list."""
	id 	= db.Column(db.integer, primary_key=True)
	name 	= db.Column(db.Unicode, nullable=True)
	note	= db.Column(db.Unicode)
	creation_data = db.Column(db.DateTime, nullable=False)
	due_data 	= db.Column(db.DateTime)
	completed 	= db.Column(db.Boolean, default=False)

	def __init__(self, *args, **kwargs):
		"""On contruction, set date of creating..."""
		super().__init__(*args, **kwargs)
		self.createion_date = datetime.now()

