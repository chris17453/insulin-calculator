from flask import Flask, render_template, redirect, url_for, request, session, flash
from werkzeug.security import check_password_hash
from flask_login import LoginManager, login_user, login_required, logout_user, current_user

from app.controlers.dashboard import bp
from app.models.user import User


@bp.route('/dashboard')
@login_required
def dashboard():
    data={}
    data['user']=current_user.username
    return render_template('dashboard.html',data=data)

