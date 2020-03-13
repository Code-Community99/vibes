from django.contrib import admin
from .models import Groups,Members
# Register your models here.

class viewer(admin.ModelAdmin):
    model = Members
    list_display = ("group_member",)

admin.site.register(Members , viewer)



class viewer(admin.ModelAdmin):
    model = Groups
    list_display = ("id","group_name" , "group_location" , "group_icon")


admin.site.register(Groups , viewer)
