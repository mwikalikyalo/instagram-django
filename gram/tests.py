from django.test import TestCase
from .models import Image, Profile

# Create your tests here.
class ImagesTestClass(TestCase):
    def setUp(self):
        self.post = Profile(name = "_miss.mwikali")
        self.post.save_profile()

        self.new_image = Image(name = '', image = 'image.png', description = 'This is a random test' , location = self.newYork, category = self.wildlife) 

    def test_instance(self):
        self.assertTrue(self.new_image, Image)  

    def tearDown(self):
        Image.objects.all().delete()
        Profile.objects.all().delete()

    def test_save_image(self):
        self.new_image.save_image() 
        images = Image.objects.all()
        self.assertTrue(len(images) > 0) 
  
    def test_delete_method(self):
        self.post.delete_profile()
        images = Image.objects.all()
        self.assertTrue(len(images)==0) 