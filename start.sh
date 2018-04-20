#!/bin/bash

echo "### Starting Gunicorn ###"
exec gunicorn django_yelp.wsgi:application \
        --bind 0.0.0.0:8000 \
        --workers 3
