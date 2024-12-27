from django import forms
from .models import Yaomia

class YaomiaForm(forms.ModelForm):
    class Meta:
        model = Yaomia
        fields = '__all__'


class YaomiaUpdateForm(forms.ModelForm):
    class Meta:
        model = Yaomia
        fields = '__all__'