from django.forms import ModelForm , Textarea , TextInput
from .models import events


class eventfrm(ModelForm):
    class Meta:
        model = events
        fields = ("event_name" , "event_description" , "event_brief_pic")
        widgets = {
            "event_name":TextInput(attrs = {"placeholder": "Hello world"}),
            "event_description":Textarea(attrs = {"cols":30,"rows":10})
        }
        labels = {
        "event_name":"Taskmate",
        "event_description":"Description",
        "event_brief_pic":"Event clip",
        }
