from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from . import views

urlpatterns = [
     path('homepage/', views.homepage, name='homepage'),
     path('newbooking/', views.newbooking, name = 'newbooking')

    
]
