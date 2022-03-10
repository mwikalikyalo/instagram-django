from django import forms
from .models import Comments, Profile, Image
from django.contrib.auth.models import User

#create forms
class ImagesForm(forms.ModelForm):
    class Meta:
        model = Image
        exclude = ['profile', 'created_date']

class CommentsForm(forms.ModelForm):
    class Meta:
        model = Comments
        

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ['user'] 
        