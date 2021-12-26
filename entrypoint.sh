#!/usr/bin/env bash
set -e

if [ "$1" = 'httpd' ]; then
    location update
    exec python3 /httpd.py "$@"
fi

exec "$@"
