from flask import render_template
from application import app
from application.posts.models import Post
from application.auth.models import User

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/hall_of_fame")
def hallOfFame():
    postWithMostComments = Post.get_the_post_with_most_comments()

    for row in postWithMostComments:
        bestPostName = row[0]
        poster = User.query.get(row[1]).username
        numberOfComments = row[2]

    return render_template("hallOfFame.html", bestPost = bestPostName, bestPostPoster = poster, numberOfComments = numberOfComments)