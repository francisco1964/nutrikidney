from flask import Flask
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

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'+ file_path
db = SQLAlchemy(app)



##CREATE TABLE IN DB
class Grupo(db.Model):
    # id = db.Column(db.Integer, primary_key=True)
    id =  mapped_column(Integer, primary_key=True)
    nombre = db.Column(db.String(100), primary_key=True)
 

class Concepto(db.Model):
    # id = db.Column(db.Integer, primary_key=True)
    id =  mapped_column(Integer, primary_key=True)
    nombre = db.Column(db.String(100), primary_key=True)

class Equivalente(db.Model):
    # id = db.Column(db.Integer, primary_key=True)
    id =  mapped_column(Integer, primary_key=True)
    nombre = db.Column(db.String(100), primary_key=True)    
    grupo_id = db.Column(db.Integer, db.ForeignKey("grupo.id"), nullable=False)

class Propiedad(db.Model):
    __tablename__ = 'propiedades'
    id =  mapped_column(Integer, primary_key=True)
    equivalente_id = db.Column(db.Integer, db.ForeignKey("equivalente.id"), nullable=False)
    concepto_id = db.Column(db.Integer, db.ForeignKey("concepto.id"), nullable=False)
    valor = db.Column(db.String(10), nullable = False) 


#Line below only required once, when creating DB. 
with app.app_context():
    db.create_all()



if __name__ == "__main__":
    # app.run(debug=True,port=5001)
    app.run(host="0.0.0.0",port=5000)