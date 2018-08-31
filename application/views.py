from flask import render_template
from application import app, login_required
from application.posts.models import Post
from application.auth.models import User

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/hall_of_fame/")
def hallOfFame():
    response = Post.get_the_post_with_most_comments()

    return render_template("hallOfFame.html", bestPost = response[0], bestPostPoster = User.query.get(response[1]).username, numberOfComments = response[2])

@app.route("/admin_test/")
@login_required("Admin")
def admin_test():
    return render_template("adminTest.html")