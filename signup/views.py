from django.shortcuts import render,redirect
from django.http import HttpResponse
# Create your views here.
from .models import signup as signmodel
from django.contrib.auth.hashers import make_password
import validate_email as v



def password_master(pass1,pass2):

    if pass1==pass2:
        return True

    else:
        return False


def signup(request):
    error_log = list()
    if request.method == "POST":
        username = request.POST['username']
        pnumber = request.POST['pnumber']
        email = request.POST['email']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']
        hobby = request.POST['hobby']
        profilepic = request.FILES['profilepic']
        # location = "Hello"
        passwordflag = password_master(pass1 , pass2)

        if passwordflag:
            password = make_password(request.POST['pass1'])
            if v.validate_email(email):
                try:
                    signmodel.objects.get(email = email)
                except Exception as e:
                    try:
                        signmodel.objects.get(username = username)

                    except Exception as e:
                        signmodel.objects.create(username = username , pnumber = pnumber , email = email , password = password ,
                        hobby = hobby , profilepic = profilepic)
                        return redirect("/login/")

                    else:
                        error_log.append("User exists")
                        print("\n\n\n\n\n{}".format(error_log))
                        return render(request , "signup/signup.html" , context = {"error_log":error_log})

                else:
                    error_log.append("User exists")
                    print("\n\n\n\n\n{}".format(error_log))
                    return render(request , "signup/signup.html" , context = {"error_log":error_log})
            else:
                error_log.append("Email does not exists")
                return render(request , "signup/signup.html" , context = {"error_log":error_log})

        else:
            error_log.append("Password not correct")
            return render(request , "signup/signup.html" , context = {"error_log":error_log})

    else:
        return render(request , "signup/signup.html")



# username is in use?
def userauthentication(request):
    try:
        uname = request.GET['username']

    except Exception as e:
        pass

    else:
        try:
            signmodel.objects.get(username = uname)

        except Exception as e:
            return HttpResponse("false")

        else:
            return HttpResponse("true")



# email is in use?
def emailauthentication(request):
    try:
        email = request.GET['email']

    except Exception as e:
        pass

    else:
        try:
            signmodel.objects.get(email = email)

        except Exception as e:
            if v.validate_email(email):
                print(v.validate_email(email))
                return HttpResponse("false")
            else:
                print(v.validate_email(email))
                return HttpResponse("Email not found")

        else:
            return HttpResponse("true")
