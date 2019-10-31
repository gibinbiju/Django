from django.contrib import admin
from django.shortcuts import render
from django.urls import path
from . import views
urlpatterns = [
   path('',lambda request:render(request,"formapp/home.html")),
    path('reg',views.createclg,name='reg'),
    path('home',lambda request:render(request,"formapp/home.html"),name='home'),
    path('save',views.save,name='save'),
    path('display',views.display,name='display')

]