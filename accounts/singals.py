from django.dispatch import receiver
from allauth.account.signals import email_confirmed

@receiver(email_confirmed)
def email_verified(email_address, **kwargs):
    # Set email_verified to True once email is confirmed
    email_address.user.email_verified = True
    email_address.user.save()
