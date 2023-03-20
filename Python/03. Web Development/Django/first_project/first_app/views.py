from django.shortcuts import render
from django.http import HttpResponse


# Create your views here

# 
# def index(request):
#    return HttpResponse("<em>Simple text with HTML tags</em>")

def index(request):
    my_dict = {'insert_me': "Inserting a text using a template tag"}
    return render(request, 'first_app/index.html', context=my_dict)