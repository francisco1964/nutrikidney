from flask import Flask,g,abort, render_template, redirect, url_for, request, flash
from flask_bootstrap import Bootstrap
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, URL
from forms import SearchForm
from models import Equivalente,Grupo, Concepto, Propiedad
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Integer
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import relationship
from sqlalchemy.orm import lazyload
import os.path


app = Flask(__name__)
file_path = os.path.abspath(os.getcwd())+"/data/nutri.db"

app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'+ file_path
db = SQLAlchemy(app)


Bootstrap(app)


equivalentes = []


@app.route('/')
def get_all_posts():
    return render_template("index.html")


@app.route('/equivalentes', methods = ["GET", "POST"])
def get_equivalentes():
    form = SearchForm()
    
    if form.validate_on_submit():
        with app.app_context():
            result = db.session.query(Equivalente).filter(Equivalente.nombre.contains(form.texto.data)).all()
            print(result)

        print(form.texto.data)

    return render_template("equivalentes.html",form=form)



if __name__ == "__main__":
    # app.run(debug=True,port=5001)
    app.run(host="0.0.0.0",port=5000)