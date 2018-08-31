from flask import render_template, request, redirect, url_for
from flask_login import login_user, logout_user

from application import app, db
from application.auth.models import User
from application.auth.forms import LoginForm, RegisterForm

@app.route("/auth/login", methods = ["GET"])
def auth_show_login():
    return render_template("auth/loginform.html", form = LoginForm())

@app.route("/auth/login", methods = ["POST"])
def auth_handle_login():
    form = LoginForm(request.form)

    user = User.query.filter_by(username = form.username.data, password = form.password.data).first()
    if not user:
        return render_template("auth/loginform.html", form = form, error = "No such username or password")

    login_user(user)
    return redirect(url_for("index"))

@app.route("/auth/logout")
def auth_logout():
    logout_user()
    return redirect(url_for("index"))

@app.route("/auth/register", methods = ["GET"])
def auth_show_register_form():
    return render_template("auth/registerform.html", form = RegisterForm())


@app.route("/auth/register", methods = ["POST"])
def auth_register_new_user():
    form = RegisterForm(request.form)

    if not form.validate():
        return render_template("auth/registerform.html", form = form)

    user = User.query.filter_by(username = form.username.data).first()

    if user:
        return render_template("auth/registerform.html", form = form, error = "This username is already taken")

    newUser = User(form.username.data, form.password.data, "User")
    
    db.session().add(newUser)
    db.session().commit()

    login_user(newUser)

    return redirect(url_for("index"))