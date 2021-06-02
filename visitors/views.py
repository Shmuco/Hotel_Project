from visitors.models import Bookings
from visitors.forms import BookingsForm
from django.shortcuts import render, redirect

# Create your views here

def homepage(request):
    return render(request, 'homepage.html')


def newbooking(request):
    if request.method == 'GET':
            return render (request, 'new_booking.html', {'form': BookingsForm, 'add_type': 'form'})
        
    if request.method == 'POST':
        data = request.POST
        form = BookingsForm(data)
        if form.is_valid():
            form.save()
    return redirect('new_booking')