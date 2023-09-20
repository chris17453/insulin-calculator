from flask_restful import Resource, reqparse

from app.extensions import db
from app.models.activate import Activate

# For Activations model
class ActivationAPI(Resource):
    def get(self, id=None):
        if id:
            activation = Activate.query.get(id)
            if activation:
                return {
                    "id": activation.id,
                    "links_uid": activation.links_uid,
                    "user_id": activation.user_id,
                    "created": activation.created
                }
            return {"error": "Activation not found"}, 404

        activations = Activate.query.all()
        return [
            {
                "id": act.id,
                "links_uid": act.links_uid,
                "user_id": act.user_id,
                "created": act.created
            } for act in activations
        ]
    
    def post(self):
        data = request.get_json()
        new_activation = Activate(**data)
        db.session.add(new_activation)
        db.session.commit()
        return {
            "message": "Activation created",
            "id": new_activation.id
        }, 201

    def put(self, id):
        activation = Activate.query.get(id)
        if not activation:
            return {"error": "Activation not found"}, 404
        data = request.get_json()
        for key, value in data.items():
            setattr(activation, key, value)
        db.session.commit()
        return {"message": "Activation updated"}

    def delete(self, id):
        activation = Activate.query.get(id)
        if not activation:
            return {"error": "Activation not found"}, 404
        db.session.delete(activation)
        db.session.commit()
        return {"message": "Activation deleted"}

