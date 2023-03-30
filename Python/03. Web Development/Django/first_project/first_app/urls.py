from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('', views.form_name_view, name = 'forms_page')
    
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)