# config/views.py
from django.views.generic import TemplateView
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.shortcuts import render

class Home(TemplateView):
    template_name = 'home.html'

@login_required
def dashboard(request):
    User = get_user_model()
    u = User.objects.get(username=request.user.username)
    print("User Logged In :", u)
    return render(request, "dashboard.html", {})