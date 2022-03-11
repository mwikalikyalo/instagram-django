from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate,logout
from django.contrib import messages
from django.http  import HttpResponse, Http404
from .forms import  ImagesForm, CommentsForm, ProfileForm
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
        return redirect("page") 
    else:
        form = ImagesForm()    
    return render(request, 'page.html', {"current_user":current_user, "images": images, "form":form, "liked_images":liked_images})


"""New profile page if you are a new user """
@login_required(login_url='/accounts/login/')
def create_profile(request):
    current_user = request.user

    try:
        Profile.objects.get(user_id = current_user.id)
        return redirect("page")

    except:

        if request.method == 'POST':
            form = ProfileForm(request.POST, request.FILES)
            if form.is_valid():
                profile = form.save(commit = False)
                profile.user = current_user
                profile.save()

            return redirect("page")   

        else:
            form = ProfileForm()

    return render(request, 'create_profile.html', {"form": form, "current_user":current_user}) 

"""View profile"""
@login_required(login_url='/accounts/login/')
def profile(request, username):
    current_user = request.user
    profile =  Profile.objects.filter(user = User(id = current_user.id)).first()
    images = Image.objects.filter(profile = profile.pk ).all() 
        
    return render(request, 'profile.html', {"profile": profile, "images": images, "current_user": current_user})    


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
        return redirect("page")   

    else:
        form = ImagesForm()
    return render(request, 'images.html', {"form": form, "current_user":current_user}) 


"""Adding a comment"""
@login_required(login_url='/accounts/login/')
def comment(request, id):
     image = Image.objects.get(id = id)

     if request.method == 'POST':
        form = CommentsForm(request.POST, request.FILES)
        if form.is_valid():
            comment = form.save(commit = False)        
            comment.image = image
            comment.save()

        return redirect("page")   