# -*- coding: utf-8 -*-

from flask import Flask, render_template, session
import jinja2
#from flask.ext.sqlalchemy import SQLAlchemy
#from hashlib import md5
#from datetime import datetime

app = Flask(__name__)
app.config.from_object('config')

if app.config['DEBUG']:
    for key in app.config:
        print key, '=', app.config[key]



views_dir =  app.config['VIEWS_DIR']

views_loder = jinja2.ChoiceLoader([app.jinja_loader, jinja2.FileSystemLoader([views_dir])])
app.jinja_loader = views_loder

#db = SQLAlchemy(app)

from app.controllers import home

#from app.index.views import mod as indexModule
#from app.users.views import mod as usersModule
#from app.tos.views import mod as tosModule


###
app.register_blueprint(home.mod)
#app.register_blueprint(usersModule)
#app.register_blueprint(tosModule)
###

def gravatar_url(email, size=80):
	"""Return the gravatar image for the given email address."""
	return 'http://www.gravatar.com/avatar/%s?d=identicon&s=%d' % (md5(email.strip().lower().encode('utf-8')).hexdigest(), size)

def format_datetime(timestamp, tformat= '%Y-%m-%d'):
	"""Format a timestamp for display."""
	return timestamp.strftime(tformat)


app.jinja_env.filters['gravatar'] = gravatar_url
app.jinja_env.filters['datetimeformat'] = format_datetime

###
#@app.errorhandler(404)
#def not_found(error):
#	return render_template('404.html'), 404



#@app.context_processor
#def inject_user():
#	user = userView.get_loged_user()
#	return dict(user = user)
