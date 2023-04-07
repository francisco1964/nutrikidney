from flask import Flask,g,abort, render_template, redirect, url_for, request, flash
from flask_bootstrap import Bootstrap
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, URL
from forms import SearchForm,EditPropiedadForm
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




@app.route('/')
def get_all_posts():
    return render_template("index.html")


@app.route('/equivalentes', methods = ["GET", "POST"])
def get_equivalentes():
    form = SearchForm()
    equivalentes = []
    if form.validate_on_submit():
        with app.app_context():
            print("+++++++++++++++++++++++++++++")
            equivalentes = db.session.query(Equivalente).filter(Equivalente.nombre.contains(form.texto.data)).all()
            for equivalente in equivalentes:
                print(equivalente.nombre, \
                equivalente.propiedades[0].valor,\
                equivalente.propiedades[1].valor)
                for prop in equivalente.propiedades:
                    # print(prop.concepto.nombre, prop.valor)
                    pass


        print(form.texto.data)

    return render_template("equivalentes.html",form=form,equivalentes = equivalentes)

@app.route("/equivalente/<int:index>", methods=["GET", "POST"] )
def show_equivalente(index):
    eq = None
    with app.app_context():
        eq = db.session.query(Equivalente).filter(Equivalente.id==index).first()
        return render_template("equivalente.html",equivalente = eq)
    
    return redirect(url_for("get_equivalentes"))


@app.route("/edit_equivalente/<int:index>", methods=["GET", "POST"] )
def edit_equivalente(index):
    return f"Ediatar equivalente { index} "


@app.route("/edit_prop/<int:index>", methods=["GET", "POST"] )
def edit_prop(index):
    # return f"Ediatar Propiedad { index} "
    form = EditPropiedadForm()
    prop = None


    if form.validate_on_submit(): 
        print(form.texto.data)
        with app.app_context():
            prop = db.session.query(Propiedad).filter(Propiedad.id==index).first()  
            db.session.query(Propiedad).filter(Propiedad.id==index).\
            update({'valor' : form.texto.data})
            db.session.commit()
            return redirect(url_for('show_equivalente',index=prop.equivalente.id))

    with app.app_context():
        prop = db.session.query(Propiedad).filter(Propiedad.id==index).first()
        form.texto.data = prop.valor 


    return render_template("edit_prop.html",form=form, prop = prop)




if __name__ == "__main__":
    # app.run(debug=True,port=5001)
    app.run(host="0.0.0.0",port=5000)