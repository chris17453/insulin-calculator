from flask_login import UserMixin
from sqlalchemy import Column, Integer, String, Float

from app.extensions import db


class User(UserMixin, db.Model):
    id = Column(Integer, primary_key=True)
    username = Column(String(150), unique=True, nullable=False)
    password = Column(String(150), nullable=False)