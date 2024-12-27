from django import forms
from .models import Manzom

class ManzomForm(forms.ModelForm):
    class Meta:
        model = Manzom
        fields = ['code','quantity','price','date','img']

class ManzomUpdateForm(forms.ModelForm):
    class Meta:
        model = Manzom
        fields = ['code','quantity','price','date','img']