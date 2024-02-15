from django import forms
from .models import MenuItem


class MenuItemForm(forms.ModelForm):
    """
    Form for managing MenuItem data.
    It allows for creating and editing menu items,
    including fields like:
    title, description, price, image, and menu type.
    """
    class Meta:
        model = MenuItem
        fields = ['title',
                  'description',
                  'price',
                  'image',
                  'image_alt',
                  'menu_type'
                  ]
