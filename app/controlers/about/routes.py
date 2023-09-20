from flask import render_template

from app.controlers.about import bp

@bp.route('/about', methods=['GET'])
def privacy():

    return render_template('about.html')
