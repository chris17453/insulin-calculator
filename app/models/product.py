from app.extensions import db


class Product(db.Model):
    __tablename__ = 'products'

    id = db.Column(db.Integer, primary_key=True)
    account_id = db.Column(db.Integer, db.ForeignKey('accounts.id'), nullable=False)
    name = db.Column(db.String(100), nullable=False)
    desc = db.Column(db.String(500), nullable=True)  # Description
    vendor = db.Column(db.String(100), nullable=True)
    metric_type = db.Column(db.String(50), nullable=True)  # e.g., "gram", "liter", "piece"
    servings = db.Column(db.Integer, nullable=True)
    serving_size = db.Column(db.String(50), nullable=True)  # e.g., "100g", "250ml"
    calories = db.Column(db.Integer, nullable=True)

    def __repr__(self):
        return (f"<Product(id={self.id}, name='{self.name}', account_id={self.account_id}, "
                f"desc='{self.desc}', vendor='{self.vendor}', metric_type='{self.metric_type}', "
                f"servings={self.servings}, serving_size='{self.serving_size}', calories={self.calories})>")


