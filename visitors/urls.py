from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from . import views

urlpatterns = [
     path('homepage/', views.ContactForm.as_view(), name='homepage'),
     path('newbooking/date', views.booking_date, name = 'newbooking_date'),
     path('newbooking/room/<str:check_in>/<str:check_out>/', views.booking_room, name = 'newbooking_room'),
     path('rooms', views.display_rooms, name= 'rooms'),
     path('addroom', views.AddRoom.as_view(), name= 'add_room'),
]
