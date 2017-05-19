"""
WSGI config for project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/howto/deployment/wsgi/
"""

import os

from configurations.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "main.settings")
os.environ.setdefault("DJANGO_CONFIGURATION", "Prod")

if os.environ.get('PTVSD', 'False') == 'True':
    import ptvsd
    ptvsd.enable_attach('dev', address = ('0.0.0.0', 3000))

application = get_wsgi_application()
