from django.db import models
import calendar
class Registration(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    username = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    password = models.CharField(max_length=100)






class Search(models.Model):
    PLACE_CHOICE = [
        ('Hyderabad','Hyd'),
        ('Anantapur','ATP'),
        ('Bangalore','B'),
        ('Pune','P'),
        ('Chennai','C')
    ]
    Select_Place = models.CharField(max_length=25, choices=PLACE_CHOICE)
    Booking_Date = models.DateTimeField()
