from .base import *
import dj_database_url
from decouple import config

DEBUG = False
ALLOWED_HOSTS = ['portafy-backend.onrender.com']

DATABASES = {
    "default": dj_database_url.config(default=str(config("DATABASE_URL")))
}