from datetime import date
import requests
import json
import csv
import os.path
import sys
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import mapped_column
from sqlalchemy import Integer
from flask import Flask
# Carga los datos de los equivalentes del 
# SMAE, Sistema Mexicano de Equivalentes Nutricionales.

app = Flask(__name__)

# file_path = "/home/paco/Documentos/bmv"

# INPUT_FILE = "files/Verduras.csv"
INPUT_FILE = "files/"
OUTPUT_FILE = "equivalentes.csv"


#Crer la base de datos y la tabla de equivalentes.
file_path = os.path.abspath(os.getcwd())+"/data/nutrikidney.db"

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'+ file_path
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

##CREATE TABLE IN DB
db = SQLAlchemy(app)
class Equivalente(db.Model):
    # id = db.Column(db.Integer, primary_key=True)
    id =  mapped_column(Integer, primary_key=True)
    grupo = db.Column(db.String(100))
    nombre = db.Column(db.String(100), unique=True)
    concepto = db.Column(db.String(100))
    valor = db.Column(db.String(10))



#Line below only required once, when creating DB. 
with app.app_context():
   db.create_all()


def get_files(path):
    for file in os.listdir(path):
        if os.path.isfile(os.path.join(path, file)):
            yield file


data = None
GRUPO = 0
NOMBRE = 1

for f in get_files('files/'):
    INPUT_FILE = "files/"+f
    with open(INPUT_FILE, "r") as file:
        data = list(csv.reader(file, delimiter=","))


    keys =[x for ind, x in enumerate(data[0]) if  ind > 1]
    # print(nombre)    
    # print(keys)

    # print(data[1:2])

    grupo =""
    equivalente = ""
    aportes = data[0][2:]

    for item in data[1:]:
        rango = range(len(aportes))
        for x in rango:
            grupo = item[GRUPO]
            nombre = item[NOMBRE]
            aporte = aportes[x]
            cantidad = item[x+2]
            print(f"{grupo},{nombre},{aporte},{cantidad}")
            
    # print(grupo,nombre,aportes)




if __name__ == "__main__":
    # app.run(debug=True,port=5001)
    app.run(host="0.0.0.0",port=5000)