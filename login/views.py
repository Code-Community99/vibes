from django.shortcuts import render , redirect
from django.http import HttpResponse
from signup.models import signup
import smtplib,string,random
# import validate_email as v
from django.contrib.auth.hashers import check_password,make_password



def login(request):
    if request.method == "POST":
        error_log = list()
        username = request.POST['username']
        password = request.POST['password']

        try:
            userinfo = signup.objects.get(username = username)
            username = userinfo.username

        except Exception as e:
            error_log.append(" Wrong credentials")

            return render(request , "login/login.html" , context = {"error_log" : error_log})

        else:
            if check_password(password , userinfo.password):

                # add username to the session
                request.session["username"] = username
                request.session['items'] = list()
                request.session["loginstatus"] = True

                # set the sessions expiry date
                request.session.set_expiry(0)
                # redirect user to home page
                return redirect("/")
            else:
                error_log.append("Wrong credentials")
                return render(request , "login/login.html" , context = {"error_log" : error_log})


    else:
        return render(request , "login/login.html")



def forgotcredetials(request):

    bug_hunter = []

    if request.method == "POST":
        try:
            lostuser = request.POST['email']

        except Exception as e:
            bug_hunter.append("Invalid input")
            return render(request , "login/forgot.html" , context = {"error":bug_hunter})

        else:
            try:
                userdata = signup.objects.get(email = lostuser)

            except signup.DoesNotExist as e:
                bug_hunter.append("Email not registered with us")
                return render(request , "login/forgot.html" , context = {"error":bug_hunter})

            else:

                if v.validate_email(lostuser):
                    hashcode = string.digits + string.ascii_letters + string.digits + string.digits
                    hashcode = "".join([random.choice(hashcode) for value in range(10)])
                    sender = "anornymous99@gmail.com"
                    receiver = lostuser

                    message = """From: %s
                    To: %s
                    Content-Type:text/html
                    Mime-version:1.0
                    Content-disposition: text
                    Subject:Vibes reset password is: %s
                    """%("anornymous99@gmail.com",receiver , hashcode)

                    try:
                        obj=smtplib.SMTP('smtp.gmail.com', 587)
                        obj.starttls()
                        obj.login("anornymous99@gmail.com","xcmbyzwvy")
                        obj.sendmail(sender,receiver,message)

                    except Exception as error:
                        print("Error: {}".format(error))
                        bug_hunter.append("Connection could not be established")
                        return render(request , "login/forgot.html" , context = {"error":bug_hunter})

                    else:
                        userdata.password = make_password(hashcode)
                        userdata.save()
                        print("Message sent successfully to {}".format(receiver))
                        print("Exiting the mail client program")
                        return render(request , "login/thanks.html")
                else:

                    return render(request , "login/forgot.html" , context = {"error":bug_hunter})

    else:
        return render(request , "login/forgot.html" , context = {"error":bug_hunter})



def logout(request):
    # clear the session variables
    request.session.clear()
    request.session.flush()
    request.session["loginstatus"] = False
    return redirect("/")
