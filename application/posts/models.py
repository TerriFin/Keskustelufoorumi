from application import db

class Post(db.Model):
    PostId = db.Column(db.Integer, primary_key = True)
    PostDate = db.Column(db.DateTime, default = db.func.current_timestamp())
    ModifyDate = db.Column(db.DateTime, default = db.func.current_timestamp(),
    onupdate = db.func.current_timestamp())

    PostName = db.Column(db.String(300), nullable = False)

    Comments = db.relationship("Comment", backref='Post')

    def __init__(self, postName):
        self.PostName = postName