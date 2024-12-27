from django import forms
from .models import Hesabi



class HesabiForm(forms.ModelForm):
    class Meta:
        model = Hesabi
        fields = '__all__'

class HesabiUpdateForm(forms.ModelForm):
    class Meta:
        model = Hesabi
        fields = '__all__'

