from django.http import HttpResponse
from django.shortcuts import render


def add(a:int, b:int):
    return a+b



def index(request):
    return HttpResponse("Hello, World! This is a simple HTTP response from Django.")
