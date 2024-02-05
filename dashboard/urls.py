from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard_with_pivot, name='dashboard_with_pivot'),
    path('data', views.pivot_data1, name='pivot_data1'),
    path('data', views.pivot_data2, name='pivot_data2'),
    path('data', views.pivot_data3, name='pivot_data3'),
]