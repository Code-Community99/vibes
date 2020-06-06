from django.shortcuts import render,redirect
from django.http import HttpResponse
# Create your views here.
from signup.models import signup
from django.db.models import Count,Q
from .models import Followers
from userfriendly_api import model

def discover(request):
    try:
        userdetails = signup.objects.get(username = request.session['username'])
        all_info = signup.objects.all()
    except KeyError as e:
        return redirect("/login/")
    else:
        if userdetails.location is not None:
            model_user = model.vibes_friends(userdetails)
            all_info = model_user.model_report()
        else:
            model.predict_user_location(userdetails)
            model_user = model.vibes_friends(userdetails)
            all_info = model_user.model_report()

        users = signup.objects.exclude(username = request.session['username']).annotate(follow = Count("followingcounter")  ,
        follower = Count("followercounter") , totalchaining = Count("followercounter__user_follower") + Count("followingcounter__user_follower")).order_by("-totalchaining")
        around = signup.objects.filter(location = signup.objects.get(username = request.session['username']).location).exclude(username =
        request.session['username']).annotate(follow = Count("followercounter") , follower = Count("followingcounter"))
        around = all_info
        return render(request , "discover/discover.html" , context = {"users":users , "around": around , "userdetails":userdetails})



def followBot(request):
    try:
        uuid = signup.objects.get(username = request.session['username']).uid
        fid = request.POST["userid"]
    except Exception as e:
        return redirect("/login/")

    else:
        Followers.objects.create(user_follower_id = uuid,user_following_id = fid)
        return HttpResponse("Followed")



def unfollowBot(request):
    pass
