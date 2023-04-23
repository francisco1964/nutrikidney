from typing import List
from app.extensions import db
from sqlalchemy.orm import mapped_column, Mapped
from sqlalchemy import Integer, Float, Text, ForeignKey
from sqlalchemy.orm import relationship
from app.models.equivalente import Equivalente
from typing import Optional




class Receta(db.Model):
    # id = db.Column(db.Integer, primary_key=True)
    id =  mapped_column(Integer, primary_key=True)
    nombre = db.Column(db.String(100), unique=True, nullable=False)
    rendimiento = db.Column(db.Float, nullable=False)
    unidad = db.Column(db.String(20), nullable=False)
    indicaciones = db.Column(db.Text())
    ingredientes = relationship("Ingrediente", back_populates="receta",foreign_keys='Ingrediente.receta_id')

    def __repr__(self):
        return f'<Receta "{self.nombre}">'
    



class Ingrediente(db.Model):
    # id = db.Column(db.Integer, primary_key=True)
    id =  mapped_column(Integer, primary_key=True)
    receta_id : Mapped[Optional[int]] = mapped_column(ForeignKey("receta.id"))
    receta = relationship("Receta", foreign_keys=[receta_id], back_populates="ingredientes", lazy="joined")
    cantidad = db.Column(db.Float, nullable=False)
    equivalente_id : Mapped[Optional[int]] = mapped_column(ForeignKey("equivalente.id"))
    equivalente = relationship("Equivalente", lazy="joined")
    componente_id : Mapped[Optional[int]] = mapped_column(ForeignKey("receta.id"))
    componente = relationship("Receta", foreign_keys=[componente_id], lazy="joined")
    # equivalente = relationship("Equivalente", back_populates="propiedades", lazy="joined")
    # propiedades = relationship("Propiedad", back_populates="equivalente")

    def __repr__(self):
        if self.componente != None:
            return f'<Ingrediente "{self.componenete.nombre}">'
        if self.equivalente != None:
            return f'<Ingrediente "{self.equivalente.nombre}">'
        return '<Ingrediente desconocido>'