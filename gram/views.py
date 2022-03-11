from django.shortcuts import render,redirect
from .models import Image, Profile
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate,logout
from django.contrib import messages

# Create your views here.
def user_login(request):
  if request.method == "POST":
    username= request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    if user is not None:
          login(request, user)
          # Redirect to a success page.
          return redirect('page')
    else:
          messages.success(request, 'Cannot login. Try again')
          # Return an 'invalid login' error message.
          return redirect('login')

  else: 
   return render(request, 'registration/login.html', {})




