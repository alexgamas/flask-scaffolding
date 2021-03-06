import os

BASE_DIR = os.path.abspath(os.path.dirname(__file__))

VIEWS_DIR = os.path.join(BASE_DIR , 'app', 'views')
STATIC_FILES_DIR = os.path.join(VIEWS_DIR, 'static')

DEBUG = True

#ADMINS = frozenset(['youremail@yourdomain.com'])
#SECRET_KEY = 'SecretKeyForSessionSigning'

#SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(_basedir, 'app.db')
#DATABASE_CONNECT_OPTIONS = {}

#THREADS_PER_PAGE = 8

#CSRF_ENABLED = True
#CSRF_SESSION_KEY = "somethingimpossibletoguess"

#RECAPTCHA_USE_SSL = False
#RECAPTCHA_PUBLIC_KEY = '6LeYIbsSAAAAACRPIllxA7wvXjIE411PfdB2gt2J'
#RECAPTCHA_PRIVATE_KEY = '6LeYIbsSAAAAAJezaIq3Ft_hSTo0YtyeFG-JgRtu'
#RECAPTCHA_OPTIONS = {'theme': 'white'}

APP_VERSION = "0.0.1"
APP_NAME = "My Application"
APP_TITLE = "{} :: {}".format(APP_NAME, APP_VERSION)
