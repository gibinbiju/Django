from django.shortcuts import render
from django.urls import path
from . import views
from django.contrib import admin
urlpatterns=[
    path('',lambda request:render(request,"home.html")),
    path('reg',views.input,name='reg'),
    path('home',lambda request:render(request,"home.html"),name='home'),
    path('calc',views.calc,name='calc'),
]