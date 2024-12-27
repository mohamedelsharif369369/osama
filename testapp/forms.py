from django import forms
from .models import ImageUser

class ImageUserForm(forms.ModelForm):
    class Meta:
        model = ImageUser
        fields = ['img','date']

class ImageUpdateForm(forms.ModelForm):
    class Meta:
        model = ImageUser
        fields = ['img','date']