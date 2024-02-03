from django.views.generic import TemplateView
from django.shortcuts import render


class index(TemplateView):
    template_name = 'home/index.html'

def about(request):
    return render(request, 'home/about.html')

def contact(request):
    return render(request, 'home/contact.html')

def reserve_table(request):
    return render(request, 'reservations/reserve_table.html')