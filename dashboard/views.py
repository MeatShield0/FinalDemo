from django.http import JsonResponse
from django.shortcuts import render
from dashboard.models import Club, Member, Event
from django.core import serializers

# Create your views here.

def dashboard_with_pivot(request):
    return render(request, 'dashboard_with_pivot.html', {})


def pivot_data1(request):
    dataset = Club.objects.all()
    data = serializers.serialize('json', dataset)
    return JsonResponse(data, safe=False)


def pivot_data2(request):
    dataset = Member.objects.all()
    data = serializers.serialize('json', dataset)
    return JsonResponse(data, safe=False)


def pivot_data3(request):
    dataset = Event.objects.all()
    data = serializers.serialize('json', dataset)
    return JsonResponse(data, safe=False)



