from django.utils import timezone
from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class Image(models.Model):
  image= models.ImageField(blank=True, null=True)
  image_names= models.CharField(max_length=100)
  image_caption= models.CharField(max_length=5000)
  # likes= models.IntegerField()
  comments= models.CharField(max_length=2000)
  created_date= models.DateField(default=timezone.now)

  profile= models.ForeignKey('auth.user',on_delete=models.CASCADE)

  def save_image(self):
        self.save()
    
  def delete_image(self):
      Image.objects.filter(id = self.id).delete()

  def update_image(self, updates):
      Image.objects.filter(id = self.id).update(name = updates)
  
  
class Profile(models.Model):
  profile_photo= models.ImageField(blank=True, null=True)
  bio= models.CharField(max_length=1000)

  def save_profile(self):
      self.save()


    
  def delete_profile(self):
      Profile.objects.filter(id = self.id).delete()

  def update_image(self, updates):
      Profile.objects.filter(id = self.id).update(name = updates)