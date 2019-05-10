from django.urls import path
from PhotogalleryForArchitects2 import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
]