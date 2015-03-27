./clean.sh
pip freeze > ./dependences_list
cat ./dependences_list
gunicorn -c gunicorn.cnf.py ez-booking:app
