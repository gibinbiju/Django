from django.shortcuts import render
from django.urls import path
from . import views
urlpatterns = [
    path('', lambda request: render(request, 'registration/home.html'), name='home'),
    path('home', lambda request: render(request, 'registration/home.html'), name='home'),
   # path('reg',views.register,name='reg'),
]