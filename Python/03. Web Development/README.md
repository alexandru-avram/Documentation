# Web Dev

## Web Scraping

#### [Basic Guide](https://github.com/alexandruavram-rusu/Documentation/blob/main/Python/03.%20Web%20Development/Web%20Scraping/Web%20Scraping%20-%200.%20Basic%20guide.ipynb)

    import requests
    import lxml
    import bs4

#### [Grabbing a Title](https://github.com/alexandruavram-rusu/Documentation/blob/main/Python/03.%20Web%20Development/Web%20Scraping/Web%20Scraping%20-%2001.%20Grabbin%20a%20Title.ipynb)

    <head>
        <title>Title on Browser Tab</title>
    </head>
    <body>...

#### [Grabbing a Class](https://github.com/alexandruavram-rusu/Documentation/blob/main/Python/03.%20Web%20Development/Web%20Scraping/Web%20Scraping%20-%2002.%20Grabbing%20a%20Class.ipynb)

* **soup.select('div')**	    All elements with the `<div>` tag
* **soup.select('#some_id')**	The HTML element containing the id attribute of some_id
* **soup.select('.notice')**	All the HTML elements with the CSS class named notice
* **soup.select('div span')**	Any elements named <span> that are within an element named `<div>`
* **soup.select('div > span')**	Any elements named <span> that are directly within an element named `<div>`, with no other element in between


#### [Grabbing an Image](https://github.com/alexandruavram-rusu/Documentation/blob/main/Python/03.%20Web%20Development/Web%20Scraping/Web%20Scraping%20-%2003.%20Grabbing%20an%20Image.ipynb)

    soup.select('img')
    
#### [Multiple Pages and Items](https://github.com/alexandruavram-rusu/Documentation/blob/main/Python/03.%20Web%20Development/Web%20Scraping/Web%20Scraping%20-%2004.%20%20Multiple%20Pages%20and%20Items.ipynb)
* Understand the structure of the page
* Get name of item to grab
* Get number of pages
* Create loop to grab items

## Django

[HTML & CSS Documentation](https://github.com/alexandruavram-rusu/Documentation/tree/main/HTML)

[Django Documentation](https://docs.djangoproject.com/en/4.1/intro/tutorial01/)

[Terminal Commands](https://www.techrepublic.com/article/16-terminal-commands-every-user-should-know/)
    
[django-admin & manage.py Commands](https://docs.djangoproject.com/en/4.1/ref/django-admin/)

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

### Django Basic Workflow    
    
#### Create new environment

With `conda`:
    
    conda create --env_name django

#### Activate environment

    activate --env_name
    
#### Create a project
    
    django-admin startproject --name
    
#### Run server
    
    python manage.py runserver

Starting development server: http://127.0.0.1:8000/

#### Create App
    
    python manage.py startapp --app_name

#### Add App to project
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
    

#### Add templates
##### 1. Create `templates` folder
##### 2. Create subfolders for each app
##### 3. Add template path to `TEMPLATES` in `settings.py`
    
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

##### 4. Use {{template_tag}} in template documents and differente URLs and `views.py` files
    
    def index(request):
    my_dict = {'template_tag': "Inserting a text using a template tag"}
    return render(request, 'APP_NAME/index.html', context=my_dict)
