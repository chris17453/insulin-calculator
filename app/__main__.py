from flask import Flask, render_template, redirect, url_for, request, session, flash
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, login_user, login_required, logout_user, current_user


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

from app.dashboard import bp as dash_bp
app.register_blueprint(dash_bp)

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'auth.login'
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


if __name__ == '__main__':
    app.run(debug=True)