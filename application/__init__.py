# Set up flask
from flask import Flask
app = Flask(__name__)

# Set up sqlalchemy database
from flask_sqlalchemy import SQLAlchemy
import os

if os.environ.get("HEROKU"):
    app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("DATABASE_URL")
else:
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///userPosts.db"

db = SQLAlchemy(app)

# Import all the different models and initiate them as database if needed
from application.posts import models
from application.comments import models
from application.auth import models

db.create_all()

# Set up logging in
from application.auth.models import User
from os import urandom
app.config["SECRET_KEY"] = urandom(32)

from flask_login import LoginManager
login_manager = LoginManager()
login_manager.init_app(app)

login_manager.login_view = "auth_show_login"
login_manager.login_message = "STOP! YOU VIOLATED THE LAW! (please login to do this)"

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)

# Import all the different views this app has
from application import views
from application.posts import views
from application.comments import views
from application.auth import views