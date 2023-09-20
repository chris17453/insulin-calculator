from flask import render_template

from app.controlers.terms import bp

@bp.route('/terms', methods=['GET'])
def privacy():

    return render_template('terms.html')
