import os

from .settings import  *

# Set for when HOST IP is permanent
# ALLOWED_HOSTS = ['localhost','127.0.0.1']

DEBUG = True
PRODUCTION = True

SECRET_KEY = os.environ.get('SECRET_KEY')

# Email File backend
# EMAIL_BACKEND = 'django.core.mail.backends.filebased.EmailBackend'
# EMAIL_FILE_PATH = 'D:\\Desktop\\tmp\\app-messages'