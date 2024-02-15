# reservations/forms.py
from django import forms
from .models import Reservation


class CustomTimeInput(forms.TimeInput):
    """
    Custom widget for time input to ensure consistent formatting and user experience.
    """
    input_type = 'time'

    def format_value(self, value):
        if isinstance(value, str):
            return value
        return value.strftime('%H:%M') if value else ''


class ReservationForm(forms.ModelForm):
    """
    Form for creating or updating reservations with custom widgets for date and time fields.
    """
    class Meta:
        model = Reservation
        fields = ['date', 'time', 'number_of_guests']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
        }
