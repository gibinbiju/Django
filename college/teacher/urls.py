from django.urls import path
from teacher import views

urlpatterns = [
    path("register", views.register, name="reg"),
    path("login", views.login, name="log"),

]
