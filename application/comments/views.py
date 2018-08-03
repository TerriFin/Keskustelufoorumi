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

@app.route("/commentsdelete/<PostId>/", methods=["POST"])
def delete_comment(PostId):
    comment = Comment.query.get(request.form.get("comment_to_delete"))

    db.session().delete(comment)
    db.session().commit()

    return redirect(url_for("show_comments", PostId=PostId))

@app.route("/commentsupdate/<PostId>/", methods=["POST"])
def show_comment_update_form(PostId):
    comment = Comment.query.get(request.form.get("comment_to_update"))

    return render_template("comments/updateCommentForm.html", PostId=PostId, CommentId=comment.CommentId, CommentContent=comment.CommentContent)

@app.route("/commentsupdatenow/<PostId>/", methods=["POST"])
def update_comment(PostId):
    comment = Comment.query.get(request.form.get("comment_to_update"))

    comment.CommentContent = request.form.get("updated_comment_content")
    db.session().commit()

    return redirect(url_for("show_comments", PostId=PostId))