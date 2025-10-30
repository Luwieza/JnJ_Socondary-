#!/usr/bin/env bash
set -euo pipefail

# Simple start script: run migrations and collectstatic (with retries), then start gunicorn
RETRIES=5
SLEEP=3

echo "Starting container entrypoint: running migrations and collectstatic"
for i in $(seq 1 $RETRIES); do
  if python manage.py migrate --noinput; then
    echo "migrate succeeded"
    break
  else
    echo "migrate attempt $i failed, retrying in $SLEEP seconds..."
    sleep $SLEEP
  fi
  if [ "$i" -eq "$RETRIES" ]; then
    echo "migrate failed after $RETRIES attempts — continuing and letting application handle DB errors"
  fi
done

# Collect static files (safe to run even if DB not ready)
python manage.py collectstatic --noinput || true

# Default PORT fallback
PORT=${PORT:-8080}

echo "Starting gunicorn on 0.0.0.0:$PORT"
exec gunicorn --bind 0.0.0.0:$PORT --workers 1 --timeout 300 --log-level info --access-logfile - --error-logfile - Recociliator_J.wsgi:application
