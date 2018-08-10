from flask_wtf import FlaskForm
from wtforms import StringField, validators

class CommentForm(FlaskForm):
    comment = StringField("Comment", [validators.Length(min=2)])

    class Meta:
        csrf = False