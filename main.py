# from flask import Flask,g,abort, render_template, redirect, url_for, request, flash
# from flask_bootstrap import Bootstrap
# from wtforms import StringField, SubmitField
# from wtforms.validators import DataRequired, URL
# from forms import SearchForm,EditPropiedadForm, NewEquivalenteForm
# from models import Equivalente,Grupo, Concepto, Propiedad
# from flask_sqlalchemy import SQLAlchemy
# from sqlalchemy import Integer
# from sqlalchemy.orm import Mapped
# from sqlalchemy.orm import mapped_column
# from sqlalchemy.orm import DeclarativeBase
# from sqlalchemy.orm import relationship
# from sqlalchemy.orm import lazyload
# import os.path


# app = Flask(__name__)
# file_path = os.path.abspath(os.getcwd())+"/data/nutri.db"

# app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'+ file_path
# db = SQLAlchemy(app)


# Bootstrap(app)

import app as application


if __name__ == "__main__":
    # app.run(debug=True,port=5001)
    app = application.create_app()
    app.run(host="0.0.0.0",port=5000)    