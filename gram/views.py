from django.shortcuts import render,redirect
from .models import Image, Profile
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate,logout
from django.contrib import messages

# Create your views here.
def user_login(request):
  return render(request, 'registration/login.html', {})




