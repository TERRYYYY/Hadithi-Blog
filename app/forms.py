from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField
from wtforms.validators import Required

class BlogForm(FlaskForm):

    title = StringField('Blog title',validators=[Required()])
    sub-title = StringField('Blog sub-title',validators=[Required()])
    content = TextAreaField('Content', validators=[Required()])
    submit = SubmitField('Submit')