from django.shortcuts import render
from django.http import HttpResponse
from .models import notif
from signup.models import signup


def notifications(request):
    try:
        request.session['username']

    except KeyError as e:
        return redirect("/login/")

    else:
        current = signup.objects.get(username = request.session['username'])
        notify = notif.objects.filter(destination_id = current.uid).order_by("-notiftime")
        return render(request , "notifications/notifications.html" , context = {"notify":notify})
