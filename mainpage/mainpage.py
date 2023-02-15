from flask import Blueprint, render_template

mainpage_blueprint = Blueprint('mainpage_blueprint', __name__, template_folder='templates')

@mainpage_blueprint.route('/')
def mainpage_page():
    return render_template('input.html')