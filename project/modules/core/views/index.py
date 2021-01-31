from django.views.generic.base import TemplateView

from modules.utils.mixins import HtmlDebugMixin
from modules.utils.console import console

__all__ = ['IndexView']

console = console(source=__name__)

class IndexView(HtmlDebugMixin, TemplateView):
    template_name = "core/welcome.html"

    def get_context_data(self, **kwargs):
        self.hdbg("Now I can just output extra information to the screen!!!")
        # self.hdbg(self.request.META)
        kwargs = super().get_context_data(**kwargs)

        # console(self.request.META)
        return kwargs