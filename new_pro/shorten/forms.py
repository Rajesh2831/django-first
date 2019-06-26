from django import forms
from .models import bitly



class bitlyform(forms.ModelForm):
    class Meta:
        model=bitly
        fields=['long_url']

class editbitly(forms.ModelForm):
    class Meta:
        model = bitly

        fields = ["long_url","shortcode"]
