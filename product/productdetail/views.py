from django.shortcuts import render
from .forms import productform
from .models import product
# Create your views here.
def insert(request):
    if request.method=='GET':
        form=productform()
        return render(request,"registration.html",{'form':form})
    if request.method=='POST'
        form=productform(request.POST)
        

