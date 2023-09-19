from flask import Flask, render_template, redirect, url_for, request, session, flash
from werkzeug.security import check_password_hash
from flask_login import LoginManager, login_user, login_required, logout_user, current_user

from app.signup import bp
from app.models.user import User

@bp.route('/sign-up', methods=['GET', 'POST'])
def signup():
    #if request.method == 'POST':

    return render_template('signup.html')

