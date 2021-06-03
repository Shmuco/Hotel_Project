from visitors.models import ContactForm, Rooms
from visitors.forms import BookingsForm
from django.shortcuts import render, redirect
from django.views import generic
from django.urls import reverse_lazy


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