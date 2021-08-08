#!/bin/bash
echo "Starting CTF Challenge"
exec gunicorn 'wsgi:app' \
    --bind '0.0.0.0:8000' \
    --workers 5 \
