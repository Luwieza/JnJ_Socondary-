"""
WSGI config for Recociliator_J project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.2/howto/deployment/wsgi/
"""

import sys
import os

from django.core.wsgi import get_wsgi_application


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Recociliator_J.settings")

print("[WSGI] WSGI application loaded", file=sys.stderr)
application = get_wsgi_application()
