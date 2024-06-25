#!/bin/sh
set -e

python manage.py collectstatic --no-input
python manage.py migrate

gunicorn --workers $GUNICORN_WORKERS --bind $GUNICORN_HOST:$GUNICORN_PORT project.wsgi
# python manage.py runserver $GUNICORN_HOST:$GUNICORN_PORT
