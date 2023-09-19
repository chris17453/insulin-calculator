from app.extensions import db

class Owner(db.Model):
    __tablename__ = 'owners'

    id = db.Column(db.Integer, primary_key=True)
    person_id = db.Column(db.Integer, db.ForeignKey('people.id'), nullable=False)
    additional_field = db.Column(db.String(100))  # Add other relevant fields as necessary

    person = db.relationship('Person', backref=db.backref('owners', lazy=True))

    def __repr__(self):
        return f"<Owner(id={self.id}, person_id='{self.person_id}')>"

