from django.contrib import admin
from django.urls import path,include
from . import views
from django.shortcuts import render
urlpatterns = [

    # path('index',views.index,name="index"),
    path('reg',views.userform,name='reg'),
    path('',lambda request:render(request,'home.html'),name='home'),
    path('expense', views.expenseview, name='expense'),
    path('login', views.loginview, name='login'),
    path('home', lambda request: render(request, 'home.html'), name='home'),
    path('logout', views.logout, name='logout'),
    path('expense', lambda request: render(request, 'expense2.html'), name='add'),
    path('search', views.search, name='search'),
]
