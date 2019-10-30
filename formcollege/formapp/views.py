from django.shortcuts import render
from .forms import clgform

# Create your views here.
def createclg(request):
    if request.method=='GET':
        form=clgform()
        return render(request,'formapp/registration.html',{'form':form})