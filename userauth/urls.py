from django.urls import path
from . import views
app_name = 'userauth'

urlpatterns = [
   path('register/', views.register, name='register'),
   path('login/', views.log, name='log')
]