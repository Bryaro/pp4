from django.contrib import admin
from .models import UserProfile
from django.utils.html import format_html

# Register your models here.

class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user_id', 'user', 'phone_number')
    search_fields = ['phone_number']

admin.site.register(UserProfile, UserProfileAdmin)