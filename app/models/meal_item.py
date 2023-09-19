from app.extensions import db

class MealItem(db.Model):
    __tablename__ = 'meal_items'

    id = db.Column(db.Integer, primary_key=True)
    meal_id = db.Column(db.Integer, db.ForeignKey('meals.id'), nullable=False)
    product_id = db.Column(db.Integer, db.ForeignKey('products.id'), nullable=False)
    servings = db.Column(db.Float, nullable=False)

    def __repr__(self):
        return (f"<MealItem(id={self.id}, meal_id={self.meal_id}, "
                f"product_id={self.product_id}, servings={self.servings})>")
