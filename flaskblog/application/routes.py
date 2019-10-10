from flask import render_template, redirect, url_for, request, abort
from application import app, db, bcrypt
from application.models import Posts, Users, BucketList
from application.forms import PostForm, RegistrationForm, LoginForm, UpdateAccountForm, BucketListForm
from flask_login import LoginManager, login_user, current_user, logout_user, login_required
import os
from secrets import *
from PIL import Image

@app.route('/home')
@app.route('/')
def home():
	postData = Posts.query.all()
	return render_template('home.html', title='Home')

@app.route('/ideas')
def ideas():
	return render_template('ideas.html', title='Ideas')

@app.route('/login', methods=['GET','POST'])
def login():
	if current_user.is_authenticated:
		return redirect(url_for('home'))
	form = LoginForm()
	if form.validate_on_submit():
		user = Users.query.filter_by(email=form.email.data).first()
		if user and bcrypt.check_password_hash(user.password, form.password.data):
			login_user(user, remember=form.remember.data)
			next_page = request.args.get('next')
			if next_page:
				return redirect(next_page)
			else:
				return redirect(url_for('home'))	
	return render_template('login.html', title='Login', form=form)

@app.route('/logout')
def logout():
	logout_user()
	return redirect(url_for('login'))

@app.route('/register', methods=['GET','POST'])
def register():
	if current_user.is_authenticated:
		return redirect(url_for('home'))
	form = RegistrationForm()
	if form.validate_on_submit():
		hashed_pw = bcrypt.generate_password_hash(form.password.data)
		user = Users(
			first_name=form.first_name.data,
			last_name=form.last_name.data,
			username=form.username.data,
			email=form.email.data,
			password=hashed_pw)
		db.session.add(user)
		db.session.commit()
		return redirect(url_for('community'))
	return render_template('register.html', title='Register', form=form)


def save_picture(form_picture):
	random_hex = secrets.token_hex(8)
	_, f_ext = os.path.splitext(form_picture.filename)
	picture_fn = random_hex + f_ext
	picture_path = os.path.join(app.root_path, 'static/ProfilePics', picture_fn)

	output_size = (125, 125)
	i = Image.open(form_picture)
	i.thumbnail(output_size)
	i.save(picture_path)

	return picture_fn

@app.route('/account', methods=['GET','POST'])
@login_required
def account():
	form = UpdateAccountForm()
	if form.validate_on_submit():
		if form.picture.data:
			picture_file = save_picture(form.picture.data)
			current_user.image_file = picture_file
		current_user.username = form.username.data
		current_user.first_name = form.first_name.data
		current_user.last_name = form.last_name.data
		current_user.email = form.email.data
		db.session.commit()
		return redirect(url_for('account'))
	elif request.method == 'GET':
		form.username.data = current_user.username
		form.first_name.data = current_user.first_name
		form.last_name.data = current_user.last_name
		form.email.data = current_user.email
	image_file = url_for('static', filename='ProfilePics/' + current_user.image_file)
	return render_template('account.html', title='Account', form=form, image_file=image_file)

@app.route('/community', methods=['GET', 'POST'])
def community():
	postData = Posts.query.all()
	return render_template('community.html', title='Community', posts=postData)

@app.route('/communitypost', methods=['GET','POST'])
@login_required
def communitypost():
	form = PostForm()
	if form.validate_on_submit():
		postData = Posts(
				title=form.title.data,
				content=form.content.data,
				author=current_user
			)
		db.session.add(postData)
		db.session.commit()
		return redirect(url_for('community'))
	else:
		print(form.errors)
	return render_template('communitypost.html', title='Post to Community', form=form, legend='Add Post')

@app.route('/communitypost/<int:post_id>')
def post(post_id):
	postData = Posts.query.get_or_404(post_id)
	return render_template('post.html', title=postData.title, post=postData)

@app.route('/communitypost/<int:post_id>/update', methods=['GET', 'POST'])
@login_required
def update_post(post_id):
	postData = Posts.query.get_or_404(post_id)
	if postData.author != current_user:
		abort(403)
	form = PostForm()
	if form.validate_on_submit():
		postData.title = form.title.data
		postData.content = form.content.data
		db.session.commit()
		return redirect(url_for('community'))
	elif request.method == 'GET':
		form.title.data = postData.title
		form.content.data = postData.content
	form.title.data = postData.title
	form.content.data = postData.content
	return render_template('communitypost.html', title='Update Post', form=form, legend='Update Post')

@app.route('/communitypost/<int:post_id>/delete', methods=['POST'])
@login_required
def delete_post(post_id):
	postData = Posts.query.get_or_404(post_id)
	if postData.author != current_user:
		abort(403)
	db.session.delete(postData)
	db.session.commit()
	return redirect(url_for('community'))

@app.route('/my_bucket_list', methods=['GET','POST'])
@login_required
def my_bucket_list():
	BucketListData = BucketList.query.all()
	return render_template('my_bucket_list.html', title='My Bucket List', posts=BucketListData)

@app.route('/add_to_my_bucket_list', methods=['GET','POST'])
@login_required
def add_to_list():
	form = BucketListForm()
	if form.validate_on_submit():
		BucketListData = BucketList(
				title=form.title.data,
				description=form.description.data,
				due_date=form.due_date.data,
				author_of_list=current_user
			)
		db.session.add(BucketListData)
		db.session.commit()
		return redirect(url_for('my_bucket_list'))
	else:
		print(form.errors)
	return render_template('add_to_my_bucket_list.html', title='Add To My Bucket List', form=form)

@app.route('/my_bucket_list/<int:post_id>')
def list_item(post_id):
	BucketListData = BucketList.query.get_or_404(post_id)
	return render_template('list_item.html', title=BucketListData.title, post=BucketListData)


@app.route('/add_to_my_bucket_list/<int:post_id>/update', methods=['GET', 'POST'])
@login_required
def update_item(post_id):
	BucketListData = BucketList.query.get_or_404(post_id)
	if BucketListData.author_of_list != current_user:
		abort(403)
	form = BucketListForm()
	if form.validate_on_submit():
		BucketListData.title = form.title.data
		BucketListData.description = form.description.data
		BucketListData.due_date = form.due_date.data
		db.session.commit()
		return redirect(url_for('my_bucket_list'))
	elif request.method == 'GET':
		form.title.data = BucketListData.title
		form.description.data = BucketListData.description
		form.due_date.data = BucketListData.due_date
	form.title.data = BucketListData.title
	form.description.data = BucketListData.description
	form.due_date.data = BucketListData.due_date
	return render_template('add_to_my_bucket_list.html', title='Update Item in List', form=form)

@app.route('/add_to_my_bucket_list/<int:post_id>/delete', methods=['POST'])
@login_required
def delete_item(post_id):
	BucketListData = BucketList.query.get_or_404(post_id)
	if BucketListData.author_of_list != current_user:
		abort(403)
	db.session.delete(BucketListData)
	db.session.commit()
	return redirect(url_for('my_bucket_list'))
