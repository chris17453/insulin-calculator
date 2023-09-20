
from flask import Blueprint

bp = Blueprint('features', __name__)

from app.controlers.features import routes


