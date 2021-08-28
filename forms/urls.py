from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.contrib.auth.views import LogoutView

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('dashboard/', views.dashboard, name='dashboard'), # dashboard + form listing
    path('form-detail/<int:pk>/', views.formdetail, name='formdetail'),
    path('forms/<int:pk>', views.formsubmit, name='formsubmit'),
    path('form-results/<int:pk>', views.formresults, name='formresults'),
    path('question-count/', views.formcreate1, name='formcreate1'),
    path('create-form/', views.formcreate2, name='formcreate2'),
    path('delete-form/<int:pk>', views.deleteform, name='deleteform'),
    path('export/<int:pk>', views.export, name='export'),
]