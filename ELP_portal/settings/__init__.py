from decouple import config

if config("ENVIRONMENT", default=False) == "development":
    from .development import *
elif config("ENVIRONMENT", default=False) == "staging":
    from .staging import *
else:
    from .production import *
