import os

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

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get('SECRET_KEY')

# Debug settings
DEBUG = True

ALLOWED_HOSTS = ['*']

# # Default domain name. Needed for absolute urls in emails
DEFAULT_DOMAIN = 'https://{}'.format(ALLOWED_HOSTS[0])

# Application definition
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django_celery_beat',
    'django_celery_results',
    'modules.core',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

STATICFILES_FINDERS = [
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
]

ROOT_URLCONF = 'config.urls'
STATIC_TEMPLATES = (os.path.join(PROJECT_ROOT, 'templates/'))

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [STATIC_TEMPLATES],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django.template.context_processors.request',
                'modules.core.context_processors.django_environment_variable',
            ],
        },
    },
]

STATIC_URL = '/static/'
MEDIA_URL = '/media/'

STATIC_URL = '/static/'
STATIC_ROOT = (os.path.join(PROJECT_ROOT, 'staticfiles'))
STATICFILES_DIRS = (
    os.path.join(PROJECT_ROOT, 'static'),
) #specifies all the folders on your system where Django should look for static files

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(PROJECT_ROOT, 'mediafiles')

WSGI_APPLICATION = 'config.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': (os.environ.get('DB_NAME', '')),
        'USER': (os.environ.get('DB_USER','')),
        'PASSWORD': (os.environ.get('DB_PASS','')),
        'HOST': (os.environ.get('DB_SERVICE','')),
        'PORT': (os.environ.get('DB_PORT','')),
    }
}

SESSION_COOKIE_AGE = 60 * 60 * 24 * 30 # One month

CELERY_BROKER_URL = 'amqp://rabbitmq:rabbitmq@rabbitmq:5672/vhost1'
CELERY_BEAT_SCHEDULER = 'django_celery_beat.schedulers:DatabaseScheduler'
CELERY_RESULT_BACKEND = 'django-db'
CELERY_ACCEPT_CONTENT = ['json']
CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'
CELERY_TASK_RESULT_EXPIRES = 3600

LANGUAGE_CODE = 'en-gb'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
        'LOCATION': 'unique-snowflake',
    }
}