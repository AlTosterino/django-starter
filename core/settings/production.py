from os import environ
from core.settings.shared import *


# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = environ.get("DJANGO_SECRET_KEY", None)

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = bool(int(environ.get("DJANGO_DEBUG", 0)))

ALLOWED_HOSTS = ["127.0.0.1", "localhost"]

# Database
# https://docs.djangoproject.com/en/dev/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql_psycopg2",
        "NAME": environ.get("DJANGO_DATABASE_NAME", None),
        "USER": environ.get("DJANGO_DATABASE_USER", None),
        "PASSWORD": environ.get("DJANGO_DATABASE_PASSWORD", None),
        "HOST": environ.get("DJANGO_DATABASE_HOST", None),
        "PORT": environ.get("DJANGO_DATABASE_PORT", None),
    }
}
