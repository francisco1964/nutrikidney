from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, SelectField
from wtforms.validators import DataRequired, URL, email_validator


class SearchForm(FlaskForm):
    texto = StringField("Texto", validators=[DataRequired()])
    submit = SubmitField("BUSCAR")


class NewEquivalenteForm(FlaskForm):
    nombre = StringField("Nombre", validators=[DataRequired()])
    grupo = SelectField('Grupo', coerce=int,choices = [],  validate_choice=False)
    submit = SubmitField("CREAR")


class EditPropiedadForm(FlaskForm):
    texto = StringField("Nuevo Valor", validators=[DataRequired()])
    submit = SubmitField("CAMBIAR")

