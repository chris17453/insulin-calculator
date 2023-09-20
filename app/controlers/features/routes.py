from flask import render_template

from app.controlers.features import bp

@bp.route('/features', methods=['GET'])
def privacy():

    return render_template('features.html')
