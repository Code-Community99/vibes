from django.contrib import admin
from .models import signup
# Register your models here.


# Cutom admin panel

class admininterface(admin.ModelAdmin):

    model = signup
    list_display = ("email" , "username" , "pnumber" , "location" , "hobby" , "profilepic" , "password")

admin.site.register(signup, admininterface)
