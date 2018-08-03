from flask import Flask
app = Flask(__name__)

from flask_sqlalchemy import SQLAlchemy

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///userPosts.db"

db = SQLAlchemy(app)

from application.posts import models
from application.comments import models

db.create_all()

from application import views
from application.posts import views
from application.comments import views