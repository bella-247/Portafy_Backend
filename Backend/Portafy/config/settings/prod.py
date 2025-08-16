from .base import *

import environ
env = environ.Env()
environ.Env.read_env()

DEBUG = False
ALLOWED_HOSTS = ['portafy-backend.onrender.com']

DATABASES = {
    "default": env.db()
}