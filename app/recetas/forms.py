from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField,FloatField, SelectField
from wtforms.validators import DataRequired, URL, email_validator
from flask_ckeditor import CKEditorField

class SearchForm(FlaskForm):
    texto = StringField("Texto", validators=[DataRequired()])
    submit = SubmitField("BUSCAR")


class NewRecetaForm(FlaskForm):
    nombre = StringField("Nombre", validators=[DataRequired()])
    rendimiento = FloatField('Cantidad resultante', validators=[DataRequired()])
    unidad = SelectField('Unidades de Medida', choices = [], validate_choice=False)
    indicaciones =  CKEditorField("Indicaciones", validators=[DataRequired()])
    submit = SubmitField("CREAR")


class NewIngredienteForm(FlaskForm):
    cantidad = FloatField('Cantidad a agregar', validators=[DataRequired()])
    ingrediente = SelectField('Ingrediente', coerce=int,choices = [],  validate_choice=False)
    submit = SubmitField("AGREGAR")


