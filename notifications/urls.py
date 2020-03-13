from django.conf.urls import url
from . import views

app_name = "notifications"


urlpatterns = [
    url('^$' , views.notifications , name = 'notifications'),
]
