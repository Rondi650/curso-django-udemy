#!/bin/sh

echo "Running Django development server on port 12345..."
python3 manage.py collectstatic --noinput
python3 manage.py migrate
python3 manage.py runserver 0.0.0.0:12345