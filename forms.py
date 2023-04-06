from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField
from wtforms.validators import DataRequired, URL, email_validator


class SearchForm(FlaskForm):
    texto = StringField("Texto", validators=[DataRequired()])
    submit = SubmitField("BUSCAR")