from django.contrib import admin
from .models import UserProfile
from django.utils.html import format_html


class UserProfileAdmin(admin.ModelAdmin):
    """
    Admin configuration for user profiles.

    Display and search for user profiles in the Django admin interface.
    """
    list_display = ('user_id', 'user', 'phone_number')
    search_fields = ['phone_number']


admin.site.register(UserProfile, UserProfileAdmin)
