from django.http import HttpResponse
def index(request):
    return HttpResponse("<h1>Hello World</h1>")
def name(request):
    return HttpResponse("<h3>Kraken</h3>")
