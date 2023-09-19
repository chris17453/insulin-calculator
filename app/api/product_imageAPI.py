from flask_restful import Resource, reqparse

from app.extensions import db
from app.models.product_image import ProductImage

# For ProductImages model
class ProductImageAPI(Resource):
    def get(self, id=None):
        if id:
            product_image = ProductImage.query.get(id)
            if product_image:
                return {
                    "id": product_image.id,
                    "product_id": product_image.product_id,
                    "image_path": product_image.image_path,
                    "width": product_image.width,
                    "height": product_image.height,
                    "file_type": product_image.file_type
                }
            return {"error": "ProductImage not found"}, 404

        product_images = ProductImage.query.all()
        return [
            {
                "id": img.id,
                "product_id": img.product_id,
                "image_path": img.image_path,
                "width": img.width,
                "height": img.height,
                "file_type": img.file_type
            } for img in product_images
        ]

    def post(self):
        data = request.get_json()
        new_product_image = ProductImage(**data)
        db.session.add(new_product_image)
        db.session.commit()
        return {
            "message": "ProductImage created",
            "id": new_product_image.id
        }, 201

    def put(self, id):
        product_image = ProductImage.query.get(id)
        if not product_image:
            return {"error": "ProductImage not found"}, 404
        data = request.get_json()
        for key, value in data.items():
            setattr(product_image, key, value)
        db.session.commit()
        return {"message": "ProductImage updated"}

    def delete(self, id):
        product_image = ProductImage.query.get(id)
        if not product_image:
            return {"error": "ProductImage not found"}, 404
        db.session.delete(product_image)
        db.session.commit()
        return {"message": "ProductImage deleted"}

