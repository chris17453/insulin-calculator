from flask_restful import Resource, reqparse

from app.extensions import db
from app.models.user import User

# For Users model
class UserAPI(Resource):
    def get(self, id=None):
        if id:
            user = User.query.get(id)
            if user:
                # It's not good to expose all fields, so we'll avoid sending password_hash
                return jsonify({
                    "id": user.id,
                    "account_id": user.account_id,
                    "person_id": user.person_id,
                    "username": user.username,
                    "email": user.email,
                    "active": user.active,
                    "created": user.created,
                    "last_used": user.last_used
                })
            return {"error": "User not found"}, 404
        users = User.query.all()
        return jsonify([{
            "id": u.id,
            "account_id": u.account_id,
            "person_id": u.person_id,
            "username": u.username,
            "email": u.email,
            "active": u.active,
            "created": u.created,
            "last_used": u.last_used
        } for u in users])
    
    def post(self):
        data = request.get_json()
        new_user = User(**data)
        db.session.add(new_user)
        db.session.commit()
        return {"message": "User created", "id": new_user.id}, 201

    def put(self, id):
        user = User.query.get(id)
        if not user:
            return {"error": "User not found"}, 404
        data = request.get_json()
        for key, value in data.items():
            setattr(user, key, value)
        db.session.commit()
        return {"message": "User updated"}

    def delete(self, id):
        user = User.query.get(id)
        if not user:
            return {"error": "User not found"}, 404
        db.session.delete(user)
        db.session.commit()
        return {"message": "User deleted"}

