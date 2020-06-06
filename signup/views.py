from django.shortcuts import render,redirect
from django.http import HttpResponse
# Create your views here.
from .models import signup as signmodel
from django.contrib.auth.hashers import make_password
import validate_email as v , json


def password_master(pass1,pass2):

    if pass1==pass2:
        return True
    else:
        return False
def signup(request):
    data_logger = dict()
    bugs = dict()
    data_logger["errors"] = True
    if request.method == "POST":
        username = request.POST['username']
        pnumber = request.POST['pnumber']
        email = request.POST['email']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']
        hobby = request.POST['hobby']
        location = request.POST["location"]
        profilepic = request.FILES['profilepic']
        passwordflag = password_master(pass1 , pass2)

        try:
            signmodel.objects.get(username = username)
        except Exception as e:
            try:
                signmodel.objects.get(email = email )
            except Exception as e:
                if v.validate_email(email):
                    if passwordflag:
                        password = make_password(request.POST['pass1'])
                        signmodel.objects.create(username = username , pnumber = pnumber , email = email , password = password ,
                        hobby = hobby, location = location , profilepic = profilepic)
                        data_logger["redirect"] = "/login/"
                        data_logger["errors"] = False
                        data_logger = json.dumps(data_logger)
                    else:
                        bug["passwordvalid"] = "Password not correct"
                        data_logger["fields"] = json.dumps(bugs)
                        data_logger = json.dumps(data_logger)
                else:
                    bugs["emailvalid"] = "Email does not exists"
                    data_logger["fields"] = json.dumps(bugs)
                    data_logger = json.dumps(data_logger)
            else:
                bugs["emailvalid"]  = "Another account is using that email"
                data_logger["fields"] = json.dumps(bugs)
                data_logger = json.dumps(data_logger)
        else:
            bugs["usernamevalid"] = "User exists"
            data_logger["fields"] = json.dumps(bugs)
            data_logger = json.dumps(data_logger)
        return HttpResponse(data_logger ,  content_type="application/json")
    else:
        return render(request , "signup/signup.html")

# username is in use?
def userauthentication(request):
    try:
        uname = request.POST['username']

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
        email = request.POST['email']

    except Exception as e:
        pass

    else:
        try:
            signmodel.objects.get(email = email)

        except Exception as e:
            if v.validate_email(email):
                return HttpResponse("false")
            else:
                return HttpResponse("Email not found")

        else:
            return HttpResponse("true")
