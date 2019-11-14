from django.shortcuts import render
from basicformapp.forms import newuserform,login,expenseform,searchform
from .models import users,expense,category
from django.db.models import Min,Max,Sum
# Create your views here.
# def index(request):
    # return render(request, 'basicformapp/users.html', {'form':form})

def userform(request):
    if request.method == "GET":
        form=newuserform()
    if request.method=="POST":
        form=newuserform(request.POST)
        if form.is_valid():
            form.save(commit=True)
            print("Success")
            # return index(request)
            return render(request, 'home.html', {'form': form})
        else:
            print('error from invalid')
    return render(request,'basicformapp/users.html',{'form':form})

def loginview(request):
    if request.method == 'GET':
        form = login()
        print("inside get")
        return render(request,'login.html', {'form': form})
    if request.method == 'POST':
        form = login(request.POST)
        if form.is_valid():
            print("form is valid")
            #form.save(commit=True)

            name = form.cleaned_data['username']
            pwd = form.cleaned_data['pwd']

            print(name,pwd)

            if users.objects.filter(username=name).filter(pwd=pwd):
               print("login successfull")
               request.session['user']=name
               return render(request, 'mypage.html', {'form': form})


            else:
                print("incorrect Username / Password")

    return render(request, 'login.html', {'form': form})
def expenseview(request):
    if request.method == "GET":
        form=expenseform()
        return render(request, 'expense.html', {'form': form})
    if request.method=="POST":
        form=expenseform(request.POST)
        if form.is_valid():
            u=users.objects.get(username=request.session['user'])
            category=form.cleaned_data['category_name']
            amount=form.cleaned_data['amount']
            e=expense(name=u,category_name=category,amount=amount)
            e.save()
            print("Success")
            # return index(request)
            return render(request, 'expense2.html', {'form': form})
        else:
            print('error from invalid')
            return render(request, 'expense.html', {'form': form})
def logout(request):
    del request.session['user']
    return render(request, 'home.html')
def search(request):
    if request.method == 'GET':
        form = searchform()
        return render(request, 'search.html', {'form': form})
    if request.method=='POST':
        form=searchform(request.POST)
        if form.is_valid():
            dates = form.cleaned_data['dates']
            if request.POST.get('max'):
                u = expense.objects.filter(dates=dates).aggregate(Max('amount'))
                print("Max operation")
                return render(request, 'search2.html', {'u': u,})
            elif request.POST.get('min'):
                u = expense.objects.filter(dates=dates).aggregate(Min('amount'))
                print("Min operation")
                return render(request, 'search2.html', {'u': u,})
            elif request.POST.get('total'):
                u = expense.objects.aggregate(Sum('amount'))
                print("total expense operation")
                return render(request, 'search2.html', {'u': u})
            else:
                u = expense.objects.filter(dates=dates)
                print("Full data operation")
                return render(request, 'search2.html', {'u':u})
    return render(request,'search.html',{'form':form})