from django.db import models
from django.contrib.auth.models import User
from django_resized import ResizedImageField
from django.db.models.signals import post_save
from django.dispatch import receiver


class UserProfile(models.Model):
    """
    Represents a user profile linked to the Django User model.
    It stores additional information
    about the user such as phone number, address, email, profile image,
    and email verification status with text.
    The image is resized to 300x300 pixels with 75% quality in WEBP format.
    """
    user = models.OneToOneField(
        User, related_name="profile",
        on_delete=models.CASCADE,
        primary_key=True)
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    email = models.EmailField(default='')
    image = ResizedImageField(
        size=[300, 300],
        quality=75,
        upload_to='profile_images/',
        force_format="WEBP",
        blank=True,
        null=True,
        )
    updated_on = models.DateField(auto_now=True)
    is_email_verified = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.user.username} Profile'


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    """
    Signal handler to create a UserProfile instance automatically
    when a new User instance is created.
    This ensures that each User has an associated UserProfile,
    for storing additional information.
    """
    if created:
        UserProfile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    """
    Signal handler to save the UserProfile instance
    automatically whenever the User instance is saved.
    This keeps the UserProfile information up to date,
    with the User instance changes.
    """
    instance.profile.save()
