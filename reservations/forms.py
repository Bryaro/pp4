# reservations/forms.py
from django import forms
from .models import Reservation


class CustomTimeInput(forms.TimeInput):
    input_type = 'time'

    def format_value(self, value):
        if isinstance(value, str):
            return value
        return value.strftime('%H:%M') if value else ''


class ReservationForm(forms.ModelForm):
    class Meta:
        model = Reservation
        fields = ['date', 'time', 'number_of_guests']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
        }
