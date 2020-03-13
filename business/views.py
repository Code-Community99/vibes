from django.shortcuts import render,redirect
from django.http import HttpResponse
from .forms import sell_frm
from .models import sell_goods
from signup.models import signup



def business(request):
    dataitems = sell_goods.objects.all()

    try:
        uname = request.session["username"]

    except KeyError as e:
        # KeyError
        return redirect("/login/")

    else:
        

        form = sell_frm()
        if request.method =='POST':
            Gtitle = request.POST['Gtitle']
            GDescription = request.POST['GDescription']
            Gprice = request.POST['Gprice']
            Gphoto = request.FILES['Gphoto']
            Sid = signup.objects.get(username = uname).uid
            sell_goods.objects.create(Gtitle = Gtitle , GDescription = GDescription , Gprice = Gprice , Gphoto = Gphoto , Sid_id = Sid)
            return render(request , "business/business.html" , context = {"form":form , "dataitems":dataitems})

        else:
            return render(request , "business/business.html" , context = {"form":form , "dataitems":dataitems})







def cart(request):
    try:
        request.session['username']

    except Exception as e:
        return redirect("/")

    else:
        data = request.session['items']
        data.append(request.POST['itemid'])
        request.session['items'] = data
        print(request.session['items'])
        return redirect("/business/")



def viewcart(request):
    data_items = []

    for x in request.session['items']:
        data_items.append(sell_goods.objects.filter(GoodId = int(request.session['items'][int(x)])))


    print(data_items)

    return HttpResponse("Cart")
