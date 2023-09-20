from flask import Flask, render_template, redirect, url_for, request, session, flash
from werkzeug.security import check_password_hash
from flask_login import LoginManager, login_user, login_required, logout_user, current_user

from app.controlers.contact import bp

@bp.route('/contact-us', methods=['GET', 'POST'])
def contact():
    return render_template('contact.html')
