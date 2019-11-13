from django.shortcuts import render
from .models import User,Feedback
from .forms import Reg_form
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from  django import forms

def register(request):
    if request.method=='GET':
        form=Reg_form()
        print("insiade form")
        return render(request,'signup.html',{'form':form,})
    if request.method=='POST':
        form=Reg_form(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return render(request, 'registration/home.html', {'form': form})

def login_request(request):
    return render(request,'registration/home.html')