from django import forms
from visitors.models import *
import datetime


class BookingsDateForm(forms.ModelForm):

    class Meta:
            model = Bookings
            fields = ['check_in', 'check_out']
            
class BookingsRoomForm(forms.ModelForm):
    class Meta:
        model = Bookings
        fields = ['room', 'visitor']
