import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from flask_bootstrap import Bootstrap
from flask_script import Manager
from raven.contrib.flask import Sentry

app_version = 'v0.0.1'

app = Flask(__name__)
app.config.from_object('config')
manager = Manager(app)
bootstrap = Bootstrap(app)
db = SQLAlchemy(app)
migrate = Migrate(app, db)
lm = LoginManager()
lm.init_app(app)
lm.login_view = 'login'
sentry = Sentry(app)

from app import views, models
