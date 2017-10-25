#!/bin/bash

NAME="mt"
PROJECTDIR=/home/mt/moneytracker
DJANGODIR=/home/mt/moneytracker/mt
SOCKFILE=/home/mt/moneytracker/gunicorn.sock
USER=mt
GROUP=mt  # Change this?
NUM_WORKERS=1
DJANGO_SETTINGS_MODULE=mt.settings
DJANGO_WSGI_MODULE=mt.wsgi


echo "Starting $NAME as $(whoami)"

cd "$PROJECTDIR"
source "$PROJECTDIR/venv/bin/activate"
export DJANGO_SETTINGS_MODULE=$DJANGO_SETTINGS_MODULE
export PYTHONPATH=$DJANGODIR:$PYTHONPATH  # Should this be PROJECTDIR?
export ext_settings_file="ext_settings_prod.cson"

RUNDIR="$PROJECTDIR"
exec "$PROJECTDIR/venv/bin/gunicorn" ${DJANGO_WSGI_MODULE}:application \
  --name $NAME \
  --workers $NUM_WORKERS \
  --user $USER \
  --bind=unix:$SOCKFILE




