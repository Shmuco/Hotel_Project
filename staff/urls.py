from django.urls import path
from django.contrib.admin.views.decorators import staff_member_required

from . import views

urlpatterns = [
    path('allbookings/',staff_member_required(views.allbookings), name = 'allbookings'),
    path('viewbooking/<slug:pk>',views.ViewBooking.as_view(), name = 'viewbooking'),
    path('newbooking/date',views.booking_date_staff, name = 'booking_date_staff'),
    path('newbooking/room/<str:check_in>/<str:check_out>/,',views.booking_room_staff, name = 'booking_room_staff'),
    path('editbooking/<slug:pk>,',views.EditBooking.as_view(), name = 'editbooking'),
    path('/<slug:pk>/delete', views.DeleteBooking.as_view(), name= 'delete_booking'),
    path('messages/', views.messages, name = 'messages')
]
