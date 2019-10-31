from django.conf import settings

from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

class CoreListView(ListView):
    pass

class CoreDetailView(DetailView):
    pass