from django.urls import path

from .views import IndexView

app_name = 'core'

urlpatterns = [
    path('', view=IndexView.as_view(), name='welcome'),
]
