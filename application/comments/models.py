from application import db
from application.models import Base

class Comment(Base):

    commentContent = db.Column(db.String(500), nullable = False)

    postId = db.Column(db.Integer, db.ForeignKey('post.id'), nullable=False)
    accountId = db.Column(db.Integer, db.ForeignKey('account.id'), nullable=False)

    def __init__(self, content):
        self.commentContent = content