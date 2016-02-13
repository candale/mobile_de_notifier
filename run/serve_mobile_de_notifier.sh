#! /bin/bash
NAME="mobile_de_notifier"  
DJANGODIR=/root/workspace/virtualenvs/car_scraping/mobile_de_notifier  
SOCKFILE=/root/workspace/virtualenvs/car_scraping/run/gunicorn.sock  
USER=root                                       
# GROUP=webapps                                
NUM_WORKERS=2                                
DJANGO_SETTINGS_MODULE=mobile_de_notifier.settings 
DJANGO_WSGI_MODULE=mobile_de_notifier.wsgi 

echo "Starting $NAME as `whoami`"

# Activate the virtual environment
cd $DJANGODIR
source ../bin/activate
export DJANGO_SETTINGS_MODULE=$DJANGO_SETTINGS_MODULE
export PYTHONPATH=$DJANGODIR:$PYTHONPATH

# Create the run directory if it doesn't exist
RUNDIR=$(dirname $SOCKFILE)
test -d $RUNDIR || mkdir -p $RUNDIR

# Start your Django Unicorn
# Programs meant to be run under supervisor should not daemonize themselves (do not use --daemon)
exec ../bin/gunicorn ${DJANGO_WSGI_MODULE}:application \
  --name $NAME \
  --workers $NUM_WORKERS \
  --user=$USER \
  --bind=unix:$SOCKFILE \
  --log-level=debug \
  --log-file=-
