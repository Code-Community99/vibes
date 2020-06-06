from django.shortcuts import render,redirect
from django.http import HttpResponse
from discover.models import Followers
from signup.models import signup
from .models import Groups as Groupmodel,Members
from .forms import gform
from django.db.models import Count
from django.db.models import Count

from notifications.models import notif
# Create your views here.


def groupsview(request):
    try:
        request.session['username']
        users = Followers.objects.filter(user_following_id = signup.objects.get(username = request.session['username']).uid)
    except Exception as e:
        return redirect("/login/")
    else:
        for x in users:
        Group = Groupmodel.objects.order_by("-group_create")

        return render(request , "groups/group.html" , context = {"users":users , "Group":Group , "current":request.session['username']})

def creategroup(request):
    form = gform()
    if request.method =="POST":
        user_data = signup.objects.get(username = request.session['username'])
        try:
            group_name = request.POST['group_name']
            group_icon = request.FILES['group_icon']
            group_description = request.POST['Description']

        except Exception as e:
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
    GroupName = Groupmodel.objects.get(id = group_name).group_name
    GroupInfor = Groupmodel.objects.get(id = group_name)
    admin_name = Groupmodel.objects.get(id = group_name).group_admin
    group_member_count = Groupmodel.objects.get(id = group_name).members_set.all().count()
    return render(request , "groups/onegroup.html" , context = {"GroupName":GroupName , "groupinfor":GroupInfor , "groupadmin":admin_name , "member_count":group_member_count})
