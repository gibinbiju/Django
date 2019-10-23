from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from django.views import View
from django.views.generic import TemplateView


class IndexView(TemplateView):
    template_name = "index.html"
    message = "Hello"

    def get(self, request, *args, **kwargs):
        return render(request,"index.html",{"message":self.message})


class MessageView(View):
    def get(self,request):
        return HttpResponse("hello")

def index(request):
    return render(request, "index.html", {"message": "hello"})