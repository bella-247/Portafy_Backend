# config/settings/__init__.py
import environ
env = environ.Env()
environ.Env.read_env()

if str(env("DJANGO_ENV")).endswith("prod"):
    from .prod import *
else:
    from .dev import *
