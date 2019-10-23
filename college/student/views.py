from django.shortcuts import render

def register(request):
    return render(request,'student/registration.html')

def login(request):
    return render(request,'student/login.html')
