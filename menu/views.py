from django.shortcuts import render, redirect
from .forms import MenuItemForm
from .models import MenuItem

# Create your views here.
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
    menu_items = MenuItem.objects.all()  # Retrieves all menu items from the database
    return render(request, 'menu/menu_list.html', {'menu_items': menu_items})