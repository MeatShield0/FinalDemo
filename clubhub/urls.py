from django.contrib import admin
from django.urls import path,include
from django.urls import path

urlpatterns = [

    path('admin/', admin.site.urls),
    path('', include('Authentication.urls')),
    path('', include('dashboard1.urls')),
]
