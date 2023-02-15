from flask import Blueprint, render_template

profile_blueprint = Blueprint('profile_blueprint', __name__, template_folder='templates')

@profile_blueprint.route('/<uid>')
def profile_page(uid):
    return f'Я страница профиля пользователя {uid}'
