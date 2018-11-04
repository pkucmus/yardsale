#!/bin/bash

set -e

echo "Collect static files"
python src/service/manage.py collectstatic --noinput

echo "Apply database migrations"
python src/service/manage.py migrate

exec "$@"
