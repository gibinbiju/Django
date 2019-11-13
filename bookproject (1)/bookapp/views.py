from django.shortcuts import render, get_object_or_404, redirect
from .models import Book
from .forms import BookForm


# Create your views here.


def book_list(request,template_name='bookapp/book_list.html'):
    book=Book.objects.all()
    data={}
    data['object_list']=book
    return render(request,template_name,data)

def book_view(request,pk,template_name='bookapp/book_detail.html'):
    book=get_object_or_404(Book,pk=pk)
    return render(request,template_name,{'object':book})

def book_edit(request,pk,template_name='bookapp/book_form.html'):
    book=get_object_or_404(Book,pk=pk)
    form=BookForm(request.POST or None,instance=book)
    if form.is_valid():
        form.save()
        return book_list(request)
    return render(request,template_name,{'form':form})

def book_create(request,template_name='bookapp/book_form.html'):
    form=BookForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('book_list')
    return render(request,template_name,{'form':form})