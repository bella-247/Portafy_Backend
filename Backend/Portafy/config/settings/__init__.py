# config/settings/__init__.py
import os

env = os.environ.get("DJANGO_ENV", "dev")
if env.endswith("prod"):
    from .prod import *
else:
    from .dev import *
