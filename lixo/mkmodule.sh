#!/bin/bash
#############################

cd ./app
mkdir $1
cd $1

touch __init__.py
touch views.py
touch forms.py
touch constants.py
touch models.py
touch decorators.py

cd ..

cd templates
mkdir $1
touch search.html
touch create.html

