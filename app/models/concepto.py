from app.extensions import db
from sqlalchemy.orm import mapped_column
from sqlalchemy import Integer
from sqlalchemy.orm import relationship


class Concepto(db.Model):
    # id = db.Column(db.Integer, primary_key=True)
    id =  mapped_column(Integer, primary_key=True)
    nombre = db.Column(db.String(100), unique=True)
    propiedades = relationship("Propiedad", back_populates="concepto")

    def __repr__(self):
        return f'<Concepto "{self.nombre}">'