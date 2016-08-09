from .base import *

# See: https://docs.djangoproject.com/en/dev/ref/settings/#debug
DEBUG = True

ALLOWED_HOSTS = ['*']

# Database configuration
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# disable the automatic setup for debug_toolbar
DEBUG_TOOLBAR_PATCH_SETTINGS = False

# required by debug_toolbar
MIDDLEWARE += ('utils.middlewares.AtopdedTo110DebugMiddleware',)
INTERNAL_IPS = ['127.0.0.1']

# enable the following apps in the local environment
INSTALLED_APPS += (
    'django_extensions',
    'debug_toolbar',
)

# Output emails to the console.
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
