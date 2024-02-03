from django.contrib import admin
from django.urls import path, include
from . import views
from .views import dashboard

urlpatterns = [
   
    path('event',views.event,name = "event"),
    path('dashboard/', dashboard, name='dashboard'),
]

