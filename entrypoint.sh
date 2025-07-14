#!/bin/sh

set -e

echo "!!! Apply Django migrations !!!"
python manage.py migrate --noinput
echo "!!! Successfully Django migrations !!!"

echo "!!! Start server !!!"

exec "$@"