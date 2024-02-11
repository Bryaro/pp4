from django import forms
from .models import UserProfile

class UserProfileForm(forms.ModelForm):
    new_email = forms.EmailField(label='New Email', required=False)

    class Meta:
        model = UserProfile
        fields = ['email', 'phone_number', 'address', 'image']