
from flask import Blueprint

bp = Blueprint('terms', __name__)

from app.controlers.terms import routes


