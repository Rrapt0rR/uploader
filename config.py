WTF_CSRF_ENABLED = True
SECRET_KEY = 'you-will-never-guess'

import os
basedir = os.path.abspath(os.path.dirname(__file__))

SQLALCHEMY_DATABASE_URI = 'postgresql://mastermanager@postgresql:5432/master'

SQLALCHEMY_BINDS = {
    'config': 'postgresql://mastermanager@postgresql:5432/config'
}

SENTRY_DSN = ''

CSRF_ENABLED     = True
CSRF_SESSION_KEY = SECRET_KEY
