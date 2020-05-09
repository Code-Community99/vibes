from django.forms import *
from .models import Groups


class gform(ModelForm):
    class Meta:
        model = Groups
        fields = ("group_name" ,"group_description", "group_icon")

        widgets = {
        "group_name":TextInput(attrs = {"name":"GName" , "required":"True" , "maxlength":15}),
        "group_description":Textarea(attrs = {"name":"Description" , "rows":5 , "cols":24 , "required":True , "maxlength":100}),
        }
        labels = {
        "group_name":"Name",
        "group_description":"description",
        "group_icon":"Group Icon",
        }
