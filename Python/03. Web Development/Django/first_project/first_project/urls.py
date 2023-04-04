"""first_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from first_app import views

urlpatterns = [
    
    # Will enable you to access the admin page by typing PROJECT_ADDRESS/admin
    path('admin/', admin.site.urls),
    
    # Will include any view mapped in the first_app/views.py: PROJECT_ADDRESS/first_app/VIEW_NAME
    path('first_app/', include('first_app.urls')),
    
    # When oppening the PROJECT_ADDRESS, it will display the index view
    path('', views.index, name='index'),
    
    # Typing PROJECT_ADDRESS/formpage will open the form_name view mapped in frst_app.views.py
    path('formpage/', views.form_name_view, name="forms_page"),

    path('templates/', views.t_home, name='templates')
    
    
    
]
