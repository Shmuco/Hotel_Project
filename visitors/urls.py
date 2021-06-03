from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from . import views

urlpatterns = [
     path('homepage/', views.ContactForm.as_view(), name='homepage'),
     path('newbooking/', views.newbooking, name = 'newbooking'),
     path('rooms', views.display_rooms, name= 'rooms'),
     path('addroom', views.AddRoom.as_view(), name= 'rooms'),


    
]
