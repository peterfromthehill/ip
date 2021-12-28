#!/usr/bin/env bash
set -e

echo "ARGS: $*"

if [ "$1" = 'httpd' ]; then
    location update
    exec python3 /httpd.py "$@"
fi

exec "$@"
