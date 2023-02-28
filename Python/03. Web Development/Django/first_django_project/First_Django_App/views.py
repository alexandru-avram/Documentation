from django.shortcuts import render
from django.http import HttpResponse
# Create your views here

# This is a view which will return an HttpResponse object
# This view should be mapped to the url.py file
def index(resquest): 
    return HttpResponse("Hello World")
