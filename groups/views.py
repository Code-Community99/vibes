from django.shortcuts import render,redirect
from django.http import HttpResponse
from discover.models import Followers
from signup.models import signup
from .models import Groups as Groupmodel,Members , Group_content as gc
from .forms import gform
from django.db.models import Count
from django.db.models import Count
import json
from notifications.models import notif
# Create your views here.
def groupsview(request):
    try:
        request.session['username']
        users = Followers.objects.filter(user_following_id = signup.objects.get(username = request.session['username']).uid)
    except Exception as e:
        return redirect("/login/")
    else:
        Group = Groupmodel.objects.order_by("-group_create")
        return render(request , "groups/group.html" , context = {"users":users , "Group":Group , "current":request.session['username']})

def creategroup(request):
    form = gform()
    if request.method =="POST":
        user_data = signup.objects.get(username = request.session['username'])
        try:
            group_name = request.POST['group_name']
            group_icon = request.FILES['group_icon']
            group_description = request.POST['group_description']

        except KeyError as e:
            print("{}\n\n\n\n".format(e))
            return render(request , "groups/add.html" , context = {"form":form})
        else:
            mem = Members(group_member_id = user_data.uid)
            obj1 = Groupmodel.objects.create(group_name = group_name ,
            group_icon = group_icon , group_location = "Nairobi/Kenya" ,
            group_description = group_description , group_admin_id = user_data.uid)
            mem.save()
            mem.group_id.add(obj1)
            mem.save()
            return redirect("/groups/")
    else:
        return render(request , "groups/add.html" , context = {"form":form})

def join_group(request , gid):
    try:
        user = signup.objects.get(username = request.session['username'])
    except Exception as e:
        return redirect("/login/")
    else:
        try:
            mem = Members(group_member_id = user.uid)
            obj1 = Groupmodel.objects.get(id = gid)
            mem.save()
            mem.group_id.add(obj1)
            mem.save()
            obj1.save()
        except Exception as e:
            return redirect("/groups/")
        else:
            # contact admin and inform of the join
            admin = obj1.group_admin_id
            notif.objects.create(source_id = mem.group_member.uid, destination_id = admin,message = user.username + " just joined " + obj1.group_name)
            return redirect("/groups/")

def group_viewer(request , group_name):
    GroupName = Groupmodel.objects.get(id = group_name)
    GroupInfor = Groupmodel.objects.get(id = group_name)
    admin_name = Groupmodel.objects.get(id = group_name).group_admin
    group_member_count = Groupmodel.objects.get(id = group_name).members_set.all().count()
    all_topics = gc.objects.filter(group_post_own_id = group_name)
    myinfo = signup.objects.get(username = request.session["username"])
    return render(request , "groups/onegroup.html" , context = {"GroupName":GroupName , "groupinfor":GroupInfor , "myinfo":myinfo, "groupadmin":admin_name , "member_count":group_member_count  , "group_topics":all_topics})


def post_to_group(request , gid):
    if request.method =="POST":
        try:
            userinfo = signup.objects.get(username = request.session["username"])
        except Exception as e:
            return redirect("/groups/")
        else:
            post_obj = gc.objects.create(poster_id = userinfo.uid , group_post_own_id = gid , post_content = request.POST["post_content"])
            profilepic = ""
            # post_obj.poster.profilepic
            return HttpResponse(json.dumps({"response":True, "poster_name":post_obj.poster.username, "responsetext":request.POST["post_content"] ,"poster_img":profilepic}) , content_type = "application/json")
