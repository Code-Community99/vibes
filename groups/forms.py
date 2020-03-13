from django.forms import *
from .models import Groups


class gform(ModelForm):
    class Meta:
        model = Groups
        fields = ("group_name" ,"group_description", "group_icon")
