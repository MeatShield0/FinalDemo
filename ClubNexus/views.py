from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

<<<<<<< HEAD
def home (request):
    return render(request,"base.html")
=======
def home(request):
    return render(request, "ClubNexus/home.html")

def about(request):
    return render(request, "ClubNexus/about.html")

def contact(request):
    return render(request, "ClubNexus/contact.html")

def event(request):
    return render(request, "ClubNexus/event.html")

def services(request):
    return render(request, "ClubNexus/services.html")
>>>>>>> 2dcde839c12a96215a942d797c1f503f855a614a
