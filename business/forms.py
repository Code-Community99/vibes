from django.forms import ModelForm,TextInput , FileInput , Textarea
from .models import sell_goods

class sell_frm(ModelForm):
    class Meta:
        model = sell_goods
        fields = ('Gtitle','GDescription' , 'Gprice' , "Gphoto")
        labels = {
        "Gtitle":"Item name",
        "GDescription":"Description",
        "Gprice":"Price",
        "Gphoto":"Photo",
        }
        widgets = {
            "Gtitle":TextInput(attrs = {"name": "itemname" , "maxlength":20 , "placeholder":"name"}),
            "GDescription":Textarea(attrs = {"name": "itemdescription" , "cols":20,"rows":3 , "maxlength":50  , "placeholder":"Description"}),
            "Gprice":TextInput(attrs = {"name": "itemprice"  , "maxlength":5  , "placeholder":"Price"}),
            "Gphoto":FileInput(attrs = {"name": "itemphoto"}),
        }
