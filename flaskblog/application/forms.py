from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileRequired, FileAllowed
from werkzeug.utils import secure_filename
from wtforms import StringField, SubmitField, PasswordField, BooleanField, TextAreaField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from application.models import Users, Posts, BucketList
from flask_login import current_user, LoginManager

class PostForm(FlaskForm):
	title = StringField('Title',
		validators=[
			DataRequired(),
			Length(min=4, max=100)
		])
	content = TextAreaField('Content',
		validators=[
			DataRequired(),
			Length(min=4, max=10000)
		])
	picture = FileField('Add photo to post',
		validators=[
			FileAllowed(['jpg', 'png', 'jpeg'])
		])
	submit = SubmitField('Post Content')

class RegistrationForm(FlaskForm):
	first_name = StringField('First Name: ',
		validators=[
			DataRequired(),
			Length(min=2, max=30)
		],
		render_kw={"placeholder": "First Name"})
	last_name = StringField('Last Name: ',
		validators=[
			DataRequired(),
			Length(min=2, max=30)
		],
		render_kw={"placeholder": "Last Name"})
	email = StringField('Email: ',
		validators=[
			DataRequired(),
			Email()
		],
		render_kw={"placeholder": "Email"})
	username = StringField('Username: ',
		validators=[
			DataRequired(),
			Length(min=3, max=50)
		],
		render_kw={"placeholder": "Username"})
	password = PasswordField('Password: ',
		validators=[
			DataRequired()
		],
		render_kw={"placeholder": "Password"})
	confirm_password = PasswordField('Confirm Password: ',
		validators=[
			DataRequired(),
			EqualTo('password')
		],
		render_kw={"placeholder": "Confirm Password"})
	submit = SubmitField('Sign Up')

	def validate_email(self, email):
		user = Users.query.filter_by(email=email.data).first()
		if user:
			raise ValidationError('Email already in use!')

	def validate_username(self, username):
		user = Users.query.filter_by(username=username.data).first()
		if user:
			raise ValidationError('Username already in use!')

class LoginForm(FlaskForm):
	email = StringField('Email',
		validators=[
			DataRequired(),
			Email()
		])
	password = PasswordField('Password',
		validators=[
			DataRequired()
		])
	remember = BooleanField('Remember Me')
	submit = SubmitField('Login')

class UpdateAccountForm(FlaskForm):
	username = StringField('Username',
		validators=[
			DataRequired()
		])
	first_name = StringField('First Name',
		validators=[
			DataRequired(),
			Length(min=2, max=30)
		])
	last_name = StringField('Last Name',
		validators=[
			DataRequired(),
			Length(min=2, max=30)
		])
	email = StringField('Email',
		validators=[
			DataRequired(),
			Email()
		])
	picture = FileField('Update Profile Picture',
		validators=[
			FileAllowed(['jpg', 'png', 'jpeg'])
		])
	
	submit = SubmitField('Update')

	def validate_email(self, email):
		if email.data != current_user.email:
			user = Users.query.filter_by(email=email.data).first()
			if user:
				raise ValidationError('Email already in use - Please choose another!')

	def validate_username(self, username):
		if username.data != current_user.username:
			user = Users.query.filter_by(username=username.data).first()
			if user:
				raise ValidationError('Username already in use - Please choose another!')

class BucketListForm(FlaskForm):
	title = StringField('Title',
		validators=[
			DataRequired(),
			Length(min=4, max=100)
		])
	description = TextAreaField('Description',
		validators=[
			DataRequired(),
			Length(min=4, max=10000)
		])
	due_date = StringField('Due Date',
		validators=[
		])
	submit = SubmitField('Add to Bucket List')





