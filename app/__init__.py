from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_dance.contrib.google import make_google_blueprint
from werkzeug.contrib.fixers import ProxyFix

app = Flask(__name__)
app.secret_key = "supersekrit"
app.config.from_object(Config)
app.wsgi_app = ProxyFix(app.wsgi_app)
db = SQLAlchemy(app)
migrate = Migrate(app, db)

blueprint = make_google_blueprint(
    client_id="423174373080-9l7f3n6pc98uqcs0vr6ggautos2eoitd.apps.googleusercontent.com",
    client_secret="da0p6LhvAinLmQdT8oUrthen",
    scope=[
        "https://www.googleapis.com/auth/plus.me",
        "https://www.googleapis.com/auth/userinfo.email",
    ],

)


app.register_blueprint(blueprint, url_prefix="/login", offline=True)

from app import routes, models





