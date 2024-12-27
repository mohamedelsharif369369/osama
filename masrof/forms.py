from django import forms
from .models import Masrof


class MasrofForm(forms.ModelForm):
    class Meta:
        model = Masrof
        fields = ['msrof','name','day','date']

class MasrofUpdateForm(forms.ModelForm):
    class Meta:
        model = Masrof
        fields = ['msrof','name','day','date']
