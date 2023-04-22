from flask import Blueprint

bp = Blueprint('recetas', __name__)



from app.recetas import routes