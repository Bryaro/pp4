from django import forms
from django.contrib.auth.models import User
from .models import UserProfile


class UserProfileForm(forms.ModelForm):
    """
    Form for updating user profile information.
    Allows users to update their:
    phone number, address, profile image, and optionally, their email.
    """
    new_email = forms.EmailField(label='New Email', required=False)

    def clean_new_email(self):
        new_email = self.cleaned_data.get('new_email')
        if User.objects.filter(email=new_email).exists():
            raise forms.ValidationError("This email is already in use.")
        return new_email

    class Meta:
        model = UserProfile
        fields = ['phone_number', 'address', 'image', 'new_email']
