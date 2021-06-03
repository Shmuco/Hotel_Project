from django.db import models
from django.utils.timezone import now
from django.conf import settings


# Create your models here.

class Rooms(models.Model):
    name = models.CharField(max_length=200)
    price = models.FloatField(null=False)
    avaliable = models.BooleanField(default=True)
    description = models.CharField(max_length=500)

    def __str__(self):
        return self.name
    

class Bookings(models.Model):
    visitor = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    room = models.ForeignKey(Rooms, null=False,on_delete=models.CASCADE)
    check_in = models.DateTimeField(default= now) 
    check_out = models.DateTimeField(default= now) 


class ContactForm(models.Model):
    name = models.CharField(max_length=50)
    phone_number = models.IntegerField()
    email = models.EmailField()
    message = models.CharField(max_length=300)


