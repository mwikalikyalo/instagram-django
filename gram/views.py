from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate,logout
from django.contrib import messages
from django.http  import HttpResponse, Http404
from .forms import  ImagesForm, CommentsForm
from django.contrib.auth.models import User
from .models import Image, Profile, Comments, Likes

# Create your views here.

@login_required(login_url='/accounts/login/')
def home(request):
    current_user = request.user
    images = Image.objects.all().order_by("date_posted").reverse()
    liked_images = [i for i in Image.objects.all() if Likes.objects.filter(user = request.user, image=i)]

    if request.method == 'POST':
        form = ImagesForm(request.POST, request.FILES)
        if form.is_valid():
            image = form.save(commit = False)
            image.profile = Profile.objects.get(user_id = current_user.id)
            image.save()

        return redirect("home") 

    else:
        form = ImagesForm()    

    return render(request, 'home.html', {"current_user":current_user, "images": images, "form":form, "liked_images":liked_images})

""" Uploading images"""
@login_required(login_url='/accounts/login/')
def upload_images(request):
    current_user = request.user

    if request.method == 'POST':
        form = ImagesForm(request.POST, request.FILES)
        if form.is_valid():
            image = form.save(commit = False)
            image.profile = Profile.objects.get(user_id = current_user.id)
            image.save()

        return redirect("home")   

    else:
        form = ImagesForm()

    return render(request, 'images.html', {"form": form, "current_user":current_user}) 







def user_login(request):
  if request.method == "POST":
    username= request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    if user is not None:
          login(request, user)
          return redirect('page')
    else:
          messages.success(request, 'Cannot login. Try again')
          return redirect('login')

  else: 
   return render(request, 'registration/login.html', {})


