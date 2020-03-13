from django.forms import ModelForm
from .models import events


class eventfrm(ModelForm):
    class Meta:
        model = events
        fields = ("event_name" , "event_description" , "event_brief_pic")
