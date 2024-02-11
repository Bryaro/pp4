from django.db import models
from django.contrib.auth.models import User

from django_resized import ResizedImageField
from django.db.models.signals import post_save
from django.dispatch import receiver


# Create your models here.

class UserProfile(models.Model):
    user = models.OneToOneField(User, related_name="profile", on_delete=models.CASCADE, primary_key=True)
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    email = models.EmailField(default='')
    image = ResizedImageField(
        size=[300,300],
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
    print(f"User created: {created}, User instance: {instance}")
    if created:
        UserProfile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()