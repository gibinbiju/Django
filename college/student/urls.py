from django.urls import path
from student import views

urlpatterns = [
    path("register", views.register, name="regi"),
    path("login", views.login, name="logi"),

]