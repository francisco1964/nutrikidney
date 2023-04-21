from app.extensions import db
from sqlalchemy.orm import mapped_column
from sqlalchemy import Integer
from sqlalchemy.orm import relationship
from app.models.propiedad import Propiedad
# from app.models.grupo import Grupo


class Equivalente(db.Model):
    # id = db.Column(db.Integer, primary_key=True)
    id =  mapped_column(Integer, primary_key=True)
    nombre = db.Column(db.String(100), unique=True)    
    grupo_id = db.Column(db.Integer, db.ForeignKey("grupo.id"), nullable=False)
    propiedades = relationship("Propiedad", back_populates="equivalente")

    def __repr__(self):
        return f'<Equivalente "{self.nombre}">'