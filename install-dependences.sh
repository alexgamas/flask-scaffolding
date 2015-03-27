#!/bin/bash

aptitude install python-pip

pip install sqlalchemy
pip install flask-sqlalchemy
pip install Flask-WTF
pip install gunicorn
pip install flask-restful

pip freeze > dependences_list

