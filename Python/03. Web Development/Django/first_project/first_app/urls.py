from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from . import views

# TEMPLATE TAGGING
app_name = 'first_app'

# URL PATTERNS
urlpatterns = [
    path('', views.index, name='index'),
    path('forms_page/', views.form_name_view, name = 'forms_page'),
    path('templates/', views.t_home, name='templates' ),
    path('templates/filters', views.t_filters, name='template_filters'),
    
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)