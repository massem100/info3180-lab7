from flask_wtf import FlaskForm
from wtforms import  TextAreaField
from wtforms.validators import InputRequired, Email
from flask_wtf.file import FileField, FileAllowed, FileRequired

class UploadForm(FlaskForm):
    description = TextAreaField('Description', validators=[InputRequired(message='A description is required.')])
    photo = FileField('Photo', validators=[FileRequired('No photo was submitted.'), FileAllowed(['jpg', 'jpeg', 'png'], 'Images only!')])
