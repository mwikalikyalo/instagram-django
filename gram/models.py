from django.utils import timezone
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
  profile_photo= models.ImageField(blank=True, null=True)
  bio= models.CharField(max_length=1000)
  user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)

  def save_profile(self):
      self.save()
 
  def delete_profile(self):
      Profile.objects.filter(id = self.id).delete()

  def update_image(self, updates):
      Profile.objects.filter(id = self.id).update(name = updates)

  @classmethod
  def search_by_user(cls,search_term):
        person = cls.objects.filter(user__icontains=search_term)
        return person   


class Image(models.Model):
  image= models.ImageField()
  image_names= models.CharField(max_length=100)
  image_caption= models.CharField(max_length=5000)
  created_date= models.DateField(default=timezone.now)

  profile= models.ForeignKey('auth.user',on_delete=models.CASCADE)

  def save_image(self):
        self.save()
    
  def delete_image(self):
      Image.objects.filter(id = self.id).delete()

  def update_image(self, updates):
      Image.objects.filter(id = self.id).update(name = updates)
  
  
class Comments(models.Model):
    comment = models.TextField(max_length=5000)
    # image = models.ForeignKey(Image,related_name='comments', on_delete=models.CASCADE)

    def save_comment(self):
        self.save()   

    def delete_comment(self):
        self.save()   


class Likes(models.Model):
    likes=models.IntegerField()
    # user = models.ForeignKey(User, related_name= 'like', on_delete=models.CASCADE)

    def save_likes(self):
        self.save()

    def delete_likes(self):
        self.save() 



