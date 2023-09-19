from app.__main__ import app

from app.extensions import db
from app.config import Config

from eralchemy2 import render_er

from app.models.account import Account
from app.models.activate import Activate
from app.models.meal   import Meal
from app.models.meal_item import MealItem
from app.models.owner import Owner
from app.models.person import Person
from app.models.product_image import ProductImage
from app.models.product import Product
from app.models.user import User
 
with app.app_context():
    db.create_all()


## Draw from SQLAlchemy base
#render_erdb, 'erd_from_sqlalchemy.png')

## Draw from database
render_er(Config.SQLALCHEMY_DATABASE_URI, 'docs/erd_from_sqlite.pdf')