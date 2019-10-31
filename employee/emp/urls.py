from django.contrib import admin
from django.shortcuts import render
from django.urls import path
from . import views
urlpatterns = [
   path('',lambda request:render(request,"home.html")),
    path('reg',views.create,name='reg'),
    path('insert',views.input,name='insert'),
    path('home',lambda request:render(request,"home.html"),name='home'),
    path('show',views.Details,name='show'),

]