from flask_restful import Resource, reqparse

from app.extensions import db
from app.models.person import Person

# For Person model
class PersonAPI(Resource):
    def get(self, id=None):
        if id:
            person = Person.query.get(id)
            if person:
                return {
                    "id": person.id,
                    "display_name": person.display_name,
                    "first_name": person.first_name,
                    "middle_name": person.middle_name,
                    "last_name": person.last_name,
                    "birthday": person.birthday
                }
            return {"error": "Person not found"}, 404

        persons = Person.query.all()
        return [
            {
                "id": person.id,
                "display_name": person.display_name,
                "first_name": person.first_name,
                "middle_name": person.middle_name,
                "last_name": person.last_name,
                "birthday": person.birthday
            } for person in persons
        ]

    def post(self):
        data = request.get_json()
        new_person = Person(**data)
        db.session.add(new_person)
        db.session.commit()
        return {
            "message": "Person created",
            "id": new_person.id
        }, 201

    def put(self, id):
        person = Person.query.get(id)
        if not person:
            return {"error": "Person not found"}, 404
        data = request.get_json()
        for key, value in data.items():
            setattr(person, key, value)
        db.session.commit()
        return {"message": "Person updated"}

    def delete(self, id):
        person = Person.query.get(id)
        if not person:
            return {"error": "Person not found"}, 404
        db.session.delete(person)
        db.session.commit()
        return {"message": "Person deleted"}

