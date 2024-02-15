from django.contrib import admin
from .models import MenuItem


@admin.register(MenuItem)
class MenuItemAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'menu_type',
        'description',
        'image'
    )

    list_filter = ('menu_type',)
