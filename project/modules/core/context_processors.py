import os

from django.conf import settings
from modules import __build__, __version__ 

__all__ = ['django_environment_variable', 'debug']

def django_environment_variable(request):
    return {'DJANGO_ENVIRONMENT_NAME': os.environ.setdefault('DJANGO_ENV', 'development')}

def debug(context):
  return {'DEBUG': settings.DEBUG}

def build(context):
  return {'BUILD': __build__}

def version(context):
  return {'VERSION': __version__}