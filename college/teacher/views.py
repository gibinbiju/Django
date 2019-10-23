from django.shortcuts import render

def register(request):
    return render(request,'teacher/registration.html')

def login(request):
    return render(request,'teacher/login.html')
