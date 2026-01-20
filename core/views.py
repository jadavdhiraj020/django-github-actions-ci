from django.http import HttpResponse
from django.shortcuts import render


def add(a:int, b:int):
    return a+b


def home(request):
    return HttpResponse("<h1>Django CI/CD Deployment Successful!</h1><br><h2>Hello Dhiraj</h2>")
