#!/bin/bash

# Collect static files
echo "Collect static files"
python3 /code/perfectcushion/manage.py collectstatic --noinput

# Apply database migrations
echo "Apply database migrations"
python3 /code/perfectcushion/manage.py migrate

# Start server
echo "Starting server"
python3 /code/perfectcushion/manage.py runserver 0.0.0.0:8000
