"""
ASGI config for Portafy project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.2/howto/deployment/asgi/
"""

from pathlib import Path

import os
from dotenv import load_dotenv

from django.core.asgi import get_asgi_application

BASE_DIR = BASE_DIR = Path(__file__).resolve().parent.parent
load_dotenv(os.path.join(BASE_DIR, ".env"))
# Set the default settings module for the 'asgi' command.
# This allows the application to use the correct settings based on the environment.
os.environ.setdefault(
    "DJANGO_SETTINGS_MODULE",
    os.getenv("DJANGO_ENV", "config.settings.prod")
)
application = get_asgi_application()
