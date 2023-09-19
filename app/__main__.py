from flask import Flask
from flask_login import LoginManager
from flask_restful import Api

from app.config import Config
from app.extensions import db

app = Flask(__name__)
app.config.from_object(Config)

db.init_app(app)

from app.models.user import User
# Initialize Flask extensions here

# Register blueprints here
from app.main import bp as main_bp
app.register_blueprint(main_bp)
    
from app.auth import bp as auth_bp
app.register_blueprint(auth_bp)

from app.signup import bp as signup_bp
app.register_blueprint(signup_bp)


from app.contact import bp as contact_bp
app.register_blueprint(contact_bp)

from app.dashboard import bp as dash_bp
app.register_blueprint(dash_bp)

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'auth.login'
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

api = Api(app)
from app.api.accountAPI       import AccountAPI
from app.api.activationAPI    import ActivationAPI
from app.api.meal_itemAPI     import MealItemAPI
from app.api.mealAPI          import MealAPI
from app.api.personAPI        import PersonAPI
from app.api.product_imageAPI import ProductImageAPI
from app.api.productAPI       import ProductAPI
from app.api.userAPI          import UserAPI

api.add_resource(AccountAPI     , '/api/activations'   , '/api/accounts/<int:account_id>')
api.add_resource(ActivationAPI  , '/api/activations'   , '/api/activations/<int:id>')
api.add_resource(MealItemAPI    , '/api/meal-items'    , '/api/meal-items/<int:id>')
api.add_resource(MealAPI        , '/api/meals'         , '/api/meals/<int:id>')
api.add_resource(PersonAPI      , '/api/persons'       , '/api/persons/<int:id>')
api.add_resource(ProductImageAPI, '/api/product-images', '/api/product-images/<int:id>')
api.add_resource(ProductAPI     , '/api/products'      , '/api/products/<int:id>')
api.add_resource(UserAPI        , '/api/users'         , '/api/users/<int:id>')




if __name__ == '__main__':
    app.run(debug=True,)