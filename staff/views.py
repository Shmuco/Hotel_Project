from typing import Generic
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import generic
from visitors.models import *
from .forms import *
from django.contrib.admin.views.decorators import staff_member_required



# Create your views here.
# @staff_member_required(login_url='homepage')
def allbookings (request):

    bookings = Bookings.objects.all()
    print(bookings)
    return render (request, 'all_bookings.html', {'bookings': bookings})

# @staff_member_required
def booking_date_staff(request):
    form = BookingsDateForm()

    if request.method == "POST":
        check_in = request.POST["check_in"]
        check_out = request.POST["check_out"]
        return redirect("booking_room_staff", check_in, check_out)

    return render(request, "make_booking.html", {"form": form})

# @staff_member_required
def booking_room_staff(request, check_in, check_out):
    form = BookingsRoomForm()
    # check_in = datetime.datetime.strptime(check_in)
    # check_out = datetime.datetime.strptime(check_out)
    rooms_booked = Bookings.objects.filter(check_in__gt=check_in, check_out__lt=check_out)
    print(rooms_booked)
    li = []
    print(li)
    for i in rooms_booked:
        print(i.room)
    form.fields['room'].queryset = Rooms.objects.all().exclude()
    if request.method == "POST":
        
        return redirect("homepage")

    return render(request, "make_booking.html", {"form": form})

# @staff_member_required
class EditBooking(generic.UpdateView):
    template_name = 'make_booking.html'
    model = Bookings
    fields = '__all__'
    success_url = reverse_lazy('homepage')

    def form_valid(self, form):
        post_to_add = form.cleaned_data
        print(post_to_add)
        return super().form_valid(form) 

# @staff_member_required
class ViewBooking(generic.DetailView):
    model = Bookings
    template_name = 'view_booking.html'
# @staff_member_required
class DeleteBooking(generic.DeleteView):
    model = Bookings
    success_url = reverse_lazy('allbookings')

    def delete(self, request, *args, **kwargs):

        return super(DeleteBooking, self).delete(request, *args, **kwargs)


@staff_member_required
def messages(request):
    messages = ContactForm.objects.all()

    return render(request, 'messages.html', {'messages':messages})

