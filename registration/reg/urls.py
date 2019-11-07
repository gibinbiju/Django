from django.urls import path
from reg import views

urlpatterns = [
    path("register", views.register, name="regi"),
    path("base", views.home, name="base"),
    path("view", views.view, name="show"),


]