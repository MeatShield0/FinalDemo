# dashboard/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('dashboard1/', views.dashboard1, name='dashboard1'),
    # Add other URL patterns if needed
]
