from django import forms
from .models import *
import datetime


class BookingsDateForm(forms.ModelForm):

    class Meta:
            model = Bookings
            fields = ['check_in', 'check_out']
            
class BookingsRoomForm(forms.ModelForm):
    class Meta:
        model = Bookings
        fields = ['room']

            


# class BookingsForm(forms.Form):
#     # visitor = forms.ModelChoiceField(queryset = settings.AUTH_USER_MODEL)
#     room = forms.ModelMultipleChoiceField(queryset = Rooms.objects.filter(avaliable = True))
#     check_in = forms.DateField(initial=datetime.date.today, )

#     check_out = forms.DateField(initial=datetime.date.today) 

