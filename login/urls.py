from django.conf.urls import url
from . import views

app_name = "login"


urlpatterns = [
    url('^$' , views.login , name = 'login'),
    url("^forgot/" , views.forgotcredetials , name = 'forgot'),
    url("^logout/" , views.logout , name = "logout")
]
