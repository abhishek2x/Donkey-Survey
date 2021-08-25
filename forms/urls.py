
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.contrib.auth.views import LogoutView

from .views import *

urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('dashboard/', dashboard, name='dashboard'), # dashboard + form listing
    path('form-detail/<int:pk>/', formdetail, name='formdetail'),
    path('forms/<int:pk>', formsubmit, name='formsubmit'),
    path('form-results/<int:pk>', formresults, name='formresults'),
    # path('create/', formcreate, name='formcreate'),
]