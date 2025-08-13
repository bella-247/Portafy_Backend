from .base import *
import dj_database_url

DEBUG = False
ALLOWED_HOSTS = ['portafy-backend.onrender.com']

DATABASES = {
    "default": dj_database_url.config()
}