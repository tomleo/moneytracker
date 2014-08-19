"""
Django settings for mt project.

For more information on this file, see
https://docs.djangoproject.com/en/dev/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/dev/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
import json
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
ROOT = os.path.realpath(os.path.abspath(os.path.join(BASE_DIR, '../')))
DB_CONFIG_FILE = os.path.realpath(os.path.abspath(os.path.join(ROOT, './db_settings.json')))
try:
    with open(DB_CONFIG_FILE) as f:
        db_settings = json.loads(f.read())
except IOError:
    db_settings = {}


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/dev/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '*%@-(od3#%iei^cbnlpbo%0)j74etf&wi9l3noqfcnh14r&e%r'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'widget_tweaks',

    'spending',
    'userprofile',
    'places'
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'mt.urls'

WSGI_APPLICATION = 'mt.wsgi.application'


# Database
# https://docs.djangoproject.com/en/dev/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': db_settings.get('engine'),
        'NAME': db_settings.get('name'),
        'USER': db_settings.get('user'),
        'PASSWORD': db_settings.get('password'),
        'HOST': db_settings.get('host'),
        'PORT': db_settings.get('post'),
    }
}

# Internationalization
# https://docs.djangoproject.com/en/dev/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/dev/howto/static-files/

STATIC_ROOT = '/data/moneytraker/static/'
STATIC_URL = '/data/moneytraker/static/'

#AUTH_PROFILE_MODULE = "userprofile.UserProfile"



LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
     'handlers': {
         'file': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'filename': '/var/log/moneytraker/django_debug.log',
        },
    },
    'loggers': {
        'django.request': {
            'handlers': ['file'],
            'level': 'DEBUG',
            'propagate': True,
        },
    }
}

