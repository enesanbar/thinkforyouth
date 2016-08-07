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

# enable the following apps in the local environment
INSTALLED_APPS += (
    'django_extensions',
)

# Output emails to the console.
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
