from ELP_portal.settings.common import *

DEBUG = True

ALLOWED_HOSTS += [
    "*",
]

CORS_ALLOWED_ORIGINS += [
    "*",
]

# CORS_ALLOWED_ORIGINS_REGEXES += [
#     r"^(http?:\/\/)?((localhost)|(127\.0\.0\.1)):3\d{3}",
#     r"^(http?:\/\/)?((localhost)|(127\.0\.0\.1)):5\d{3}",
#     r"^https:\/\/elp-portal-*",
#     r"(^|^[^:]+:\/\/|[^\.]+\.)elp-portal\.co\.ke",
# ]

# DATABASES = {
#     "default": {
#         "ENGINE": "django.db.backends.sqlite3",
#         "NAME": BASE_DIR + "staging.db",
#     }
# }

DATABASES = {
    "default": dj_database_url.config(default=config("DATABASE_URL_STAGING"))
}
