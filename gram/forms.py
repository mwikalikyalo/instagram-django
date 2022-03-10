from django import forms
from .models import Profile, Image
from django.contrib.auth.models import User

#create forms
class ImagesForm(forms.ModelForm):
    class Meta:
        model = Image
        exclude = ['profile', 'created_date']
        fields = ('image_caption', 'image', 'tag_someone',)

class SignUpForm(forms.ModelForm):
  class Meta:
    model = Profile
    exclude = ['bio','profile_pic','profile_avatar','date']
