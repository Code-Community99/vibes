from django.contrib import admin
from .models import Followers
# Register your models here.

class adminshowfollow(admin.ModelAdmin):
    class Meta:
        model = Followers
        list_display = ['fid' , 'follower.username' , 'following.username']

admin.site.register(Followers)
