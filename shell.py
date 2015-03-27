#!/usr/bin/env python

import os
import readline
from pprint import pprint

from flask import *
from app import *
from app.users.models import *
from app.tos.models import *

sess = db.session()

def select(model):
	query = sess.query(model)
	results = query.all()
	for result in results:
		pprint(result)
		#print(result)
		
def insert(model):
	db.session.add(model)
	db.session.commit()

os.environ['PYTHONINSPECT'] = 'True'
