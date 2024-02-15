from django.shortcuts import render, redirect
from .forms import MenuItemForm
from .models import MenuItem


def index(request):
    return render(request, 'index.html')


def about(request):
    return render(request, 'about.html')


def contact(request):
    return render(request, 'contact.html')


def add_menu_item(request):
    if request.method == 'POST':
        form = MenuItemForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('menu')
    else:
        form = MenuItemForm()
    return render(request, 'add_menu.html', {'form': form})


def menu_list(request):
    coffee_items = MenuItem.objects.filter(menu_type='coffee')
    pastry_items = MenuItem.objects.filter(menu_type='pastry')

    return render(request, 'menu/menu_list.html', {
        'coffee_items': coffee_items,
        'pastry_items': pastry_items
    })
