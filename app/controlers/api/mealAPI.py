from flask_restful import Resource, reqparse

from app.extensions import db
from app.models.meal import Meal

# For Meal model
class MealAPI(Resource):
    def get(self, id=None):
        if id:
            meal = Meal.query.get(id)
            if meal:
                return {
                    "id": meal.id,
                    "person_id": meal.person_id,
                    "date_time": meal.date_time,
                    "name": meal.name
                }
            return {"error": "Meal not found"}, 404

        meals = Meal.query.all()
        return [
            {
                "id": meal.id,
                "person_id": meal.person_id,
                "date_time": meal.date_time,
                "name": meal.name
            } for meal in meals
        ]

    def post(self):
        data = request.get_json()
        new_meal = Meal(**data)
        db.session.add(new_meal)
        db.session.commit()
        return {
            "message": "Meal created",
            "id": new_meal.id
        }, 201

    def put(self, id):
        meal = Meal.query.get(id)
        if not meal:
            return {"error": "Meal not found"}, 404
        data = request.get_json()
        for key, value in data.items():
            setattr(meal, key, value)
        db.session.commit()
        return {"message": "Meal updated"}

    def delete(self, id):
        meal = Meal.query.get(id)
        if not meal:
            return {"error": "Meal not found"}, 404
        db.session.delete(meal)
        db.session.commit()
        return {"message": "Meal deleted"}

