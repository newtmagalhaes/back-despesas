#!/bin/sh
set -e

# TODO: use gunicorn
# gunicorn project.wsgi
python manage.py runserver $GUNICORN_HOST:$GUNICORN_PORT
