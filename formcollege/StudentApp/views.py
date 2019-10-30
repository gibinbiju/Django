from django.shortcuts import render
from StudentApp.models import Student


# Create your views here.
def getRegistration(request):
    return render(request, 'registration.html')


def insertToStudent(request):
    print("inside insert method")
    name = request.POST.get("name")
    addr = request.POST.get("addr")
    total = request.POST.get("total")
    try:
        obj = Student(name=name, address=addr, course=total)
        obj.save()
    except Exception as e:
        print(e.args)
        msg = e.args
        return render(request, 'registration.html', {'msg': msg})

    return render(request, 'home.html')


def getStudentDetails(request):
    print("inside student")
    obj = Student.objects.all()
    return render(request, 'studentDetails.html', {"object_list":obj})
def searchstudent(request):
    sname = request.POST.get("sname")
    print(sname)
    try:
        obj = Student.objects.filter(name=sname)
        return render(request, 'studentDetails.html', {"object_list": obj})
    except Exception as e:
        print(e.args)
        msg = e.args
        return render(request, 'home.html', {'msg': msg})

def search(request):
    return render(request,"search.html")
