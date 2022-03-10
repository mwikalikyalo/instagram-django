from django import forms
from .models import Profile, Image, Comments

#create forms
class ImagesForm(forms.ModelForm):
    class Meta:
        model = Image
        exclude = ['profile', 'created_date']

