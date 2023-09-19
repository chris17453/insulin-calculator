from datetime import datetime
from app.extensions import db

class Activate(db.Model):
    __tablename__ = 'activations'

    id = db.Column(db.Integer, primary_key=True)
    links_uid = db.Column(db.String(128), unique=True, nullable=False)  # This can be a unique token or identifier
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    created = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)

    def __repr__(self):
        return (f"<Activate(id={self.id}, links_uid='{self.links_uid}', "
                f"user_id={self.user_id}, created='{self.created}')>")
