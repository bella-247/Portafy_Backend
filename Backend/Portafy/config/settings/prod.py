from .base import *
import dj_database_url

DEBUG = False
ALLOWED_HOSTS = ['yourdomain.com']

DATABASES = {
    "default": dj_database_url.config()
}