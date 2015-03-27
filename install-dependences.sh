#!/bin/bash

sudo aptitude install python-pip
sudo pip install sqlalchemy
sudo pip install flask-sqlalchemy
sudo pip install Flask-WTF
sudo pip install gunicorn
sudo pip install flask-restful

pip freeze > dependences_list

