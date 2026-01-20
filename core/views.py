from django.http import HttpResponse
from django.shortcuts import render


def add(a:int, b:int):
    return a+b


def home(request):
    return HttpResponse("🎉 Django CI/CD Deployment Successful!")
