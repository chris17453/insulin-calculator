
from flask import Blueprint

bp = Blueprint('contact', __name__)

from app.controlers.contact import routes


