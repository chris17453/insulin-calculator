from flask import render_template

from app.controlers.privacy import bp

@bp.route('/privacy', methods=['GET'])
def privacy():

    return render_template('privacy.html')
