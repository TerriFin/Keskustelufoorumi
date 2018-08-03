from application import app, db
from flask import render_template, request, url_for, redirect
from application.posts.models import Post
from application.comments.models import Comment

@app.route("/comments/<PostId>/", methods=["GET"])
def show_comments(PostId):
    p = Post.query.get(PostId)

    return render_template("comments/comments.html", PostName = p.PostName, Comments = p.Comments, PostID = p.PostId)

@app.route("/comments/<PostId>/", methods=["POST"])
def create_comment(PostId):
    newComment = Comment(request.form.get("newComment"))

    newComment.PostId = PostId

    db.session().add(newComment)
    db.session().commit()

    return redirect(url_for("show_comments", PostId=PostId))