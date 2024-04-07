from django.urls import path
from . import views
app_name = 'website'

urlpatterns = [
    path('home/', views.homeview, name='home'),
    path('about/', views.aboutview, name='about'),
    path('contact/', views.contactview, name='contact')
]