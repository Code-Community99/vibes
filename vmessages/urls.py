from django.conf.urls import url
from . import views

app_name = "messaging"


urlpatterns = [
    url('^$' , views.display , name = 'display'),
    # url('^display/' , views.display , name = 'display'),
    url('^(?P<receiverId>[\d]+)/$' , views.messaging , name = 'messaging'),
]
