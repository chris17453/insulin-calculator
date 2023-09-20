from flask import Flask, url_for
from flask_login import LoginManager
from flask_restful import Api

from app.config import Config
from app.extensions import db

app = Flask(__name__,template_folder="views",static_url_path='/assets',static_folder="assets")
app.config.from_object(Config)

db.init_app(app)

from app.models.user import User
# Initialize Flask extensions here

# Register blueprints here
from app.controlers.main import bp as main_bp
app.register_blueprint(main_bp)
    
from app.controlers.auth import bp as auth_bp
app.register_blueprint(auth_bp)

from app.controlers.signup import bp as signup_bp
app.register_blueprint(signup_bp)


from app.controlers.contact import bp as contact_bp
app.register_blueprint(contact_bp)

from app.controlers.dashboard import bp as dash_bp
app.register_blueprint(dash_bp)

from app.controlers.about import bp as about_bp
app.register_blueprint(about_bp)

from app.controlers.terms import bp as terms_bp
app.register_blueprint(terms_bp)

from app.controlers.privacy import bp as privacy_bp
app.register_blueprint(privacy_bp)

from app.controlers.features import bp as features_bp
app.register_blueprint(features_bp)

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'auth.login'
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

api = Api(app)
from app.controlers.api.accountAPI       import AccountAPI
from app.controlers.api.activationAPI    import ActivationAPI
from app.controlers.api.meal_itemAPI     import MealItemAPI
from app.controlers.api.mealAPI          import MealAPI
from app.controlers.api.personAPI        import PersonAPI
from app.controlers.api.product_imageAPI import ProductImageAPI
from app.controlers.api.productAPI       import ProductAPI
from app.controlers.api.userAPI          import UserAPI

api.add_resource(AccountAPI     , '/api/account'      , '/api/account/<int:account_id>')
api.add_resource(ActivationAPI  , '/api/activation'   , '/api/activation/<int:id>')
api.add_resource(MealItemAPI    , '/api/meal-item'    , '/api/meal-item/<int:id>')
api.add_resource(MealAPI        , '/api/meal'         , '/api/meal/<int:id>')
api.add_resource(PersonAPI      , '/api/person'       , '/api/person/<int:id>')
api.add_resource(ProductImageAPI, '/api/product-image', '/api/product-image/<int:id>')
api.add_resource(ProductAPI     , '/api/product'      , '/api/product/<int:id>')
api.add_resource(UserAPI        , '/api/user'         , '/api/user/<int:id>')



def has_no_empty_params(rule):
    defaults = rule.defaults if rule.defaults is not None else ()
    arguments = rule.arguments if rule.arguments is not None else ()
    return len(defaults) >= len(arguments)


@app.route("/site-map")
def site_map():
    links = []
    for rule in app.url_map.iter_rules():
        # Filter out rules we can't navigate to in a browser
        # and rules that require parameters
        if "GET" in rule.methods and has_no_empty_params(rule):
            url = url_for(rule.endpoint, **(rule.defaults or {}))
            links.append((url, rule.endpoint))
    # links is now a list of url, endpoint tuples
    return links
if __name__ == '__main__':

    app.run(debug=True,)