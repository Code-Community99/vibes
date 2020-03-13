from django.shortcuts import render ,redirect
from .models import MsgContent
from django.http import HttpResponse
from signup.models import signup
from django.db.models import Count ,Q
# Create your views here.


def display(request):
    # url = ""
    try:
        request.session["username"]
    except Exception as e:
        return redirect("/login/")
    else:
        peoples = signup.objects.all()
        list = []
        cou = 0
        for people in peoples:
            x =0
            peopleId = people.uid
            try:
                counter = MsgContent.objects.filter(ruid_id = peopleId , readStatus = 0).order_by("postTime")
                for c in counter:
                    x = x+1
                    # print(c)
                list.append(x)
                people.id= list[cou]
                # print(counter.last().postTime)
                people.date = counter.last().postTime
                people.msg = counter.last().message
            except Exception as e:
                people.date = ""
                people.msg = ""
            # print(people.uid)
            # print(counter.last().message)
            cou = cou +1
        senderName = request.session["username"]
        return render(request , "messages/people.html" , {"peoples":peoples , "senderName":senderName})

def messaging(request , receiverId):
    i = 0
    mes = MsgContent.objects.filter(readStatus = 0).order_by("postTime")
    for m in mes:
        i = i+1
    try:
        request.session["username"]

    except Exception as e:
        return redirect("/login/")

    else:
        peoples = signup.objects.all()
        list = []
        cou = 0
        for people in peoples:
            x =0
            peopleId = people.uid
            try:
                counter = MsgContent.objects.filter(suid_id = peopleId , readStatus = 0).order_by("postTime")
                for c in counter:
                    x = x+1
                    # print(c)
                list.append(x)
                people.id= list[cou]

            except Exception as e:
                people.date = ""
                people.msg = ""
            cou = cou +1
        senderName = request.session["username"]
        senderId = signup.objects.get(username = senderName).uid
        receiverId = receiverId
        receicerName = signup.objects.get(uid = receiverId)


        messages = MsgContent.objects.filter(Q(ruid_id = receiverId ,suid_id = senderId)|Q(ruid_id = senderId ,suid_id = receiverId))

        individualSum = 0
        for m in messages:
            # print(m.readStatus)
            individualSum =individualSum+1
            # print(individualSum)
            # print("hi")
        if request.method == "POST":
            msgPosted = request.POST['msgPosted']
            if msgPosted == "":
                return redirect("/messages/")
            else:
                try:
                    MsgContent.objects.create(message = msgPosted , ruid_id = receiverId , suid_id = senderId)
                except Exception as e:
                    return render(request , "messages/messages.html" , {"messages":messages, "i":i,"individualSum":individualSum ,"senderName":senderName,"peoples":peoples , "receicerName":receicerName})
                else:
                    messages = MsgContent.objects.filter(Q(ruid_id = receiverId ,suid_id = senderId)|Q(ruid_id = senderId ,suid_id = receiverId))
                    messages.readStatus =True
                    return render(request , "messages/messages.html" , {"messages":messages , "i":i,"individualSum":individualSum,"senderName":senderName,"peoples":peoples , "receicerName":receicerName})

        else:
            return render(request ,"messages/messages.html" ,{"messages":messages, "i":i ,"senderName":senderName,"individualSum":individualSum,"peoples":peoples , "receicerName":receicerName})
