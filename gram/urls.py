from unicodedata import name
from . import views
from django.urls import path

app_name="gram"

urlpatterns= [
  path('user_login', views.user_login, name="login"),

]
