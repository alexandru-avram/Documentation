# Django


[HTML & CSS Documentation](https://github.com/alexandruavram-rusu/Documentation/tree/main/HTML)

[Django Documentation](https://docs.djangoproject.com/en/4.1/intro/tutorial01/)

[Terminal Commands](https://www.techrepublic.com/article/16-terminal-commands-every-user-should-know/)
    
[django-admin & manage.py Commands](https://docs.djangoproject.com/en/4.1/ref/django-admin/)

## Folder Structure

### Django Project Basic Structure
- `__init__.py`: blank Python script that due to its special name let’s Python know that this directory can be treated as a package
- `settings.py`: where you will store all your project settings
- `urls.py`: Python script that will store all the URL patterns for your project. different pages for the web application
- `wsgi.py`: Python script that acts as the Web Server Gateway Interface, helping us deploy our web app to production
- `manage.py`: Python script that is associated with many commands as we build our web app

### Django App Basic Structure
- `__init__.py`: blank Python script that due to its special name let’s Python know that this directory can be treated as a package
- `admin.py`: register your models here which Django will then use them with Django’s admin interface
- `apps.py`: you can place application specific configurations
- `models.py`: store the application’s data models
- `tests.py`: store test functions to test your code
- `views.py`: you have functions that handle requests and return responses
- `Migrations` folder: this directory stores database specific information as it relates to the models

## Django Basic Workflow    
    
### Create new environment

With `conda`:
    
    conda create --env_name django
    
With 'venv':

    python3 -m venv venv

### Activate environment

    activate --env_name
    
### Create a project
    
    django-admin startproject --name
    
### Run server
    
    python manage.py runserver

Starting development server: http://127.0.0.1:8000/

### Create App
    
    python manage.py startapp --app_name

#### Map App to project
##### 1. Add app to `settings.py` in the `INSTALLED_APPS` list
    
    INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'APP_NAME']
 
##### 2. Create `urls.py` file in the app directory and add `url patterns`
    from django.urls import path
    from . import views

    urlpatterns = [
    path('', views.index, name='index')
    ]
    
    
##### 3. Add app and path to `ulrs.py`
    from django.contrib import admin
    from django.urls import path, include
    from APP_NAME import views

    urlpatterns = [
    path('admin/', admin.site.urls),
    path('APP_NAME/', include('APP_NAME.urls')), 
    ]
    

## Add templates
#### 1. Create `templates` folder
#### 2. Create subfolders for each app
#### 3. Add template path to `TEMPLATES` in `settings.py`
    
    TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
    ]

#### 4. Use ` {{template_tag}} ` in template documents and differente URLs and `views.py` files
    
    def index(request):
    my_dict = {'template_tag': "Inserting a text using a template tag"}
    return render(request, 'APP_NAME/index.html', context=my_dict)

## Loading static files
#### 1. Create new `static` folder
#### 2. Create subfolders for each type of items or for each app
#### 3. Add `{%load static %} ` to the templates you want to use
    
    {%load static %}

#### 4. Files can be used in the templates (* ex: image example.jpg*)
    
    <img src="{% static 'images/example.jpg' %}" alt="The image didn't appear">
    
## Loading CSS styles
#### 1. Create `css` subfolder in the `static` folder
#### 2. Make sure the `{%load static %} ` to the templates in which you want to use css
#### 3. Link the HTML file to the CSS file
    
     <link rel= "stylesheet" href="{% static 'css/css_style.css' %}">

## Create models
#### 1. Create Django classes in the `models.py` file in the App
[Django models documentation](https://docs.djangoproject.com/en/4.1/topics/db/models/)
    
    class ClassName(models.Model):
        class1 = models.Class(CLASS_CHARACTERISTICS)
