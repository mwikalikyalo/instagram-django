from django.test import TestCase
from .models import Image, Profile
from .models import Profile, Image, User
from django.conf import settings

User=settings.AUTH_USER_MODEL
# Create your tests here.
# Create your tests here.
class ImagesTestClass(TestCase):
    def setUp(self):
        self.user= User(username='lovey')
        self.user.save()
        self.mwikali=Profile(user=self.user,bio='Live,love and laugh.',profile_photo='default.png')
       
        self.new_image = Image(image = 'image.png', image_names='', image_caption= 'Live,love and laugh.' , profile= self.mwikali) 

    def test_instance(self):
        self.assertTrue(self.new_image, Image)  

    def tearDown(self):
        Image.objects.all().delete()
        Profile.objects.all().delete()

    def test_save_image(self):
        self.new_image.save_image() 
        images = Image.objects.all()
        self.assertTrue(len(images) > 0) 
  
    def test_delete_image(self):
        self.new_image.delete_image()
        images = Image.objects.all()
        self.assertTrue(len(images)==0) 


class ProfileTestClass(TestCase):
    def setUp(self):

        self.user=User(username='rue')
        self.user.save()
        self.mwikali=Profile(user=self.user,bio='Live,love and laugh.',profile_photo='default.png')

    def tearDown(self):
        Profile.objects.all().delete()
        User.objects.all().delete()

    def test_instance(self):
        self.assertTrue(isinstance(self.mwikali, Profile))

    def test_saveProfile(self):
        self.mwikali.save_profile()
        profile_saved = Profile.objects.all()
        self.assertTrue(len(profile_saved) > 0)