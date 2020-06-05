from django.shortcuts import render ,redirect
from .models import MsgContent
from django.http import HttpResponse
from signup.models import signup
from django.db.models import Count ,Q,Sum
# Create your views here.
from itertools import chain

def display(request):
    # url = ""
    try:
        request.session["username"]
    except Exception as e:
        return redirect("/login/")
    else:
        peoples = signup.objects.all().exclude(username=request.session["username"])
        list = []
        cou = 0
        for people in peoples:
            x =0
            peopleId = people.uid
            try:
                counter = MsgContent.objects.filter(ruid_id = peopleId , readStatus = 0).order_by("postTime")
                for c in counter:
                    x = x+1
                list.append(x)
                people.id= list[cou]
                people.date = counter.last().postTime
                people.msg = counter.last().message
            except Exception as e:
                people.date = ""
                people.msg = ""
            cou = cou +1
        senderName = request.session["username"]
        return render(request , "messages/people.html" , {"peoples":peoples , "senderName":senderName})


def messagefilter(myid):
    refined_data = list()
    ids_data = list()
    messages = MsgContent.objects.filter(Q(ruid=myid) | Q(suid=myid)).annotate(no_of_messages = Count("ruid_id")).order_by("-postTime")

    for x in messages:
        if (x.suid_id == myid) and (x.ruid_id not in ids_data):
            ids_data.append(x.ruid_id)
            refined_data.append(x.ruid)
        elif (x.ruid_id == myid) and (x.suid_id not in ids_data):
            ids_data.append(x.suid_id)
            refined_data.append(x.suid)

    return refined_data

def messaging(request , receiverId):
    userinfo = signup.objects.get(username = request.session["username"])
    messages = MsgContent.objects.filter(Q(suid = receiverId , ruid=userinfo.uid) | Q(ruid = receiverId , suid=userinfo.uid)).order_by("postTime")
    msgcount = len(messages)
    peoples = messagefilter(userinfo.uid)
    receicerName = signup.objects.get(uid = receiverId)
    if receicerName.uid==userinfo.uid:
        return redirect("/messages/")
    else:
        if request.method=="POST":
            MsgContent.objects.create(message = request.POST["msgPosted"],suid_id = userinfo.uid, ruid_id = receiverId)
            messages = MsgContent.objects.filter(Q(suid = receiverId , ruid=userinfo.uid) | Q(ruid = receiverId , suid=userinfo.uid)).order_by("postTime")
            msgcount = len(messages)
            messages = MsgContent.objects.filter(Q(suid = receiverId , ruid=userinfo.uid) | Q(ruid = receiverId , suid=userinfo.uid)).order_by("postTime")
            msgcount = len(messages)
            peoples = messagefilter(userinfo.uid)
            return render(request , "messages/messages.html" , {"messages":messages , "userinfo":userinfo, "individualSum":msgcount,"senderName":userinfo,"peoples":peoples , "receicerName":receicerName})
        else:
            return render(request , "messages/messages.html" , {"messages":messages , "userinfo":userinfo, "individualSum":msgcount,"senderName":userinfo,"peoples":peoples , "receicerName":receicerName})
