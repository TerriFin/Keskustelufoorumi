from application import app, db
from flask import render_template, request, url_for, redirect
from application.posts.models import Post

@app.route("/posts/new/", methods=["GET"])
def posts_form():
    return render_template("posts/new.html")

@app.route("/posts/", methods=["POST"])
def posts_create():
    post = Post(request.form.get("postName"))

    db.session().add(post)
    db.session().commit()

    return redirect(url_for("posts_index"))

@app.route("/posts/", methods=["GET"])
def posts_index():
    return render_template("posts/list.html", posts = Post.query.all())