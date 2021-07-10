from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,"hello/index.html")

def chen(request):
    return HttpResponse("Hey there Chen!")

def steve(request):
    return HttpResponse("Hey there Steve!")

def greet(request, name):
    return render(request, "hello/greet.html", {
        "name": name.capitalize()
    })