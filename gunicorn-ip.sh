#!/bin/sh

NAME="oauth2-server-production"                         	 # Name of the application
# DJANGODIR=/www/webmarks/mywebmarks-backend       	 # Django project directory
DJANGODIR=`pwd`
USER=webdev                                      	 # the user to run as
GROUP=webdev                                     	 # the group to run as
NUM_WORKERS=4                                        # how many worker processes should Gunicorn spawn
NUM_THREAD=4                                         # how many worker processes should Gunicorn spawn
DJANGO_SETTINGS_MODULE=config.settings.production   # which settings file should Django use
DJANGO_WSGI_MODULE=mysite.wsgi                       # WSGI module name

echo "Starting $NAME as `whoami` "

# Activate the virtual environment
cd $DJANGODIR
source ./env/bin/activate
export DJANGO_SETTINGS_MODULE=$DJANGO_SETTINGS_MODULE
export PYTHONPATH=$DJANGODIR:$PYTHONPATH
export DJANGO_DEBUG=False
export BIND=127.0.0.1:8010

echo $PYTHONPATH


# python /app/manage.py collectstatic --noinput
# gunicorn config.wsgi -w $NUM_WORKERS -b 0.0.0.0:5000 --chdir=/app
gunicorn -w $NUM_WORKERS --threads $NUM_THREAD -b $BIND --env DJANGO_SETTINGS_MODULE=$DJANGO_SETTINGS_MODULE $DJANGO_WSGI_MODULE
