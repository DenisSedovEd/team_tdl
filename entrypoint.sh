#!/bin/sh

set -e

echo "!!! Apply Django migrations !!!"
python manage.py migrate --noinput
echo "!!! Successfully Django migrations !!!"

echo "!!! Collect static files !!!"
python manage.py collectstatic --noinput
echo "!!! Successfully collected static files !!!"

gunicorn config.wsgi:application --bind 0.0.0.0:8000
echo "!!! Start server !!!"

exec "$@"