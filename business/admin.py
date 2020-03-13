from django.contrib import admin
from .models import sell_goods


class admininterface(admin.ModelAdmin):

    model = sell_goods
    list_display = ("GoodId" , "Gtitle" , "GDescription" , "GLocation" , "Gprice" , "Gphoto" , "Sid")

admin.site.register(sell_goods, admininterface)
