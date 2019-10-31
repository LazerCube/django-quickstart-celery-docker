from django.urls import include, path
from modules.core import views

from django.views.generic import TemplateView

app_name = 'core'
urlpatterns = [
    path('', view=TemplateView.as_view(template_name="core/views/welcome.html"), name='welcome'),
]
