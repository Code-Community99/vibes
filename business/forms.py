from django import forms
from .models import sell_goods

class sell_frm(forms.ModelForm):
    class Meta:
        model = sell_goods
        fields = ('Gtitle','GDescription' , 'Gprice' , "Gphoto")

        widgets = {
            'itemdesc':forms.Textarea(attrs = {'rows':4 , 'cols':30 , 'name':'description' , "label":"Description"}),
        }
