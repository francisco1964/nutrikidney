from datetime import date
import requests
import json
import csv
import os.path
import sys




# file_path = "/home/paco/Documentos/bmv"

# INPUT_FILE = "files/Verduras.csv"
INPUT_FILE = "files/"
OUTPUT_FILE = "equivalentes.csv"

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