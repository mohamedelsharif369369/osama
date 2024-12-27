from django import forms
from .models import Manzoma,Hesabi,Masrof,Product,Servie,Yaomia

class ManzomaForm(forms.ModelForm):
    class Meta:
        model = Manzoma
        fields = '__all__'


class HesabiForm(forms.ModelForm):
    class Meta:
        model = Hesabi
        fields = '__all__'


class MasrofForm(forms.ModelForm):
    class Meta:
        model = Masrof
        fields = '__all__'


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'


class ServieForm(forms.ModelForm):
    class Meta:
        model = Servie
        fields = '__all__'


class YaomiaForm(forms.ModelForm):
    class Meta:
        model = Yaomia
        fields = '__all__'
