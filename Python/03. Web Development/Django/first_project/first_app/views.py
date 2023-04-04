from django.shortcuts import render
from django.http import HttpResponse
from first_app.models import Topic, Webpage, AccessRecord
from . import forms

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
"""
def index(request):
    webpages_list = AccessRecord.objects.order_by('date') # create a list and order it by the date field
    date_dict = {'access_records': webpages_list}

    
    return render(request, 'first_app/index.html', context=date_dict)
"""

# Forth view: Create Django forms
def index(request):

    return render(request, 'first_app/index.html')

# Forms view
def form_name_view(request):
    form = forms.FormName()

    # Insert the POST method in our form
    if request.method == 'POST':
        form = forms.FormName(request.POST)

    # DO SOMETHING CODE
    # Will post in the console
        if form.is_valid():
            print("VALIDATION SUCCESS!")
            print("NAME: " +form.cleaned_data['name'])
            print("EMAIL: " +form.cleaned_data['email'])
            print("TEXT: " +form.cleaned_data['text'])

    return render(request, 'first_app/form_page.html', context={'form':form})


# Relative URL Template Tagging
def t_home(request):
    return render(request, 'first_app/first_app_templates/t_home.html')

def t_base(request):
    return render(request, 'first_app/first_app_templates/t_base.html')

def t_tagging(request):
    return render(request, 'first_app/first_app_templates/t_tagging.html')

def t_filters(request):
    context_dict = {"text":"This is a context dictionary",
                    "number":100}
    return render(request, 'first_app/first_app_templates/t_filters.html', context=context_dict)
