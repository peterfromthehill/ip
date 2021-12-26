#!/usr/bin/env bash
set -e

if [ "$1" = 'httpd' ]; then
    exec python3 /httpd.py "$@"
fi

exec "$@"
