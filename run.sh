#!/bin/bash

echo "installing requirements"
pip install -r requirements.txt
echo "running app"
gunicorn --workers 4 --bind 0.0.0.0:4444 wsgi:app