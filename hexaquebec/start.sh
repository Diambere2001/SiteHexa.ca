#!/bin/bash
set -e

export DJANGO_SETTINGS_MODULE=hexaquebec.settings

python manage.py migrate --noinput
python manage.py collectstatic --noinput

gunicorn hexaquebec.wsgi:application --bind 0.0.0.0:$PORT
