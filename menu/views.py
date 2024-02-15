from django.shortcuts import render, redirect
from .forms import MenuItemForm
from .models import MenuItem


def index(request):
    """Renders the homepage."""
    return render(request, 'index.html')


def about(request):
    """Renders the about page."""
    return render(request, 'about.html')


def contact(request):
    """Renders the contact page."""
    return render(request, 'contact.html')


def add_menu_item(request):
    """
    Handles the addition of new menu items.
    If POST, processes the form and redirects to the menu.
    Otherwise, displays a blank form for adding a menu item.
    """
    if request.method == 'POST':
        form = MenuItemForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('menu')
    else:
        form = MenuItemForm()
    return render(request, 'add_menu.html', {'form': form})


def menu_list(request):
    """
    Displays the menu, separating items by type (coffee, pastry).
    """
    coffee_items = MenuItem.objects.filter(menu_type='coffee')
    pastry_items = MenuItem.objects.filter(menu_type='pastry')

    return render(request, 'menu/menu_list.html', {
        'coffee_items': coffee_items,
        'pastry_items': pastry_items
    })
