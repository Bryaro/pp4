from django import forms
from .models import Reservation

class RservationForm(forms.ModelForm):
    
    class Meta:
        model = Rservation
        fields = ['date','time', 'number_of_guests']
