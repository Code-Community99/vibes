from django.conf.urls import url
from . import views

app_name = "signup"


urlpatterns = [
    url('^$' , views.signup , name = 'signup'),
    url('^userauthentication/' , views.userauthentication , name = 'userauthentication'),
    url('^emailauthentication/' , views.emailauthentication , name = 'emailauthentication'),
]
