
from flask import Blueprint

bp = Blueprint('signup', __name__)

from app.controlers.signup import routes


