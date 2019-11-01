import logging.config
import os
import sys

from .base import *

DEBUG = False
HTTPS = False

# Set for when HOST IP is permanent
# ALLOWED_HOSTS = ['0.0.0.0', 'localhost']

AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

# Production only apps
# INSTALLED_APPS += [
#     'production.contrib.django.production_app',
# ]

# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error when DEBUG=False.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.

LOGGING_CONFIG = None
DJANGO_LOG_LEVEL = os.environ.get('DJANGO_LOG_LEVEL', 'INFO')

logging.config.dictConfig(
    {
        'version': 1,
        'disable_existing_loggers': False,
        'formatters': {'default': {'format': '%(asctime)s %(name)-12s %(levelname)-8s %(message)s'}},
        'handlers': {
            'mail_admins': {'level': 'ERROR', 'class': 'django.utils.log.AdminEmailHandler'},
            'stdout': {
                'level': 'INFO',
                'class': 'logging.StreamHandler',
                'formatter': 'default',
                'stream': sys.stdout,
            },
            'stderr': {
                'level': 'ERROR',
                'class': 'logging.StreamHandler',
                'formatter': 'default',
                'stream': sys.stderr,
            },
        },
        'loggers': {
            '': {'level': 'DEBUG', 'handlers': ['stdout']},
            'app': {'level': DJANGO_LOG_LEVEL, 'handlers': ['stdout'], 'propagate': False},
            'django.request': {'handlers': ['mail_admins'], 'level': 'ERROR', 'propagate': False},
        },
    }
)


if HTTPS:
    CSRF_COOKIE_HTTPONLY = True
    CSRF_COOKIE_SECURE = True

    SECURE_BROWSER_XSS_FILTER = True
    SECURE_CONTENT_TYPE_NOSNIFF = True
    SECURE_SSL_HOST = True
    SECURE_SSL_REDIRECT = True
    SECURE_HSTS_SECONDS = 31536000
    SECURE_HSTS_INCLUDE_SUBDOMAINS = True
    SECURE_HSTS_PRELOAD = True

    SESSION_COOKIE_DOMAIN = None
    SESSION_COOKIE_SECURE = True
    SESSION_COOKIE_HTTPONLY = True
    
SESSION_COOKIE_AGE = 60 * 60 * 24 * 30 # One month

# SESSION_EXPIRE_AT_BROWSER_CLOSE = True
# SESSION_COOKIE_NAME = ''

X_FRAME_OPTIONS = 'DENY'

# ADMINS will be notified of 500 errors by email.
# MANAGERS will be notified of 404 errors.
# IGNORABLE_404_URLS can help filter out spurious reports.

# ADMINS = (('Your Name', 'your@email.com'),)
# MANAGERS = ADMINS

# Email File backend
# EMAIL_BACKEND = 'django.core.mail.backends.filebased.EmailBackend'
# EMAIL_FILE_PATH = 'D:\\Desktop\\tmp\\app-messages'