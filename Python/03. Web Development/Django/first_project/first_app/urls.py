from django.urls import path
from first_app import views

urlpatters = [
    path('', views.index, name='index')
]