import os
import cson
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  # moneytracker/mt
ROOT = os.path.realpath(os.path.abspath(os.path.join(BASE_DIR, '../'))) # moneytracker/

ext_settings_file = os.environ.get('ext_settings_file', 'ext_settings.cson')
CONFIG_FILE = os.path.join(ROOT, ext_settings_file) # moneytracker/ext_settings.cson

try:
    with open(CONFIG_FILE) as f:
        ext = cson.loads(f.read())
except IOError:
    ext = {}

SECRET_KEY = ext.get('secret_key')
DEBUG = ext.get('debug', False)

ALLOWED_HOSTS = []

# May add back at later time: 'django.contrib.gis'
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'whitenoise.runserver_nostatic',
    'rest_framework',
    'spending',
    'budget'
]

MIDDLEWARE_CLASSES = [
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
]

ROOT_URLCONF = 'mt.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'mt.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases
DATABASES = {}
DATABASES['default'] = {}
DATABASES['default']['ENGINE'] = ext.get('engine', 'django.db.backends.sqlite3')
if DATABASES['default']['ENGINE'] == 'django.db.backends.sqlite3':
    DATABASES['default']['NAME'] = os.path.join(BASE_DIR, 'db.sqlite3')
else:
    DATABASES['default']['NAME'] = ext.get('name')
DATABASES['default'].update({
    'USER': ext.get('user', None),
    'PASSWORD': ext.get('password', None),
    'HOST': ext.get('host', None),
    'PORT': ext.get('post', None),
})


# Internationalization
# https://docs.djangoproject.com/en/1.11/topics/i18n/
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True


# https://docs.djangoproject.com/en/1.11/howto/static-files/
# Static files (CSS, JavaScript, Images)
STATIC_ROOT = ext.get('static_root', os.path.join(BASE_DIR, 'staticfiles'))
STATIC_URL = ext.get('static_url', '/static/')
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'


LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
     'handlers': {
         'file': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'filename': ext.get('log_file', os.path.join(ROOT, 'mt.log'))
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

REST_FRAMEWORK = {
    # Use Django's standard `django.contrib.auth` permissions,
    # or allow read-only access for unauthenticated users.
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticated'
    ]
}
