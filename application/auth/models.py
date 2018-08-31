from application import db
from application.models import Base

class User(Base):

    __tablename__ = "account"

    username = db.Column(db.String(150), nullable = False)
    password = db.Column(db.String(150), nullable = False)

    role = db.Column(db.String(100), nullable = False)

    posts = db.relationship("Post", backref='account')
    comments = db.relationship("Comment", backref='account')

    def __init__(self, username, password, role):
        self.username = username
        self.password = password
        self.role = role


    def get_id(self):
        return self.id

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def is_authenticated(self):
        return True