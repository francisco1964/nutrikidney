from flask import Blueprint

bp = Blueprint('equivalentes', __name__)

from app.equivalentes import routes