from datetime import datetime
from app.extensions import db

class Account(db.Model):
    __tablename__ = 'accounts'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    active = db.Column(db.Boolean, default=True, nullable=False)
    created = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)
    last_used = db.Column(db.DateTime, nullable=True)
    activated = db.Column(db.DateTime, nullable=True)

    def __repr__(self):
        return (f"<Account(id={self.id}, owner_id={self.owner_id}, active={self.active}, "
                f"created='{self.created}', last_used='{self.last_used}', activated='{self.activated}')>")
