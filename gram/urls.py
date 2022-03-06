from unicodedata import name
from django.urls import path, include
from .views import (
  ImageListView
)

app_name="gram"

urlpatterns= [path('', ImageListView.as_view(), name='page')]
