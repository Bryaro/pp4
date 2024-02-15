from django.dispatch import receiver
from allauth.account.signals import email_confirmed


@receiver(email_confirmed)
def email_verified(email_address, **kwargs):
    """
    Signal handler that sets:
    the user's email verification status to True upon email confirmation.
    This is triggered by the `email_confirmed` signal from django-allauth,
    when a user's email address is successfully verified.

    Args:
        email_address: The EmailAddress instance that was confirmed.
    """
    # Set email_verified to True once email is confirmed
    email_address.user.email_verified = True
    email_address.user.save()
