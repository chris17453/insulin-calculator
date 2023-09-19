from flask_restful import Resource, reqparse

from app.extensions import db
from app.models.account import Account


class AccountAPI(Resource):
    def get(self, account_id):
        account = Account.query.get(account_id)
        if not account:
            return {"error": "Account not found"}, 404
        return {
            "id": account.id,
            "user_id": account.user_id,
            "active": account.active,
            "created": account.created,
            "last_used": account.last_used,
            "activated": account.activated
        }

    def post(self):
        args = parser.parse_args()
        account = Account(user_id=args['user_id'], active=args.get('active', True))
        db.session.add(account)
        db.session.commit()
        return {"message": "Account created", "account_id": account.id}, 201

    def put(self, account_id):
        account = Account.query.get(account_id)
        if not account:
            return {"error": "Account not found"}, 404
        args = parser.parse_args()
        if 'user_id' in args:
            account.user_id = args['user_id']
        if 'active' in args:
            account.active = args['active']
        db.session.commit()
        return {"message": "Account updated"}

    def delete(self, account_id):
        account = Account.query.get(account_id)
        if not account:
            return {"error": "Account not found"}, 404
        db.session.delete(account)
        db.session.commit()
        return {"message": "Account deleted"}

