from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    my_dict = {'insert_content': "HELLO. I'm from APP 2.1"}
    return render(request, 'app_2_1/index.html', context=my_dict)