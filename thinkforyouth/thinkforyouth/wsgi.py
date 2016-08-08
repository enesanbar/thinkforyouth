"""
WSGI config for thinkforyouth project.

It exposes the WSGI callable as a module-level variable named ``application``.
"""

import os

import dotenv
from django.core.wsgi import get_wsgi_application

dotenv.read_dotenv(os.path.join(os.path.dirname(os.path.dirname(__file__)), '.env'))

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "thinkforyouth.settings.local")

application = get_wsgi_application()
