from flask_wtf import FlaskForm
from wtforms import StringField, validators

class PostForm(FlaskForm):
    name = StringField("Post name", [validators.Length(min=3)])

    class Meta:
        csrf = False