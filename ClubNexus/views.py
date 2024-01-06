from django.shortcuts import render

# Create your views here.

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