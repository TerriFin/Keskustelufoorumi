from application import db

class Comment(db.Model):
    CommentId = db.Column(db.Integer, primary_key = True)
    CommentDate = db.Column(db.DateTime, default = db.func.current_timestamp())
    ModifyDate = db.Column(db.DateTime, default = db.func.current_timestamp(),
    onupdate = db.func.current_timestamp())

    CommentContent = db.Column(db.String(500), nullable = False)

    PostId = db.Column(db.Integer, db.ForeignKey('post.PostId'), nullable=False)

    def __init__(self, commentContent):
        self.CommentContent = commentContent