from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
import os
import pymysql

POST_PHOTO_FOLDER = os.path.join('static', 'CommunityPhotos')

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:password@mysql:3306/flask_database'
app.config['SECRET_KEY'] = 'secretkeyexample'
app.config['UPLOAD_FOLDER'] = POST_PHOTO_FOLDER

db = SQLAlchemy(app)
bcrypt = Bcrypt(app)

login_manager = LoginManager(app)
login_manager.login_view = 'login'

from application import routes

