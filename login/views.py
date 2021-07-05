from django.contrib.auth.hashers import check_password,make_password
from django.shortcuts import render , redirect
from django.http import HttpResponse
from signup.models import signup
import smtplib,string,random
import validate_email as v
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
def login(request):
    try:
        request.session["username"]
    except Exception as e:
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
    else:
        return redirect("/")



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
                    message = "Your recovery code is <strong>%s </strong><a href='devcodes.herokuapp.com/login/updatereset/'> reset link</a>"%hashcode
                    mess = MIMEMultipart("alternatives")
                    mess["From"] = "devcodesv1@gmail.com"
                    mess["To"] = receiver
                    mess["Subject"] = "Devcodes recovery code."
                    message = MIMEText( message, "html")
                    mess.attach(message)
                    try:
                        obj=smtplib.SMTP('smtp.gmail.com', 587)
                        obj.starttls()
                        obj.login("anornymous99@gmail.com","xcmbyzwvy")
                        obj.sendmail(sender,receiver,mess.as_string())
                        obj.close()
                    except Exception as error:
                        bug_hunter.append("Connection could not be established")
                        print("Errors;;;;;%s"%(error))
                        return render(request , "login/forgot.html" , context = {"error":bug_hunter})

                    else:
                        Recoverdata.objects.create(uid_id = Signup.objects.get(email = receiver).uid , secret_code = hashcode)
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
