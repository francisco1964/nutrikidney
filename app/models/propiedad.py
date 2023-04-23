from app.extensions import db
from sqlalchemy.orm import mapped_column
from sqlalchemy import Integer
from sqlalchemy.orm import relationship
from app.models.concepto import Concepto


class Propiedad(db.Model):
    __tablename__ = 'propiedades'
    id =  mapped_column(Integer, primary_key=True)
    equivalente_id = db.Column(db.Integer, db.ForeignKey("equivalente.id"), nullable=False)
    concepto_id = db.Column(db.Integer, db.ForeignKey("concepto.id"), nullable=False)
    valor = db.Column(db.String(10), nullable = False) 
    equivalente = relationship("Equivalente", back_populates="propiedades", lazy="joined")
    concepto = relationship("Concepto", back_populates="propiedades", lazy="joined")

    def __repr__(self):
        return f'<Propiedad "{self.valor}">'