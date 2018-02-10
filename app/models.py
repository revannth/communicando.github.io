#models.py

from app import db
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import UserMixin

class Participant(db.Model):
	name = db.Column(db.String(128),nullable=False)
	email = db.Column(db.String(128),unique=True,nullable=False)
	college = db.Column(db.String(240),nullable=False)
	mobile = db.Column(db.Integer)
	event = db.Column(db.String(10),nullable=False)


class Login(UserMixin,db.Model):
	id = db.Column(db.Integer,primary_key = True)
	username = db.Column(db.String(64),unique=True)
	password_hash = db.Column(db.String(128))
	


	@property
	def password(self):
		raise AttributeError('password is not a readable entity')

	@password.setter
	def password(self,password):
		self.password_hash = generate_password_hash(password)

	def verify_password(self,password):
		return check_password_hash(self.password_hash,password)



