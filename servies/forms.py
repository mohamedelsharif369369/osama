from django import forms
from .models import Servie

class ServieForm(forms.ModelForm):
    class Meta:
        model = Servie
        fields = '__all__'


class ServieUpdateForm(forms.ModelForm):
    class Meta:
        model = Servie
        fields = '__all__'
