#from flask_login import UserMixin
#from sqlalchemy import Column, Integer, String, Float

from app.extensions import db


#class User(UserMixin, db.Model):
 #   id = Column(Integer, primary_key=True)
 #   username = Column(String(150), unique=True, nullable=False)
 #   password = Column(String(150), nullable=False)

from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime

class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    account_id = db.Column(db.Integer, db.ForeignKey('accounts.id'), nullable=False)
    person_id = db.Column(db.Integer, db.ForeignKey('people.id'), nullable=False)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    active = db.Column(db.Boolean, default=True, nullable=False)
    created = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)
    last_used = db.Column(db.DateTime, nullable=True)

    account = db.relationship('Account', backref=db.backref('users', lazy=True))
    person = db.relationship('People', backref=db.backref('people', lazy=True))

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return (f"<User(id={self.id}, username='{self.username}', email='{self.email}', "
                f"active={self.active}, created='{self.created}', last_used='{self.last_used}')>")
