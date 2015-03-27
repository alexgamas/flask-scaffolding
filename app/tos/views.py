from flask import Blueprint, request, render_template, flash, g, session, redirect, url_for

from app.tos.models import TOS
import datetime
#from app import db

mod = Blueprint('terms', __name__, url_prefix='/tos')

tos = None

@mod.route('/')
def index():
    return redirect(url_for('tos.read'))

@mod.route('/read/')
def read():
	return render_template("tos/terms.html", term = g.tos)


@mod.before_request
def before_request():
	today = datetime.date.today().strftime('%Y-%m-%d')
	_filter = ("date <= '%s 23:59:59'" % today)
	g.tos = TOS.query.filter(_filter).first()
	print g.tos
