from flask_restful import Resource, reqparse

from app.extensions import db
from app.models.meal_item import MealItem

# For MealItem model
class MealItemAPI(Resource):
    def get(self, id=None):
        if id:
            meal_item = MealItem.query.get(id)
            if meal_item:
                return {
                    "id": meal_item.id,
                    "meal_id": meal_item.meal_id,
                    "product_id": meal_item.product_id,
                    "servings": meal_item.servings
                }
            return {"error": "MealItem not found"}, 404

        meal_items = MealItem.query.all()
        return [
            {
                "id": item.id,
                "meal_id": item.meal_id,
                "product_id": item.product_id,
                "servings": item.servings
            } for item in meal_items
        ]

    def post(self):
        data = request.get_json()
        new_meal_item = MealItem(**data)
        db.session.add(new_meal_item)
        db.session.commit()
        return {
            "message": "MealItem created",
            "id": new_meal_item.id
        }, 201

    def put(self, id):
        meal_item = MealItem.query.get(id)
        if not meal_item:
            return {"error": "MealItem not found"}, 404
        data = request.get_json()
        for key, value in data.items():
            setattr(meal_item, key, value)
        db.session.commit()
        return {"message": "MealItem updated"}

    def delete(self, id):
        meal_item = MealItem.query.get(id)
        if not meal_item:
            return {"error": "MealItem not found"}, 404
        db.session.delete(meal_item)
        db.session.commit()
        return {"message": "MealItem deleted"}

