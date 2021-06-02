from django import forms
from .models import *
import datetime


class BookingsForm(forms.Form):
    # visitor = forms.ModelChoiceField(queryset = settings.AUTH_USER_MODEL)
    room = forms.ModelMultipleChoiceField(queryset = Rooms.objects.filter(avaliable = True))
    check_in = forms.DateField(initial=datetime.date.today, )

    check_out = forms.DateField(initial=datetime.date.today) 
