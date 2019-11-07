from django.shortcuts import render

# Create your views here.
def register(request):
    return render(request,'register.html')
def home(request):
    return render(request,'base.html')
def view(request):
    return render(request,'show.html')
