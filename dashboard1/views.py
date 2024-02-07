from django.shortcuts import render

# Create your views here.

# dashboard/views.py

from django.shortcuts import render

def dashboard1(request):
    return render(request, 'dashboard1/dashboard1.html')

