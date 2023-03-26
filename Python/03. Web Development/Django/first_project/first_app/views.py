from django.shortcuts import render
from django.http import HttpResponse
from first_app.models import Topic, Webpage, AccessRecord

# Create your views here

# First view: simple display of a text with HTML tags
"""
def index(request):
    return HttpResponse("<em>Simple text with HTML tags</em>")
"""


# Second view: Using template tagging
"""
def index(request):
    my_dict = {'insert_me': "Inserting a text using a template tag"}
    return render(request, 'first_app/index.html', context=my_dict)
"""

# Third view: Create a view using first_app models
def index(request):
    webpages_list = AccessRecord.objects.order_by('date') # create a list and order it by the date field
    date_dict = {'access_records': webpages_list}

    
    return render(request, 'first_app/index.html', context=date_dict)
