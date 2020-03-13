from django.conf.urls import url
from . import views

app_name = "profile"


urlpatterns = [
    url('^$' , views.profile , name = 'profile'),
    url("^events/" , views.event_manager , name = "event_manager"),
]
