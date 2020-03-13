from django.contrib import admin
from .models import events

class viewer(admin.ModelAdmin):
    model = events
    list_display = ("eid","usereventid" , "event_name" , "event_description" , "post_time" , "event_brief_pic")


admin.site.register(events , viewer)
