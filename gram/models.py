from django.utils import timezone
from django.db import models

# Create your models here.
class Image(models.Model):
  image= models.ImageField(blank=True, null=True)
  image_names= models.CharField(max_length=100)
  image_caption= models.CharField(max_length=5000)
  # likes= 
  comments= models.CharField(max_length=2000)
  created_date= models.DateField(default=timezone.now)

  profile= models.ForeignKey('auth.user',on_delete=models.CASCADE)
  
  
class Profile(models.Model):
  profile_photo= models.ImageField(blank=True, null=True)
  bio= models.CharField(max_length=1000)

