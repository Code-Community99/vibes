from django.shortcuts import render

# Create your views here.


def home(request):
    return render(request , "home/home.html" , context = {"loginstatus":request.session.get("loginstatus")})
