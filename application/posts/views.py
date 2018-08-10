from application import app, db
from flask import render_template, request, url_for, redirect
from application.posts.models import Post
from application.posts.forms import PostForm
from flask_login import login_required

@app.route("/posts/new/", methods=["GET"])
@login_required
def posts_form():
    return render_template("posts/new.html", form = PostForm())

@app.route("/posts/", methods=["POST"])
@login_required
def posts_create():
    form = PostForm(request.form)

    if not form.validate():
        return render_template("posts/new.html", form = form)

    post = Post(form.name.data)

    db.session().add(post)
    db.session().commit()

    return redirect(url_for("posts_index"))

@app.route("/posts/", methods=["GET"])
def posts_index():
    return render_template("posts/list.html", posts = Post.query.all())