from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

#Simple function that will display a "hello world" message
def index(request):
    return HttpResponse("<em>Hello World!</em>")