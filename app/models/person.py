from app.extensions import db

class Person(db.Model):
    __tablename__ = 'people'

    id = db.Column(db.Integer, primary_key=True)
    account_id = db.Column(db.Integer, db.ForeignKey('accounts.id'), nullable=False)
    display_name = db.Column(db.String(50), nullable=False)
    first_name = db.Column(db.String(50), nullable=True)
    middle_name = db.Column(db.String(50), nullable=True)
    last_name = db.Column(db.String(50), nullable=False)
    birthday = db.Column(db.Date, nullable=True)
    
    def __repr__(self):
        return f"<Person(id={self.id}, display_name='{self.display_name}', first_name='{self.first_name}', last_name='{self.last_name}', birthday='{self.birthday}')>"
    
