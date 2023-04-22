from app.extensions import db
from sqlalchemy.orm import mapped_column
from sqlalchemy import Integer, Float, Text
from sqlalchemy.orm import relationship
# from app.models.grupo import Grupo


class Receta(db.Model):
    # id = db.Column(db.Integer, primary_key=True)
    id =  mapped_column(Integer, primary_key=True)
    nombre = db.Column(db.String(100), unique=True, nullable=False)
    rendimiento = db.Column(db.Float, nullable=False)
    unidad = db.Column(db.String(20), nullable=False)
    indicaciones = db.Column(db.Text())
    # componentes = relationship("Componente", back_populates="receta")

    def __repr__(self):
        return f'<Equivalente "{self.nombre}">'