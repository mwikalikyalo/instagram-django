from django.shortcuts import render
from .models import Image, Profile
from django.contrib.auth.decorators import login_required
from django.views.generic import (
  ListView
)

# Create your views here.
class ImageListView(ListView):
  template_name= "page.html"
  queryset= Image.objects.all()
  context_object_name= 'images'


