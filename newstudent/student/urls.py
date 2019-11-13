from django.shortcuts import render
from django.urls import path,include
from . import views
urlpatterns = [
    path('', lambda request: render(request, 'registration/home.html'), name='home'),
    path('home', lambda request: render(request, 'registration/home.html'), name='home'),
    path('reg',views.register,name='reg'),
    path('login',include('django.contrib.auth.urls'),name='login'),
]