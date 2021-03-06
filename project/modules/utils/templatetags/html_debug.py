import logging
import pprint

from django import template
from django.conf import settings
from django.utils.html import escape, format_html
from django.utils.safestring import mark_safe

register = template.Library()

from modules.utils.console import console

__all__ = [
    'hdbg',
]

logger = logging.getLogger('app')
console = console(source=__name__)

@register.simple_tag(takes_context=True)
def hdbg(context):
    """
    Works only if DEBUG is True!
    """

    if not settings.DEBUG :
        return ''

    out = []
    hdbg_data = context.get('hdbg_data', [])

    if hdbg_data:
        for row in hdbg_data:
            out.append(escape(pprint.pformat(row)))
        return format_html('<div id="core-debug"><pre>{0}</pre></div>', mark_safe('\n'.join(out)))
    return ''