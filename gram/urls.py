from unicodedata import name
from . import views
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name="gram"

urlpatterns= [
  path('', views.page, name = 'page'),
  path('new/profile/', views.new_profile, name = 'new_profile'),
  path('profile/<str:username>/', views.profile, name = 'profile'),
  path('comments/image/<int:id>/', views.comment, name= 'comment'),
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)


