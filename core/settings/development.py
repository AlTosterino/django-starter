from core.settings.shared import *


# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "VerySecretDevelopmentKey"

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ["127.0.0.1", "localhost"]

# If something needs to be at exact place, use insert instead
INSTALLED_APPS.insert(0, "whitenoise.runserver_nostatic")

# Add apps only for development mode as shown
INSTALLED_APPS += ["debug_toolbar"]

# Add middlewares only for development mode as shown
MIDDLEWARE += ["debug_toolbar.middleware.DebugToolbarMiddleware"]

# Iternal IPS required by django_debug_toolbar
INTERNAL_IPS = ["127.0.0.1"]

# Database
# https://docs.djangoproject.com/en/dev/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}
