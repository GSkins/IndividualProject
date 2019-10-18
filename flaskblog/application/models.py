from application import db, login_manager
from flask_login import UserMixin
from datetime import datetime

class Posts(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	title = db.Column(db.String(200), nullable=False, unique=False)
	content = db.Column(db.String(10000), nullable=False, unique=False)
	date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
	image_file = db.Column(db.String(60), nullable=False, default='blank.jpg')

	user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)

	def __repr__(self):
		return ''.join([
			'User ID: ', self.user_id, '\r\n',
			'Title: ', self.title, '\r\n', self.content])

class Users(db.Model, UserMixin):
	id = db.Column(db.Integer, primary_key=True)
	first_name = db.Column(db.String(30), nullable=False)
	last_name = db.Column(db.String(30), nullable=False)
	email = db.Column(db.String(150), nullable=False, unique=True)
	username = db.Column(db.String(50), nullable=False, unique=True)
	image_file = db.Column(db.String(60), nullable=False, default='test.jpg')
	password = db.Column(db.String(50), nullable=False)
	posts = db.relationship('Posts', backref='author', lazy=True)
	bucket_list = db.relationship('BucketList', backref='author_of_list', lazy=True)

	def __repr__(self):
		return ''.join(['User ID: ', str(self.id), '\r\n', 
			'Email: ', self.email, '\r\n', 'Username: ', self.username, '\r\n', 
			'Name: ', self.first_name, ' ', self.last_name])

class BucketList(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	title = db.Column(db.String(200), nullable=False, unique=False)
	description = db.Column(db.String(200), nullable=False, unique=False)
	created_on = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
	due_date = db.Column(db.String(11), nullable=False, default='Not set')
	_is_deleted = db.Column(db.Boolean, nullable=False, default=False)
	_is_done = db.Column(db.Boolean, nullable=False, default=False)
	user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)

	def __repr__(self):
		return ''.join([
			'User ID: ', str(self.id), '\r\n',
			'Title: ', self.title, '\r\n', 'Description: ', self.description
			, '\r\n', 'Due Date: ', self.due_date])

@login_manager.user_loader
def load_user(user_id):
	return Users.query.get(user_id)
