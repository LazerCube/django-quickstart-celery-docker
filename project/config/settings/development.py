import logging
import os
import re

from django.core.management.color import color_style

from .base import *

ansi_escape = re.compile(r'\x1b[^m]*m')

LOGGING_SKIP_THESE_EXTENSIONS = ['css', 'js', 'png', 'jpg', 'svg', 'gif', 'woff']

def create_log_message_chunk(record):
    message = ansi_escape.sub('', record.msg)
    message_chunk = message.split()
    if message_chunk:
        if message_chunk[0] == '127.0.0.1':
            http_method = message_chunk[5].replace('"', '')
            request_path = message_chunk[6]
            __, request_extension = os.path.splitext(request_path)
            request_extension = request_extension.replace('.', '')
            http_status = message_chunk[8]
            return dict(
                http_method=http_method,
                request_path=request_path,
                http_status=http_status,
                extension=request_extension,
            )
    return []

def development_log_callback(record):
    message_chunk = create_log_message_chunk(record)
    if message_chunk:
        if message_chunk.get('extension') in LOGGING_SKIP_THESE_EXTENSIONS:
            return False
    return True


class DevelopmentLogFormatter(logging.Formatter):
    def format(self, record):  # noqa: A003
        message_chunk = create_log_message_chunk(record)
        if message_chunk:
            http_method = message_chunk.get('http_method')
            request_path = message_chunk.get('request_path')
            http_status = message_chunk.get('http_status')
            record.msg = f'{http_method} | {http_status} | {request_path}'
        return super().format(record)


class SQLQueryLogFormatter(logging.Formatter):
    def __init__(self, *args, **kwargs):
        self.style = color_style()
        super().__init__(*args, **kwargs)

    def format(self, record):  # noqa: A003
        record.levelname = '{0:.<14}'.format('SQL')
        record.levelname = self.style.HTTP_INFO(record.levelname)
        record.sql = self.style.SQL_KEYWORD(record.sql)
        return super().format(record)

LOGGING = {
    'version': 1,
    'disable_existing_loggers': True,
    'filters': {'development': {'()': 'django.utils.log.CallbackFilter', 'callback': development_log_callback}},
    'formatters': {
        'development': {'()': DevelopmentLogFormatter, 'format': '%(levelname)s | %(message)s'},
        'sql': {'()': SQLQueryLogFormatter, 'format': '%(sql)s\n\ntook: %(duration)f mseconds\n\n'},
    },
    'handlers': {
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'development',
            'filters': ['development'],
        },
        'console_sql': {'level': 'DEBUG', 'class': 'logging.StreamHandler', 'formatter': 'sql'},
    },
    'loggers': {
        'app': {'handlers': ['console'], 'level': 'DEBUG'},
        'django.server': {'handlers': ['console'], 'level': 'DEBUG', 'propagate': True},
        # 'django.db.backends': {'handlers': ['console_sql'], 'level': 'DEBUG'},
    },
}

DEBUG = True
ALLOWED_HOSTS = ['*']
INTERNAL_IPS = ['127.0.0.1']

# middlewares for development purposes only
MIDDLEWARE.insert(0, 'debug_toolbar.middleware.DebugToolbarMiddleware')

# apps for development purposes only
INSTALLED_APPS += ['debug_toolbar']

# Developing with a Django server in a Docker container with docker, the standard instructions for enabling the toolbar don't work.
# The reason is related to the fact that the actual address that you would need to add to INTERNAL_IPS is going to be something
# dynamic, like 172.24.0.1. Rather than trying to dynamically set the value of INTERNAL_IPS, the straightforward solution
# is to just replace the function that enables the toolbar.

DEBUG_TOOLBAR_CONFIG = {
    'SHOW_TOOLBAR_CALLBACK': lambda _request: DEBUG
}