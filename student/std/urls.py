from django.contrib import admin
from django.shortcuts import render
from django.urls import path
from . import views
urlpatterns = [
    path("getpage",views.getRegistration,name="getpage"),
    path("register",views.insertToStudent,name="insert"),
    path("register",views.getStudentDetails,name="fetch"),
]