from django.shortcuts import render , redirect
from django.http import HttpResponse
from signup.models import signup
from django.contrib.auth.hashers import make_password
# import validate_email as v
# Create your views here.

def settings(request):
    try:
        request.session["username"]
    except Exception as e:
        print("ERROR:"+str(e))
        return redirect('/login/')

    else:
        user = request.session["username"]
        #check the details of the loggen in user

        try:
            details = signup.objects.get(username = user)
        except Exception as e:
            print("ERROR2:"+str(e))
            return redirect("/login/")
        else:
            print(details.email)
            return render(request , 'settings/settings.html' , {"details":details})
    # return HttpResponse("Hello settings")


def ChangeDetails(request):
    print("Already startes the block")
    try:
        user = request.session["username"]
    except Exception as e:
        print("Details Error:"+str(e))
        return redirect("/login/")
    else:
        print("Hello")
        userId = signup.objects.get(username = user).uid
        print("Hello2")
        try:
            changer = signup.objects.get(uid = userId)
        except Exception as e:
            #modified later to a page
            return HttpResponse("An error Occured")

        else:
            #get the data from the db from the form
            if request.method == "POST":
                username = request.POST["username"]
                email = request.POST["email"]
                pnumber = request.POST["pnumber"]

                changer.username = username
                changer.email = email
                changer.pnumber = pnumber
                changer.save()
                request.session['username'] = username
                return redirect("/messages/")
            else:
                return redirect("/settings/")


def changePas(request):
    try:
        request.session["username"]
    except Exception as e:
        return redirect("/login/")
    else:
        userId=signup.objects.get(username = request.session["username"]).uid
        if request.method == "POST":
            #get the deatail
            pass1 = request.POST["psw"]
            pass2 = request.POST["cpsw"]
            currpass = request.POST["currpsw"]
            username = request.POST["uname"]

            if username == request.session["username"]:
                if pass1 == pass2:
                    try:
                        obj = signup.objects.get(username = request.session["username"])
                    except Exception as e:
                        print(e)

                    else:
                        #hash the password
                        password = make_password(pass1)
                        obj.password = password
                        obj.save()
                        print("data adjusted.\n\n\n\nn\n")
                        return redirect("/settings/")

                else:
                    return HttpResponse("Password does not much")

            else:
                return HttpResponse("Username does not much")

        else:
            return render(request , "/settings/")
