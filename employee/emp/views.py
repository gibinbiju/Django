from django.shortcuts import render
from .forms import empform
from .models import Desig,Employee,Company
def create(request):
    if request.method=='GET':
        print("Hai")
        form=empform()
        return render(request,'registration.html',{'form':form})
def input(request):
    print("inside insert method")
    cname=request.POST.get("companyname")
    desig=request.POST.get("designation")
    name = request.POST.get("ename")
    sal = request.POST.get("esal")
    try:
        obj = Desig.objects.all(designation=desig)
        obj.save()
        obj=Company.objects.all(companyname=cname)
        obj.save()
        obj=Employee.objects.all(ename=name,esal=sal)
        obj.save()
    except Exception as e:
        print(e.args)
        msg = e.args
        return render(request, 'registration.html', {'msg': msg})

    return render(request, 'home.html')
def Details(request):
    print("inside student")
    obj = Employee.objects.all()
    return render(request, 'show.html', {"object_list":obj})


# Create your views here.
