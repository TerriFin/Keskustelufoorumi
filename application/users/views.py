from application import app, db, login_required
from application.auth.models import User
from flask import render_template, request, url_for, redirect

@app.route("/users/", methods=["GET"])
def users_index():
    return render_template("users/userList.html", users = User.query.all())

@app.route("/user/<UserId>/", methods=["GET"])
@login_required()
def user_page(UserId):
    u = User.query.get(UserId)

    return render_template("users/userpage.html", user = u)