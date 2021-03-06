import logging

from django.shortcuts import redirect
from django.urls import reverse

from modules.core.utils import console

__all__ = ['anonymous_required']

logger = logging.getLogger('app')
console = console(source=__name__)

def anonymous_required( view_function, redirect_to = None ):
    return AnonymousRequired( view_function, redirect_to )

class AnonymousRequired(object):
    def __init__(self, view_function, redirect_to):
        if redirect_to is None:
            from django.conf import settings
            redirect_to = getattr(settings, 'AUTHORIZED_REDIRECT_URL', 'dsynomia:home')
        self.view_function = view_function
        self.redirect_to = redirect_to

    def __call__(self, request, *args, **kwargs):
        if request.user is not None and request.user.is_authenticated:
            return redirect(self.redirect_to)
        return self.view_function(request, *args, **kwargs)