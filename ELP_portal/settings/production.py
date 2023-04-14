from .common import *

CORS_ALLOWED_ORIGINS = [
    "http://localhost:3000",
    "http://localhost",
    "http://127.0.0.1:3000",
    "http://127.0.0.1",
    'http://testelpportal.s3-website-us-east-1.amazonaws.com',
    'https://testelpportal.s3-website-us-east-1.amazonaws.com',
    'http://elpportal.s3-website-us-east-1.amazonaws.com',
    'https://elpportal.s3-website-us-east-1.amazonaws.com'
    
]

CORS_ORIGIN_WHITELIST = [
    "http://localhost:3000",
    "http://localhost",
    "http://127.0.0.1:3000",
    "http://127.0.0.1",
    'http://testelpportal.s3-website-us-east-1.amazonaws.com',
    'https://testelpportal.s3-website-us-east-1.amazonaws.com',
    'http://elpportal.s3-website-us-east-1.amazonaws.com',
    'https://elpportal.s3-website-us-east-1.amazonaws.com'
]
# SECURITY WARNING: don't run with debug turned on in production!
# Setting debug to true for troubleshooting.
DEBUG = True
ALLOWED_HOSTS = ["*"]
SECRET_KEY = os.environ['SECRET_KEY']
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': os.environ['RDS_DB_NAME'],
        'USER': os.environ['RDS_USERNAME'],
        'PASSWORD': os.environ['RDS_PASSWORD'],
        'HOST': os.environ['RDS_HOSTNAME'],
        'PORT': os.environ['RDS_PORT'],
    }
}
