#!/bin/sh
set -e

gunicorn --workers 2 --bind $GUNICORN_HOST:$GUNICORN_PORT project.wsgi
# python manage.py runserver $GUNICORN_HOST:$GUNICORN_PORT
