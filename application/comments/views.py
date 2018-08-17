from application import app, db
from flask import render_template, request, url_for, redirect
from application.posts.models import Post
from application.comments.forms import CommentForm
from flask_login import login_required, current_user
from application.comments.models import Comment

@app.route("/comments/<PostId>/", methods=["GET"])
def show_comments(PostId):
    p = Post.query.get(PostId)

    return render_template("comments/comments.html", PostName = p.postName, Comments = p.comments, PostID = p.id, form = CommentForm())

@app.route("/comments/<PostId>/", methods=["POST"])
@login_required
def create_comment(PostId):
    form = CommentForm(request.form)

    if not form.validate():
        p = Post.query.get(PostId)

        return render_template("comments/comments.html", PostName = p.postName, Comments = p.comments, PostID = p.id, form = form)


    newComment = Comment(form.comment.data)
    newComment.postId = PostId
    newComment.accountId = current_user.id

    db.session().add(newComment)
    db.session().commit()

    return redirect(url_for("show_comments", PostId=PostId))

@app.route("/commentsdelete/<PostId>/", methods=["POST"])
@login_required
def delete_comment(PostId):
    comment = Comment.query.get(request.form.get("comment_to_delete"))

    if not current_user.id == comment.account.id:
        p = Post.query.get(PostId)

        return render_template("comments/comments.html", PostName = p.postName, Comments = p.comments, PostID = p.id, form = CommentForm, error = "You are trying to remove a comment you did not make!")

    db.session().delete(comment)
    db.session().commit()

    return redirect(url_for("show_comments", PostId=PostId))

@app.route("/commentsupdate/<PostId>/", methods=["POST"])
@login_required
def show_comment_update_form(PostId):
    comment = Comment.query.get(request.form.get("comment_to_update"))

    if not current_user.id == comment.account.id:
        p = Post.query.get(PostId)

        return render_template("comments/comments.html", PostName = p.postName, Comments = p.comments, PostID = p.id, form = CommentForm, error = "You are trying to edit a comment you did not make!")

    form = CommentForm()
    form.comment.data = comment.commentContent

    return render_template("comments/updateCommentForm.html", PostId=PostId, CommentId=comment.id, form=form)

@app.route("/commentsupdatenow/<PostId>/", methods=["POST"])
@login_required
def update_comment(PostId):
    comment = Comment.query.get(request.form.get("comment_to_update"))

    if not current_user.id == comment.account.id:
        p = Post.query.get(PostId)

        return render_template("comments/comments.html", PostName = p.postName, Comments = p.comments, PostID = p.id, form = CommentForm, error = "You are trying to edit a comment you did not make!")

    
    form = CommentForm(request.form)

    if not form.validate():
        return render_template("comments/updateCommentForm.html", PostId=PostId, CommentId=request.form.get("comment_to_update"), form=form)

    comment.commentContent = form.comment.data
    db.session().commit()

    return redirect(url_for("show_comments", PostId=PostId))