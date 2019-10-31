from django.shortcuts import render
from StudentApp.models import Student


# Create your views here.
def getRegistration(request):
    return render(request, 'registration.html')


def insertToStudent(request):
    print("inside insert method")
    name = request.POST.get("name")
    addr = request.POST.get("addr")
    course = request.POST.get("course")
    try:
        obj = Student(name=name, address=addr, course=course)
        obj.save()
    except Exception as e:
        print(e.args)
        msg = e.args
        return render(request, 'registration.html', {'msg': msg})

    return render(request, 'home.html')


def getStudentDetails(request):
    print("inside student")
    obj = Student.objects.all()
    return render(request, 'studentDetails.html', {"object_list": obj})
def searchstudent(request):
    sname = request.POST.get("sname")
    scourse = request.POST.get("course")
    print(scourse)
    try:
        if sname == None:
            obj = Student.objects.filter(course=scourse)
            return render(request, 'studentDetails.html', {"object_list": obj})
        elif scourse ==None:
            obj = Student.objects.filter(name=sname)
            return render(request, 'studentDetails.html', {"object_list": obj})
        else:
            obj = Student.objects.filter(name=sname).filter(course=scourse)
            return render(request, 'studentDetails.html', {"object_list": obj})
    except Exception as e:
        print(e.args)
        msg = e.args
        return render(request, 'home.html', {'msg': msg})

def search(request):
    return render(request,"search.html")
