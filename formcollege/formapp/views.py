from django.shortcuts import render
from .forms import clgform
from .models import Student

# Create your views here.
def createclg(request):
    if request.method=='GET':
        form=clgform()
        return render(request,'formapp/registration.html',{'form':form})
    if request.method=='POST':
        form=clgform(request.POST)
        if form.is_valid():
            print("validation success")
            print("Name:"+form.cleaned_data['name'])
            print("Address:" + form.cleaned_data['address'])
            print("Course:" + form.cleaned_data['course'])
    return render(request, 'formapp/home.html', {'form': form})
def save(request):
    name=request.POST.get('name')
    addr=request.POST.get('address')
    course=request.POST.get('course')
    try:
        s = Student(name=name, address=addr, course=course)
        s.save()
    except Exception as e:
        print(e.args)
    return display(request)
def display(request):
    s=Student.objects.all()
    return render(request,'formapp/Detail.html', {"object_list":s})

