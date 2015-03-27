from app import db
#from datetime import datetime
from app.users import constants as USER

class TOS(db.Model):
	__tablename__ = 'tos'
	id = db.Column(db.Integer, primary_key=True)
	date = db.Column(db.DateTime)
	title = db.Column(db.String(500))
	text = db.Column(db.String(5000))

	def __init__(self, date=None, title=None, text=None):
		self.date = date
		self.title = title
		self.text = text
	
	def __repr__(self):
		return '<TOS [title:%r date:%r>' % (self.title, self.date)
