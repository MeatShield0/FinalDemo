from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def home (request):
    return render(request,"base.html")

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

