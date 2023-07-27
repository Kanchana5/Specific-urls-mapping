from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def first(request):
    return HttpResponse('<h1> This is First string in app1</h1>')

def second(request):
    return HttpResponse('<h1> This is my second string in app1</h1>')
