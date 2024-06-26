from django.shortcuts import render

# Create your views here.


def home(request):
    return render(request, "films/home.html")


def login(request):
    return render(request, "films/login.html")


def register(request):
    return render(request, "films/register.html")
