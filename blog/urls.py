"""myBlog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from .views import PostCreateView, PostUpdateView, PostDeleteView
from blog import views

urlpatterns = [
    path('', views.home, name='home'),
    path('blog/', views.blog, name='blog'),
    #path('blog/', PostListView.as_view(), name='blog'),
    path('blog/new/', PostCreateView.as_view(), name='blog-new'),
    path('blogpost/<int:pk>/update/', PostUpdateView.as_view(), name='blog-update'),
    path('blogpost/<str:slug>/delete/', PostDeleteView.as_view(), name='blog-delete'),
    path('search/', views.search, name='search'),
    path('blogpost/<str:slug>', views.blogpost, name='blog-slug'),
    path('contact/', views.contact, name='contact'),
    path('leafle/', views.leafle, name='leafle')
]