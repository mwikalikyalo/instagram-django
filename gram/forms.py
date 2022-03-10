from django import forms
from .models import Profile, Image
from django.contrib.auth.models import User

#create forms
class ImagesForm(forms.ModelForm):
    class Meta:
        model = Image
        exclude = ['profile', 'created_date']

