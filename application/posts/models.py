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
        stmt = text('SELECT Post."postName", Post."accountId", COUNT(Comment.id) FROM Post LEFT JOIN Comment ON Post.id = comment."postId" GROUP BY Post."postName", Post."accountId" ORDER BY Count(Comment.id) DESC LIMIT 1;')

        res = db.engine.execute(stmt)

        response = []
        for row in res:
            response.append(row[0])
            response.append(row[1])
            response.append(row[2])

        return response