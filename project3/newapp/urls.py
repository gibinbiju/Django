from django.urls import path
from newapp import views

urlpatterns = [
    path("login", views.one, name="logi"),
    path("disp",views.calc, name="disp"),

]