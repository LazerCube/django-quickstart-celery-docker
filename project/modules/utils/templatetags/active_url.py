import logging
import re

from django import template
from django.urls import reverse, NoReverseMatch

from modules.utils.console import console

__all__ = [
    'active_url',
]

logger = logging.getLogger('app')
console = console(source=__name__)

register = template.Library()

@register.simple_tag(takes_context=True)
def active_url(context, url, get_params=None):
    try:
        pattern = reverse(url)
    except NoReverseMatch:
        pattern = url

    if get_params:
        pattern += "?%s" % get_params
        path = context['request'].get_full_path()
    else:
        path = context['request'].path

    pattern = r"^%s$" % re.escape(pattern)
    
    return 'active' if re.search(pattern, path) else ''