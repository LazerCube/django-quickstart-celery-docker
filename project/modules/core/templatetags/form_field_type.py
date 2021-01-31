import logging

from django import template

from ..utils import console

register = template.Library()

__all__ = [
    'field_type',
]

logger = logging.getLogger('app')
console = console(source=__name__)

@register.filter(name='field_type')
def field_type(field):
    return field.field.widget.__class__.__name__