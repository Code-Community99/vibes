from django.conf.urls import url
from . import views

app_name = "settings"


urlpatterns = [
    url('^$' , views.settings , name = 'settings'),
    url('^details/' , views.ChangeDetails , name = 'settingsDetails'),
    url('^pass/' , views.changePas , name = 'settingsPass'),
]
