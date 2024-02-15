from django import forms
from .models import MenuItem


class MenuItemForm(forms.ModelForm):
    class Meta:
        model = MenuItem
        fields = ['title',
                  'description',
                  'price',
                  'image',
                  'image_alt',
                  'menu_type'
                  ]
