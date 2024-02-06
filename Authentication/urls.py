from django.contrib import admin

from django.urls import path,include
from . import views

from django.urls import path

urlpatterns = [
    path('',views.home,name = "home"),
    path('signup',views.signup,name = "signup"),
     path('activate/<uidb64>/<token>', views.activate, name='activate'),
    path('signin',views.signin,name = "signin"),
    path('signout',views.signout,name = "signout"),
    path('aboutus',views.aboutus,name = "aboutus"),
    path('contactus',views.contactus,name = "contactus"),
    path('join',views.join,name = "join"),
    path('help',views.help,name = "help"),
    path('thankyou',views.thankyou,name = "thankyou")

]