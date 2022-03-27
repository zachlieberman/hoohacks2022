from django.urls import re_path, include, path
from django.contrib import admin

from . import views

urlpatterns = [
    path('configure', views.configure, name='configure'),
    path('activate/', views.activate, name='activate'),
    path('register/', views.register, name='register')


]