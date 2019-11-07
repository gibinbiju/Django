from django.shortcuts import render
from .forms import primeform
#from .models import primesum

def input(request):
    if request.method=='GET':
        form=primeform()
        return render(request,'input.html',{'form':form})
    if request.method=='POST':
        form=primeform(request.POST)
        return calc(request)
def sum(a,b):
    l=int(a)
    u=int(b)
    s=0
    c=0
    for i in range(l,u+1):
        c=0
        for j in range(2,i):
            if(i%j==0):
                c=1
                break
        if c==0:
            s=s+i
    return s

def calc(request):
    l=request.POST.get('l')
    u=request.POST.get('u')
    s=sum(l,u)
    print(s)
    return render(request,'result.html',{'s':s})

