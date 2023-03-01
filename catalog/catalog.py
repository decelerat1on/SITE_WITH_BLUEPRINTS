from flask import Blueprint, render_template

catalog_blueprint = Blueprint('catalog_blueprint', __name__, template_folder='templates', static_folder='static', static_url_path='/catalog/static')
lists_of_items = [{'name':'носки',
                   'count':30,
                   'discription':'Лучшие носки в мире'},
                  {'name': 'штаны',
                   'count': 10,
                   'discription': 'Лучшие штаны в мире'},
                  {'name':'Куртки',
                   'count':20,
                   'discription':'Лучшие куртки в мире'}
                  ]
@catalog_blueprint.route('/')
def catalog():
    return render_template('catalog.html', item_list=lists_of_items, if_aut = False)

@catalog_blueprint.route('/<cat>')
def category_page():
    return f'Я страница категории {cat}'

