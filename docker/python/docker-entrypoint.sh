#!/usr/bin/env sh
set -e

CMD=$1

case "$CMD" in
    "runserver" )

        echo "-- Starting $API_TITLE server --"
        exec gunicorn -c $GUNICORN_CONF $PROPERTY_APP
        ;;
    * )
        exec "$@"
        ;;
esac
