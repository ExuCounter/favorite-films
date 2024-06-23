from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def add_film(request):
    if request.method == "GET":
        return HttpResponse("result")
