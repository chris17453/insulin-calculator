from flask_restful import Resource, reqparse

from app.extensions import db
from app.models.product import Product

# For Product model
class ProductAPI(Resource):
    def get(self, id=None):
        if id:
            product = Product.query.get(id)
            if product:
                return {
                    "id": product.id,
                    "account_id": product.account_id,
                    "name": product.name,
                    "desc": product.desc,
                    "vendor": product.vendor,
                    "metric_type": product.metric_type,
                    "servings": product.servings,
                    "serving_size": product.serving_size,
                    "calories": product.calories
                }
            return {"error": "Product not found"}, 404

        products = Product.query.all()
        return [
            {
                "id": product.id,
                "account_id": product.account_id,
                "name": product.name,
                "desc": product.desc,
                "vendor": product.vendor,
                "metric_type": product.metric_type,
                "servings": product.servings,
                "serving_size": product.serving_size,
                "calories": product.calories
            } for product in products
        ]

    def post(self):
        data = request.get_json()
        new_product = Product(**data)
        db.session.add(new_product)
        db.session.commit()
        return {
            "message": "Product created",
            "id": new_product.id
        }, 201

    def put(self, id):
        product = Product.query.get(id)
        if not product:
            return {"error": "Product not found"}, 404
        data = request.get_json()
        for key, value in data.items():
            setattr(product, key, value)
        db.session.commit()
        return {"message": "Product updated"}

    def delete(self, id):
        product = Product.query.get(id)
        if not product:
            return {"error": "Product not found"}, 404
        db.session.delete(product)
        db.session.commit()
        return {"message": "Product deleted"}

