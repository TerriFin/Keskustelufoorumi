from application import db
from application.models import Base

from sqlalchemy.sql import text

class Post(Base):

    postName = db.Column(db.String(300), nullable = False)

    accountId = db.Column(db.Integer, db.ForeignKey('account.id'), nullable=False)

    comments = db.relationship("Comment", backref='post')

    def __init__(self, name):
        self.postName = name

    @staticmethod
    def get_the_post_with_most_comments():
        stmt = text("SELECT post.postName, post.accountId, COUNT(comment.id) FROM post"
            " LEFT JOIN comment ON comment.postId = post.id"
            " GROUP BY post.postName"
            " ORDER BY Count(comment.id) DESC"
            " LIMIT 1")

        return db.engine.execute(stmt)