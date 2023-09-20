
from flask import Blueprint

bp = Blueprint('privacy', __name__)

from app.controlers.privacy import routes


