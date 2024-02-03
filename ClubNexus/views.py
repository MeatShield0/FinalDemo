from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import ClubMember
# Create your views here.


def event(request):
    return render(request,"ClubNexus\event.html")

def dashboard(request):
    user = request.user  # Assuming you have user authentication
    member_info = ClubMember.objects.get(email=user.email)
    return render(request, 'dashboard.html', {'member_info': member_info})
