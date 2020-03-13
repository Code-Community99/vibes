from django.conf.urls import url
from . import views

app_name = "business"


urlpatterns = [
    url('^$' , views.business , name = 'business'),
    url("^cart/" , views.cart , name = "cart"),
    url("^viewcart/" , views.viewcart , name = "viewcart")
]
