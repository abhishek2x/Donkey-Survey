
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.contrib.auth.views import LogoutView

from . import views

urlpatterns = [
    path('dashboard/', views.dashboard, name='dashboard'),
    path('<int:pk>/', views.formdetail, name='formdetail'),
    path('create/', views.formcreate, name='formcreate'),
]
