
from flask import Blueprint

bp = Blueprint('auth', __name__)

from app.controlers.auth import routes


