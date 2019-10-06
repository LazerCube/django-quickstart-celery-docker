from django.conf.urls import include, url
from modules.core import views

from django.views.generic import TemplateView

app_name = 'core'
urlpatterns = [
    url(r'^$',
        view=TemplateView.as_view(template_name="core/views/welcome.html"),
        name='welcome'),
]
