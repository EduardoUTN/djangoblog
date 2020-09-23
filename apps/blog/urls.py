from django.contrib import admin
from django.urls import path
from .views import PostDetailView, PostCreateView, PostUpdateView, PostUpdateView, PostDeleteView
from . import views

urlpatterns = [
    path('', views.home , name='home'),
    path('post/<int:pk>', PostDetailView.as_view(), name='post-detail'),
    path('post/new', PostCreateView.as_view(), name='post-new'),
    path('post/edit/<int:pk>', PostUpdateView.as_view(), name='post-edit'),
    path('post/delete/<int:pk>', PostDeleteView.as_view(), name='post-delete'),
    path('posts', views.posts , name='posts')
]