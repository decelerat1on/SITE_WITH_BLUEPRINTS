from flask import Flask, render_template
from profile.profile import profile_blueprint
from catalog.catalog import catalog_blueprint
from mainpage.mainpage import mainpage_blueprint

app = Flask(__name__)

app.register_blueprint(profile_blueprint, url_prefix='/profile')
app.register_blueprint(catalog_blueprint, url_prefix='/catalog')
app.register_blueprint(mainpage_blueprint)

app.run()

