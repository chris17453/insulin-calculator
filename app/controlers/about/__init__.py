
from flask import Blueprint

bp = Blueprint('about', __name__)

from app.controlers.about import routes


