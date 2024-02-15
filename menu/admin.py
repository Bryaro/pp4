from django.contrib import admin
from .models import MenuItem


@admin.register(MenuItem)
class MenuItemAdmin(admin.ModelAdmin):
    """
    Admin interface customization for the MenuItem model.
    It defines how menu items are displayed within the Django admin panel,
    including which fields are shown in the list display
    and which fields are used for filtering.

    Attributes:
        list_display: display in the list view.
        list_filter: can be filtered.
    """

    list_display = (
        'title',
        'menu_type',
        'description',
        'image'
    )

    list_filter = ('menu_type',)
