from visitors.models import ContactForm, Rooms
from django.shortcuts import render, redirect
from django.views import generic
from django.urls import reverse_lazy
from .forms import *
from dateutil.parser import parse
from django.utils.timezone import make_aware

# Create your views here

def homepage(request):
    return render(request, 'homepage.html')


# def newbooking(request):
#     if request.method == 'GET':
#             return render (request, 'new_booking.html', {'form': BookingsForm, 'add_type': 'form'})
        
#     if request.method == 'POST':
#         data = request.POST
#         form = BookingsForm(data)
#         if form.is_valid():
#             form.save()
#     return redirect('new_booking')


def display_rooms(request):
    
    rooms = Rooms.objects.all()

    return render(request, 'all_rooms.html', {'rooms': rooms })


class AddRoom(generic.CreateView):
    template_name = 'form.html'
    model = Rooms
    fields = ['name','price', 'description']
    success_url = reverse_lazy('homepage')
    

    def form_valid(self, form):
        post_to_add = form.cleaned_data
        return super().form_valid(form) 


class ContactForm(generic.CreateView):
    template_name = 'homepage.html'
    model = ContactForm
    fields = '__all__'
    success_url = reverse_lazy('homepage')
    

    def form_valid(self, form):
        post_to_add = form.cleaned_data
        return super().form_valid(form) 



def booking_date(request):
    form = BookingsDateForm()

    if request.method == "POST":
        check_in = request.POST["check_in"]
        check_out = request.POST["check_out"]
        return redirect("newbooking_room", check_in, check_out)

    return render(request, "form.html", {"form": form})

def booking_room(request, check_in, check_out):
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

    return render(request, "form.html", {"form": form})




def book_room(request, start_stay, end_stay):
    start_stay = date.fromisoformat(start_stay)
    end_stay = date.fromisoformat(end_stay)
    form = BookingRoomForm()
    form.fields["room_number"].queryset = Room.objects.filter(
        Q(booking__start_of_stay__gt=end_stay) or Q(booking__end_of_stay__lt=start_stay)
    )
    print(Room.objects.filter(Q(booking=None)))
    if request.method == "POST":
        return redirect("hotel_info")
    return render(request, "visitors/book_room.html", {"form": form})