from django.shortcuts import render,redirect
from django.http import HttpResponse
from discover.models import Followers
from signup.models import signup
from .models import Groups as Groupmodel,Members
from .forms import gform
from django.db.models import Count
# Create your views here.


def groupsview(request):
    try:
        request.session['username']
        users = Followers.objects.filter(following_id = signup.objects.get(username = request.session['username']).uid)
    except Exception as e:
        return redirect("/login/")
    else:
        Group = Groupmodel.objects.all()

        return render(request , "groups/group.html" , context = {"users":users , "Group":Group , "current":request.session['username']})





def creategroup(request):
    if request.method =="POST":
        user_data = signup.objects.get(username = request.session['username'])
        try:
            group_name = request.POST['group_name']
            group_icon = request.FILES['group_icon']
            group_description = request.POST['group_description']

        except Exception as e:
            return render(request , "groups/add.html" , context = {"form":gform})

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
        return render(request , "groups/add.html" , context = {"form":gform})






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
            obj.save()

        except Exception as e:
            return redirect("/groups/")

        else:
            return redirect("/groups/")

def group_viewer(request):
    return HttpResponse("Hello world")
