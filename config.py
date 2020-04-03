WTF_CSRF_ENABLED = True
SECRET_KEY = 'you-will-never-guess'

import os
basedir = os.path.abspath(os.path.dirname(__file__))

SQLALCHEMY_DATABASE_URI = 'postgresql://mastermanager@postgresql:5432/master'

SQLALCHEMY_BINDS = {
    'config': 'postgresql://mastermanager@postgresql:5432/config'
}

SENTRY_DSN = ''

MAIL_SERVER =   'email-smtp.us-east-1.amazonaws.com'
MAIL_PORT =  587
MAIL_USE_SSL =  False
MAIL_USE_TLS =  True
MAIL_USERNAME =  'AKIAJML4QLI7D6GMPFCQ'
MAIL_PASSWORD =  'AtY3XZRkHsNJJJB04vg7f5EiY6ivbQRYMByeBkPjvObU'
MAIL_DEFAULT_SENDER =  '"Do not reply" <donotreply@master.com>'

CSRF_ENABLED     = True
CSRF_SESSION_KEY = SECRET_KEY
