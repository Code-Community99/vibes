from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def notifications(request):
    return render(request , "notifications/notifications.html")
