from app.extensions import db
from sqlalchemy.orm import mapped_column
from sqlalchemy import Integer


##CREATE TABLE IN DB
class Grupo(db.Model):
    # id = db.Column(db.Integer, primary_key=True)
    id =  mapped_column(Integer, primary_key=True)
    nombre = db.Column(db.String(100), unique=True)
 
    def __repr__(self):
        return f'<Grupo "{self.nombre}">'