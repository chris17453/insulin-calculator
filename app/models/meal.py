from datetime import datetime
from app.extensions import db

class Meal(db.Model):
    __tablename__ = 'meals'

    id = db.Column(db.Integer, primary_key=True)
    person_id = db.Column(db.Integer, db.ForeignKey('people.id'), nullable=False)
    date_time = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)
    name = db.Column(db.String(255), nullable=False)

    def __repr__(self):
        return (f"<Meal(id={self.id}, person_id={self.person_id}, "
                f"date_time='{self.date_time}', name='{self.name}')>")
