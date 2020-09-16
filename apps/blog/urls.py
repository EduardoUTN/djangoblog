from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('blog/', views.home , name='home'),
    path('posts', views.posts , name='posts'),
]