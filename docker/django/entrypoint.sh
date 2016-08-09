#!/bin/bash
set -e

# migrate the migrations to the database
python /app/manage.py migrate

# collect the static files to the static directory
python /app/manage.py collectstatic --noinput

# execute any other command passed
exec "$@"
