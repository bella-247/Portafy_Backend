"""
ASGI config for Portafy project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.2/howto/deployment/asgi/
"""

from pathlib import Path

import os
from decouple import config
from django.core.asgi import get_asgi_application

DJANGO_ENV = str(config("DJANGO_ENV", default="config.settings.prod"))

os.environ.setdefault(
    "DJANGO_SETTINGS_MODULE",
    DJANGO_ENV
)
application = get_asgi_application()
