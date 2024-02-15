from django.db import models
from django_resized import ResizedImageField

# Choice Fields for Menu
MENU_TYPES = (
    ('coffee', 'Coffee'),
    ('pastry', 'Pastry')
)


class MenuItem(models.Model):
    """
    Represents an item in menu, including info of title, description, price,
    image, and type (e.g., coffee, pastry).
    Images are resized and stored in WEBP format.
    """
    title = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=5, decimal_places=2)
    image = ResizedImageField(
        size=[400, None],
        quality=75,
        upload_to='menu/',
        force_format="WEBP",
        blank=False,
        null=False
    )
    image_alt = models.CharField(max_length=100, null=False, blank=False)
    menu_type = models.CharField(
        max_length=50, choices=MENU_TYPES, default='coffee')

    def __str__(self):
        return self.title
