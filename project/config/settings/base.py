"""
Base settings to build other settings files upon.
"""
import os
import subprocess
import modules

# README:
# Use os.environ.get('ENV_VAR','')
# Not os.environ['ENV_VAR']
# Due to weird error with on celery_beat giving
# AttributeError: 'Settings' object has no attribute at runtimeself.
# See: https://github.com/celery/celery/issues/5463
# And: https://stackoverflow.com/questions/40915735/start-celery-worker-throws-no-attribute-worker-state-db

# Build paths inside the project like this: os.path.join(PROJECT_ROOT, ...)
CURRENT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PROJECT_ROOT = os.path.sep.join(CURRENT_DIR.split(os.path.sep)[:-1])

try:
    modules.__build__ = subprocess.check_output(["git", "describe", "--tags", "--always"], cwd=PROJECT_ROOT).decode('utf-8').strip()
except:
    modules.__build__ = modules.__version__ + " ?"

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get('SECRET_KEY')

# GENERAL
# ------------------------------------------------------------------------------
DEBUG = True
ALLOWED_HOSTS = ['*']

# DATABASE
# ------------------------------------------------------------------------------
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': (os.environ.get('DB_NAME', '')),
        'USER': (os.environ.get('DB_USER','')),
        'PASSWORD': (os.environ.get('DB_PASS','')),
        'HOST': (os.environ.get('DB_Host','')),
        'PORT': (os.environ.get('DB_PORT','')),
    }
}

# URLS
# ------------------------------------------------------------------------------
ROOT_URLCONF = 'config.urls'
WSGI_APPLICATION = "config.wsgi.application"
DEFAULT_DOMAIN = 'https://{}'.format(ALLOWED_HOSTS[0]) # Default domain name. Needed for absolute urls in emails

# APPS
# ------------------------------------------------------------------------------
DJANGO_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

THIRD_PARTY_APPS = [
    'django_celery_beat',
    'django_celery_results',
]

LOCAL_APPS = [
    'modules.core',
    'modules.utils',
]

INSTALLED_APPS = DJANGO_APPS + THIRD_PARTY_APPS + LOCAL_APPS

# AUTHENTICATION
# ------------------------------------------------------------------------------
AUTHENTICATION_BACKENDS = [
    "django.contrib.auth.backends.ModelBackend",
]
# AUTH_USER_MODEL = ""
# LOGIN_REDIRECT_URL = ""
# AUTHORIZED_REDIRECT_URL = ""
# LOGIN_URL = ""

# MIDDLEWARE
# ------------------------------------------------------------------------------
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# STATIC
# ------------------------------------------------------------------------------
STATIC_ROOT = (os.path.join(PROJECT_ROOT, 'staticfiles'))
STATIC_URL = '/static/'
STATICFILES_DIRS = (
    os.path.join(PROJECT_ROOT, 'static'),
) # specifies all the folders on your system where Django should look for static files

STATICFILES_FINDERS = [
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
]

# MEDIA
# ------------------------------------------------------------------------------
MEDIA_ROOT = os.path.join(PROJECT_ROOT, 'mediafiles')
MEDIA_URL = '/media/'

# TEMPLATES
# ------------------------------------------------------------------------------
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(PROJECT_ROOT, 'templates/')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django.template.context_processors.request',
                'modules.utils.context_processors.django_environment_variable',
                'modules.utils.context_processors.debug',
                'modules.utils.context_processors.build',
                'modules.utils.context_processors.version',
            ],
        },
    },
]

WSGI_APPLICATION = 'config.wsgi.application'

# SECURITY
# ------------------------------------------------------------------------------
SESSION_COOKIE_HTTPONLY = True
CSRF_COOKIE_HTTPONLY = True
SECURE_BROWSER_XSS_FILTER = True
X_FRAME_OPTIONS = "DENY"
SESSION_COOKIE_AGE = 60 * 60 * 24 * 30 # One month

# ADMIN
# ------------------------------------------------------------------------------
# Django Admin URL.
ADMIN_URL = "admin/"

# Celery
# ------------------------------------------------------------------------------
CELERY_BROKER_URL = 'amqp://rabbitmq:rabbitmq@rabbitmq:5672/vhost1'
CELERY_BEAT_SCHEDULER = 'django_celery_beat.schedulers:DatabaseScheduler'
CELERY_RESULT_BACKEND = 'django-db'
CELERY_TASK_RESULT_EXPIRES = 3600
CELERY_ACCEPT_CONTENT = ['application/json']
CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'

LANGUAGE_CODE = 'en-gb'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True

# CACHES
# ------------------------------------------------------------------------------
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
        'LOCATION': 'unique-snowflake',
    }
}