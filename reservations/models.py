from django.db import models
from django.contrib.auth.models import User
import datetime

# Define the choices tuple
numb_of_guest_choices = (
    (1, "1 guest"),
    (2, "2 guests"),
    (3, "3 guests"),
    (4, "4 guests"),
    (5, "5 guests"),
    (6, "6 guests"),
    (7, "7 guests"),
    (8, "8 guests"),
)

times_for_reservation = (
    (datetime.time(7, 0), '7:00 AM'),
    (datetime.time(9, 0), '9:00 AM'),
    (datetime.time(11, 0), '11:00 AM'),
    (datetime.time(13, 0), '1:00 PM'),
    (datetime.time(15, 0), '3:00 PM'),
    (datetime.time(17, 0), '5:00 PM'),
    (datetime.time(19, 0), '7:00 PM'),
    (datetime.time(21, 0), '9:00 PM'),
    )


class Reservation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField()
    time = models.TimeField(choices=times_for_reservation)
    number_of_guests = models.IntegerField(choices=numb_of_guest_choices)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Resevation for {
            self.user.username} on {self.date} at {self.time}"
