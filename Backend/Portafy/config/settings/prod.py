from .base import *

DEBUG = False
ALLOWED_HOSTS = ["127.0.0.1", 'portafy-backend.onrender.com']

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": "portafy",
        "USER": "root",
        "PASSWORD": "Jt6C8PBXpEzTsTpPS73kV6MiLyE4DcFY",
        "HOST": "dpg-d2ealsbipnbc739oq060-a.oregon-postgres.render.com",
        "PORT": "5432",
    }
}