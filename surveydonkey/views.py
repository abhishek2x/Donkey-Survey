# config/views.py
from django.views.generic import TemplateView


class Home(TemplateView):
    template_name = 'home.html'

class Dashboard(TemplateView):
    template_name = 'dashboard.html'
