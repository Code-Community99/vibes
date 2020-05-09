from django.conf.urls import url
from . import views

app_name = "groups"


urlpatterns = [
url('^$' , views.groupsview , name = 'groups'),
url("^viewgroup/(?P<group_name>[\d]+)/$" , views.group_viewer , name = "group_viewer"),
url("^creategroup/$" , views.creategroup , name = "creategroup"),
url("^creategroup(?P<gid>[\d]+)/$" , views.join_group , name = "join_group"),

]
