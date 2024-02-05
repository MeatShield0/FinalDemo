from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import ClubMember
from .models import UserProfile, Event
# Create your views here.


# def event(request):
#     return render(request,"ClubNexus\event.html")


def dashboard_view(request):
    user_profile = UserProfile.objects.get(user=request.user)
    events = Event.objects.filter(user=request.user, date__gte=datetime.date.today())

    context = {'user_profile': user_profile, 'events': events}
    return render(request, 'event.html', context)

