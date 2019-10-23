from django.shortcuts import render
def one(request):
    return render(request,'newapp/login.html')
def calc(request):
    num1=int(request.POST.get('num1'))
    num2=int(request.POST.get('num2'))
    print(num1+num2)
    return render(request,'newapp/login.html')