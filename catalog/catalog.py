from flask import Blueprint, render_template

catalog_blueprint = Blueprint('catalog_blueprint', __name__, template_folder='templates')

@catalog_blueprint.route('/')
def catalog():
    return f'Я страница каталога'

@catalog_blueprint.route('/<cat>')
def category_page():
    return f'Я страница категории {cat}'
