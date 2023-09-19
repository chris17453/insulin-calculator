from app.extensions import db

from app.extensions import db

class ProductImage(db.Model):
    __tablename__ = 'product_images'

    id = db.Column(db.Integer, primary_key=True)
    product_id = db.Column(db.Integer, db.ForeignKey('products.id'), nullable=False)
    image_path = db.Column(db.String(500), nullable=False)  # URL or filesystem path
    width = db.Column(db.Integer, nullable=True)
    height = db.Column(db.Integer, nullable=True)
    file_type = db.Column(db.String(50), nullable=True)  # e.g., "png", "jpg", "gif"

    def __repr__(self):
        return (f"<ProductImage(id={self.id}, product_id={self.product_id}, "
                f"image_path='{self.image_path}', width={self.width}, "
                f"height={self.height}, file_type='{self.file_type}')>")

    
