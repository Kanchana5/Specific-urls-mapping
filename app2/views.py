from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def first(request):
    return HttpResponse('<h1>This is my first string in appp2</h1>')
def second(request):
    return HttpResponse('<h1>This is my second string in appp2</h1>')