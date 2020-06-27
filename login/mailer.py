import smtplib as sm ,validate_email as v,string,random
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

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
                userdata = Signup.objects.get(email = lostuser)
            except Signup.DoesNotExist as e:
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
                        obj=sm.SMTP('smtp.gmail.com', 587)
                        obj.starttls()
                        obj.login("anornymous99@gmail.com","xcmbyzwvy")
                        obj.sendmail(sender,receiver,mess.as_string())
                        obj.close()
                    except Exception as error:
                        print("Error: {}".format(error))
                        bug_hunter.append("Connection could not be established")
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
