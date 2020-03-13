from django.shortcuts import render,redirect
from django.http import HttpResponse
# Create your views here.
from signup.models import signup
from .forms import eventfrm as eventform
from .models import events
from discover.models import Followers



def profile(request):
    error_log = list()
    try:
        userinfo = request.session['username']

    except Exception as e:
        return redirect("/login/")

    else:
        userinfo = signup.objects.get(username = userinfo)

        evnt = events.objects.all()
        print(evnt)

        return render(request , "uprofile/uprofile.html" , context = {"userinfo":userinfo , "evnt":evnt})




def event_manager(request):
    if request.method == "POST":
        try:
            userinfo = signup.objects.get(username = request.session['username'])

        except Exception as e:
            print("\n\n\n\n{}".format(e))
            return redirect("/login/")

        else:
            usereventid = userinfo.uid
            event_name = request.POST['event_name']
            event_description = request.POST['event_description']
            event_brief_pic = request.FILES['event_brief_pic']

            events.objects.create(usereventid_id = usereventid, event_name = event_name, event_description = event_description, event_brief_pic = event_brief_pic)
            return redirect("/profile/")
    else:
        return render(request , "uprofile/add.html" , context = {"form": eventform})
